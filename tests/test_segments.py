import numpy as np
import pandas as pd
import pytest  # type: ignore

from mopipe.segment import CalcShift, ColMeans, CrossRQAStats, Mean, RQAStats, SimpleGapFilling, WindowedCrossRQAStats


class TestMean:
    @pytest.fixture
    def segment(self) -> Mean:
        return Mean("TestMean")

    def test_process_valid_series(self, segment: Mean) -> None:
        series = pd.Series([1, 2, 3, 4, 5])
        assert segment.process(series) == 3.0

    def test_process_invalid_series(self, segment: Mean) -> None:
        series = pd.Series([])
        assert np.isnan(segment.process(series))


class TestColMeans:
    @pytest.fixture
    def segment(self) -> ColMeans:
        return ColMeans("TestColMeans")

    def test_process_with_int_col(self, segment: ColMeans) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        result = segment.process(df, col=0)
        assert isinstance(result, pd.Series)
        assert result.array == [2.0]

    def test_process_with_str_col(self, segment: ColMeans) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        result = segment.process(df, col="A")
        assert isinstance(result, pd.Series)
        assert result.array == [2.0]

    def test_process_with_slice_col(self, segment: ColMeans) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        output = segment.process(df, col=slice(0, 3))
        assert isinstance(output, pd.Series)
        assert output.array == [2.0, 5.0, 8.0]

    def test_process_with_none_col(self, segment: ColMeans) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        output = segment.process(df, col=None)
        assert isinstance(output, pd.Series)
        assert output.array == [2.0, 5.0, 8.0]

    def test_process_with_invalid_col(self, segment: ColMeans) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        with pytest.raises(ValueError):
            segment.process(df, col=1.5)  # type: ignore


class TestRQAStats:
    @pytest.fixture
    def segment(self) -> RQAStats:
        return RQAStats("TestRQAStats")

    def test_recurrence_measures(self, segment: RQAStats) -> None:
        x = pd.Series([1, 1, 2, 2])
        res = segment.process(x)
        assert res.loc[0, "recurrence_rate"] == 0.5
        assert res.loc[0, "determinism"] == 0.5
        res = segment.process(x, lmin=5)
        assert res.loc[0, "determinism"] == 0
        res = segment.process(x, threshold=2)
        assert res.loc[0, "recurrence_rate"] == 1


class TestCrossRQAStats:
    @pytest.fixture
    def segment(self) -> CrossRQAStats:
        return CrossRQAStats("TestCrossRQAStats")

    def test_cross_recurrence_measures(self, segment: CrossRQAStats) -> None:
        x = pd.DataFrame({"a": [1, 1, 2, 2, 1, 1, 2, 2], "b": [3, 3, 2, 2, 3, 3, 2, 2]})
        res = segment.process(x, col_a=0, col_b=1)
        assert res.loc[0, "recurrence_rate"] == 0.25
        res = segment.process(x, col_a="a", col_b="b")
        assert res.loc[0, "recurrence_rate"] == 0.25
        res = segment.process(x, col_a="a", col_b="a")
        assert res.loc[0, "recurrence_rate"] == 0.5
        res = segment.process(x)
        assert res.loc[0, "recurrence_rate"] == 0.5


class TestWindowedCrossRQAStats:
    @pytest.fixture
    def segment(self) -> WindowedCrossRQAStats:
        return WindowedCrossRQAStats("TestWindowedCrossRQAStats")

    def test_cross_recurrence_measures(self, segment: WindowedCrossRQAStats) -> None:
        x = pd.DataFrame({"a": [1, 1, 2, 2, 1, 1, 1, 1], "b": [3, 3, 2, 2, 3, 3, 2, 2]})
        res = segment.process(x, col_a=0, col_b=1, window=4, step=2)
        assert res.shape[0] == 3
        assert res.loc[0, "recurrence_rate"] == 0.25
        assert res.loc[1, "recurrence_rate"] == 0.25
        assert res.loc[2, "recurrence_rate"] == 0.0


class TestCalcShift:
    @pytest.fixture
    def segment(self) -> CalcShift:
        return CalcShift("TestCalcShift")

    def test_calc_shift(self, segment: CalcShift) -> None:
        x = pd.DataFrame({"a": [1, 1, 2, 2, 1, 1, 1, 1], "b": [3, 3, 2, 2, 3, 3, 2, 2]})
        res = segment.process(x, cols=["a"], shift=2)
        assert res.shape[1] == 3
        assert "a_shift" in res.columns
        assert res["a_shift"].array == [0, 0, 1, 1, -1, -1, 0, 0]
        assert res["a_shift"].mean() == 0.0


class TestSimpleGapFilling:
    @pytest.fixture
    def segment(self) -> SimpleGapFilling:
        return SimpleGapFilling("TestGapFilling")

    def test_gap_filling(self, segment: SimpleGapFilling) -> None:
        x = pd.DataFrame({"a": [1, 1, 2, np.nan, 1, 1, 1, 1], "b": [3, 3, 2, 2, np.nan, np.nan, 2, 2]})
        res = segment.process(x)
        assert res["a"][3] == 1.5
        assert res["b"][4] == 2
        assert res["b"][5] == 2
