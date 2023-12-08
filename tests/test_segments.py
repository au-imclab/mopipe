import numpy as np
import pandas as pd
import pytest  # type: ignore

from mopipe.core.segments.seg import Segment
from mopipe.segment import ColMeans, Mean


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
