import typing as t
from abc import abstractmethod

from mopipe.segments.io import IOType, IOTypeBaseMixin


class OutputTypeBaseMixin(IOTypeBaseMixin):
    """Mixin class for all segments output types."""

    _output_type: IOType

    @property
    def output_type(self) -> IOType:
        """The type of the output."""
        return self._output_type

    @abstractmethod
    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        raise NotImplementedError


class UnivariateSeriesOutput(OutputTypeBaseMixin):
    """Mixin class for univariate series output segments."""

    _output_type = IOType.UNIVARIATE_SERIES

    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        if not self._validate_series_or_dataframe(output):
            return False
        if not self._validate_shape(output, row_min=2, col_max=1):
            return False
        return True

class MultivariateSeriesOutput(OutputTypeBaseMixin):
    """Mixin class for multivariate series output segments."""

    _output_type = IOType.MULTIVARIATE_SERIES

    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        if not self._validate_series_or_dataframe(output):
            return False
        if not self._validate_shape(output, row_min=2, col_min=2):
            return False
        return True

class SingleValueOutput(OutputTypeBaseMixin):
    """Mixin class for single value output segments."""

    _output_type = IOType.SINGLE_VALUE

    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        if not self._validate_single_value(output):
            return False
        return True

class MultiValueOutput(OutputTypeBaseMixin):
    """Mixin class for multiple values output segments."""

    _output_type = IOType.MULTIPLE_VALUES

    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        if not self._validate_multiple_values(output):
            return False
        return True


class AnyOutput(OutputTypeBaseMixin):
    """Mixin class for any output segments."""

    _output_type = IOType.ANY

    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        if not self._validate_any(output):
            return False
        return True


class OtherOutput(OutputTypeBaseMixin):
    """Mixin class for other output segments."""

    _output_type = IOType.OTHER

    def validate_output(self, output: t.Any) -> bool:
        """Validate the output."""
        if not self._validate_any(output):
            return False
        return True
