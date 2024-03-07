import numpy as np
import pandas as pd
import pytest  # type: ignore

from mopipe.core.segments.seg import Segment
from mopipe.segment import ColMeans, Mean, RQAStats, CrossRQAStats, WindowedCrossRQAStats, CalcShift


class TestMean:
    @pytest.fixture
    def segment(self) -> Segment:
        return Mean("TestMean")

    def test_process_valid_series(self, segment: Segment) -> None:
        series = pd.Series([1, 2, 3, 4, 5])
        assert segment.process(series) == 3.0

    def test_process_invalid_series(self, segment: Segment) -> None:
        series = pd.Series([])
        assert np.isnan(segment.process(series))


class TestColMeans:
    @pytest.fixture
    def segment(self) -> Segment:
        return ColMeans("TestColMeans")

    def test_process_with_int_col(self, segment: Segment) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert segment.process(df, col=0) == 2.0

    def test_process_with_str_col(self, segment: Segment) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert segment.process(df, col="A") == 2.0

    def test_process_with_slice_col(self, segment: Segment) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        output = segment.process(df, col=slice(0, 3))
        assert np.array_equal(output.values, np.array([2.0, 5.0, 8.0]))

    def test_process_with_none_col(self, segment: Segment) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        output = segment.process(df, col=None)
        assert np.array_equal(output.values, np.array([2.0, 5.0, 8.0]))

    def test_process_with_invalid_col(self, segment: Segment) -> None:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        with pytest.raises(ValueError):
            segment.process(df, col=1.5)


class TestRQAStats:
    @pytest.fixture
    def segment(self) -> Segment:
        return RQAStats("TestRQAStats")

    def test_recurrence_measures(self, segment: Segment) -> None:
        x = pd.Series([1,1,2,2])
        res = segment.process(x)
        assert res.loc[0, "recurrence_rate"] == 0.5
        assert res.loc[0, "determinism"] == 0.5
        res = segment.process(x, lmin=5)
        assert res.loc[0, "determinism"] == 0
        res = segment.process(x, threshold=2)
        assert res.loc[0, "recurrence_rate"] == 1


class TestCrossRQAStats:
    @pytest.fixture
    def segment(self) -> Segment:
        return CrossRQAStats("TestCrossRQAStats")

    def test_cross_recurrence_measures(self, segment: Segment) -> None:
        x = pd.DataFrame({"a": [1,1,2,2,1,1,2,2], "b": [3,3,2,2,3,3,2,2]})
        res = segment.process(x, colA=0, colB=1)
        assert res.loc[0, "recurrence_rate"] == 0.25
        res = segment.process(x, colA="a", colB="b")
        assert res.loc[0, "recurrence_rate"] == 0.25
        res = segment.process(x, colA="a", colB="a")
        assert res.loc[0, "recurrence_rate"] == 0.5
        res = segment.process(x)
        assert res.loc[0, "recurrence_rate"] == 0.5


class TestWindowedCrossRQAStats:
    @pytest.fixture
    def segment(self) -> Segment:
        return WindowedCrossRQAStats("TestWindowedCrossRQAStats")

    def test_cross_recurrence_measures(self, segment: Segment) -> None:
        x = pd.DataFrame({"a": [1,1,2,2,1,1,1,1], "b": [3,3,2,2,3,3,2,2]})
        res = segment.process(x, colA=0, colB=1, window=4, step=2)
        assert res.shape[0] == 3
        assert res.loc[0, "recurrence_rate"] == 0.25
        assert res.loc[1, "recurrence_rate"] == 0.25
        assert res.loc[2, "recurrence_rate"] == 0.


class TestCalcShift:
    @pytest.fixture
    def segment(self) -> Segment:
        return CalcShift("TestCalcShift")

    def test_calc_shift(self, segment: Segment) -> None:
        x = pd.DataFrame({"a": [1,1,2,2,1,1,1,1], "b": [3,3,2,2,3,3,2,2]})
        res = segment.process(x, col=0, shift=2)
        assert res.shape[1] == 3
        assert (res["a_shift"].values == [0,0,1,1,-1,-1,0,0]).mean() == 1.0
