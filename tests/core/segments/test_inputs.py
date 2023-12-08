from typing import Any

import pandas as pd
import pytest  # type: ignore

from mopipe.core.segments.inputs import (
    AnyInput,
    MultiValueInput,
    MultivariateSeriesInput,
    OtherInput,
    SingleValueInput,
    UnivariateSeriesInput,
)


class TestUnivariateSeriesInput:
    @pytest.fixture
    def univariate_series_input(self) -> UnivariateSeriesInput:
        return UnivariateSeriesInput()

    def test_validate_input_with_valid_input(self, univariate_series_input: UnivariateSeriesInput):
        series = pd.Series([1, 2, 3])
        assert univariate_series_input.validate_input(x=series) is True
        dataframe = pd.DataFrame({"A": [1, 2, 3]})
        assert univariate_series_input.validate_input(x=dataframe) is True

    def test_validate_input_with_invalid_input(self, univariate_series_input: UnivariateSeriesInput):
        dataframe = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert univariate_series_input.validate_input(x=dataframe) is False


class TestMultivariateSeriesInput:
    @pytest.fixture
    def multivariate_series_input(self) -> MultivariateSeriesInput:
        return MultivariateSeriesInput()

    def test_validate_input_with_valid_input(self, multivariate_series_input: MultivariateSeriesInput):
        dataframe = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert multivariate_series_input.validate_input(x=dataframe) is True

    def test_validate_input_with_invalid_input(self, multivariate_series_input: MultivariateSeriesInput):
        series = pd.Series([1, 2, 3])
        assert multivariate_series_input.validate_input(x=series) is False


class TestSingleValueInput:
    @pytest.fixture
    def single_value_input(self) -> SingleValueInput:
        return SingleValueInput()

    def test_validate_input_with_valid_input(self, single_value_input: SingleValueInput):
        value = 10
        assert single_value_input.validate_input(x=value) is True

    def test_validate_input_with_invalid_input(self, single_value_input: SingleValueInput):
        series = pd.Series([1, 2, 3])
        assert single_value_input.validate_input(x=series) is False


class TestMultiValueInput:
    @pytest.fixture
    def multi_value_input(self) -> MultiValueInput:
        return MultiValueInput()

    def test_validate_input_with_valid_input(self, multi_value_input: MultiValueInput):
        values = [1, 2, 3]
        assert multi_value_input.validate_input(x=values) is True

    def test_validate_input_with_invalid_input(self, multi_value_input: MultiValueInput):
        value = 10
        assert multi_value_input.validate_input(x=value) is False


class TestAnyInput:
    @pytest.fixture
    def any_input(self) -> AnyInput:
        return AnyInput()

    def test_validate_input_with_valid_input(self, any_input: AnyInput):
        values = [1, "test", None, [1, 2, 3]]
        for value in values:
            assert any_input.validate_input(x=value) is True


class TestOtherInput:
    @pytest.fixture
    def other_input(self) -> OtherInput:
        return OtherInput()  # type: ignore

    def test_validate_input_with_valid_input(self, other_input: OtherInput):
        with pytest.raises(NotImplementedError):
            other_input.validate_input(x=10)


class TestOtherInputImplementation:
    @pytest.fixture
    def other_input(self) -> OtherInput:
        class OtherInputImplementation(OtherInput):
            def _validate_other(self, x: Any) -> bool:  # noqa: ARG002
                return True

        return OtherInputImplementation()  # type: ignore

    def test_validate_input_with_valid_input(self, other_input: OtherInput):
        assert other_input.validate_input(x=10) is True
