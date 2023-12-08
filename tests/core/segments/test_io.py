import pandas as pd
import pytest  # type: ignore

from mopipe.core.segments.io import IOTypeBaseMixin


class TestIOTypeBaseMixin:
    @pytest.fixture
    def io_type_base_mixin(self) -> IOTypeBaseMixin:
        return IOTypeBaseMixin()  # type: ignore

    def test_validate_series(self, io_type_base_mixin: IOTypeBaseMixin):
        series = pd.Series([1, 2, 3])
        assert io_type_base_mixin._validate_series(series) is True

    def test_validate_series_with_non_series_input(self, io_type_base_mixin: IOTypeBaseMixin):
        dataframe = pd.DataFrame({"A": [1, 2, 3]})
        assert io_type_base_mixin._validate_series(dataframe) is False

    def test_validate_dataframe(self, io_type_base_mixin: IOTypeBaseMixin):
        dataframe = pd.DataFrame({"A": [1, 2, 3]})
        assert io_type_base_mixin._validate_dataframe(dataframe) is True

    def test_validate_dataframe_with_non_dataframe_input(self, io_type_base_mixin: IOTypeBaseMixin):
        series = pd.Series([1, 2, 3])
        assert io_type_base_mixin._validate_dataframe(series) is False

    def test_validate_series_or_dataframe_with_series_input(self, io_type_base_mixin: IOTypeBaseMixin):
        series = pd.Series([1, 2, 3])
        assert io_type_base_mixin._validate_series_or_dataframe(series) is True

    def test_validate_series_or_dataframe_with_dataframe_input(self, io_type_base_mixin: IOTypeBaseMixin):
        dataframe = pd.DataFrame({"A": [1, 2, 3]})
        assert io_type_base_mixin._validate_series_or_dataframe(dataframe) is True

    def test_validate_series_or_dataframe_with_non_series_or_dataframe_input(self, io_type_base_mixin: IOTypeBaseMixin):
        value = 10
        assert io_type_base_mixin._validate_series_or_dataframe(value) is False

    def test_validate_single_value_with_single_value_input(self, io_type_base_mixin: IOTypeBaseMixin):
        value = 10
        assert io_type_base_mixin._validate_single_value(value) is True

    def test_validate_single_value_with_non_single_value_input(self, io_type_base_mixin: IOTypeBaseMixin):
        series = pd.Series([1, 2, 3])
        assert io_type_base_mixin._validate_single_value(series) is False

    def test_validate_multiple_values_with_multiple_values_input(self, io_type_base_mixin: IOTypeBaseMixin):
        values = [1, 2, 3]
        assert io_type_base_mixin._validate_multiple_values(values) is True

    def test_validate_multiple_values_with_single_value_input(self, io_type_base_mixin: IOTypeBaseMixin):
        value = 10
        assert io_type_base_mixin._validate_multiple_values(value) is False

    def test_validate_any(self, io_type_base_mixin: IOTypeBaseMixin):
        values = [1, "test", None, [1, 2, 3]]
        for value in values:
            assert io_type_base_mixin._validate_any(value) is True

    def test_validate_shape_with_valid_shape(self, io_type_base_mixin: IOTypeBaseMixin):
        dataframe = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert io_type_base_mixin._validate_shape(dataframe, row_min=1, col_min=2) is True

    def test_validate_shape_with_invalid_shape(self, io_type_base_mixin: IOTypeBaseMixin):
        series = pd.Series([1, 2, 3])
        assert io_type_base_mixin._validate_shape(series, row_min=2, col_min=2) is False
