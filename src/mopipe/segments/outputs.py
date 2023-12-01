from mopipe.segments.io import IOType


class OutputTypeMixin:
    """Mixin class for all segments output types."""

    _output_type: IOType

    @property
    def output_type(self) -> IOType:
        """The type of the output."""
        return self._output_type


class UnivariateSeriesOutputMixin(OutputTypeMixin):
    """Mixin class for univariate series output segments."""

    _output_type = IOType.UNIVARIATE_SERIES


class MultivariateSeriesOutputMixin(OutputTypeMixin):
    """Mixin class for multivariate series output segments."""

    _output_type = IOType.MULTIVARIATE_SERIES


class SingleValueOutputMixin(OutputTypeMixin):
    """Mixin class for single value output segments."""

    _output_type = IOType.SINGLE_VALUE


class MultipleValuesOutputMixin(OutputTypeMixin):
    """Mixin class for multiple values output segments."""

    _output_type = IOType.MULTIPLE_VALUES


class AnyOutputMixin(OutputTypeMixin):
    """Mixin class for any output segments."""

    _output_type = IOType.ANY


class OtherOutputMixin(OutputTypeMixin):
    """Mixin class for other output segments."""

    _output_type = IOType.OTHER
