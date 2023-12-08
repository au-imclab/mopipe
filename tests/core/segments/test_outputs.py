import pandas as pd
import pytest  # type: ignore

from mopipe.core.segments.outputs import (
    AnyOutput,
    MultiValueOutput,
    MultivariateSeriesOutput,
    OtherOutput,
    SingleValueOutput,
    UnivariateSeriesOutput,
)


class TestUnivariateSeriesOutput:
    @pytest.fixture
    def univariate_series_output(self) -> UnivariateSeriesOutput:
        return UnivariateSeriesOutput()

    def test_validate_output_with_valid_output(self, univariate_series_output: UnivariateSeriesOutput):
        series = pd.Series([1, 2, 3])
        assert univariate_series_output.validate_output(series) is True
        dataframe = pd.DataFrame({"A": [1, 2, 3]})
        assert univariate_series_output.validate_output(dataframe) is True

    def test_validate_output_with_invalid_output(self, univariate_series_output: UnivariateSeriesOutput):
        dataframe = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert univariate_series_output.validate_output(dataframe) is False


class TestMultivariateSeriesOutput:
    @pytest.fixture
    def multivariate_series_output(self) -> MultivariateSeriesOutput:
        return MultivariateSeriesOutput()

    def test_validate_output_with_valid_output(self, multivariate_series_output: MultivariateSeriesOutput):
        dataframe = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert multivariate_series_output.validate_output(dataframe) is True

    def test_validate_output_with_invalid_output(self, multivariate_series_output: MultivariateSeriesOutput):
        series = pd.Series([1, 2, 3])
        assert multivariate_series_output.validate_output(series) is False


class TestSingleValueOutput:
    @pytest.fixture
    def single_value_output(self) -> SingleValueOutput:
        return SingleValueOutput()

    def test_validate_output_with_valid_output(self, single_value_output: SingleValueOutput):
        value = 10
        assert single_value_output.validate_output(value) is True

    def test_validate_output_with_invalid_output(self, single_value_output: SingleValueOutput):
        series = pd.Series([1, 2, 3])
        assert single_value_output.validate_output(series) is False


class TestMultiValueOutput:
    @pytest.fixture
    def multi_value_output(self) -> MultiValueOutput:
        return MultiValueOutput()

    def test_validate_output_with_valid_output(self, multi_value_output: MultiValueOutput):
        values = [1, 2, 3]
        assert multi_value_output.validate_output(values) is True

    def test_validate_output_with_invalid_output(self, multi_value_output: MultiValueOutput):
        value = 10
        assert multi_value_output.validate_output(value) is False


class TestAnyOutput:
    @pytest.fixture
    def any_output(self) -> AnyOutput:
        return AnyOutput()

    def test_validate_output_with_valid_output(self, any_output: AnyOutput):
        values = [1, "test", None, [1, 2, 3]]
        for value in values:
            assert any_output.validate_output(value) is True


class TestOtherOutput:
    @pytest.fixture
    def other_output(self) -> OtherOutput:
        return OtherOutput()  # type: ignore

    def test_validate_output_with_valid_output(self, other_output: OtherOutput):
        value = 10
        with pytest.raises(NotImplementedError):
            other_output.validate_output(value)


class TestOtherOutputImplementation:
    class OtherOutputImplementation(OtherOutput):
        def _validate_other(self, output: int) -> bool:  # noqa: ARG002
            return True

    @pytest.fixture
    def other_output_implementation(self) -> OtherOutputImplementation:
        return self.OtherOutputImplementation()

    def test_validate_output_with_valid_output(self, other_output_implementation: OtherOutputImplementation):
        value = 10
        assert other_output_implementation.validate_output(value) is True
