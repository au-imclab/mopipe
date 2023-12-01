from mopipe.segments.io import IOType


class InputTypeMixin:
    """Mixin class for all segments input types."""

    _input_type: IOType

    @property
    def input_type(self) -> IOType:
        """The type of the input."""
        return self._input_type


class UnivariateSeriesInputMixin(InputTypeMixin):
    """Mixin class for univariate series input segments."""

    _input_type = IOType.UNIVARIATE_SERIES


class MultivariateSeriesInputMixin(InputTypeMixin):
    """Mixin class for multivariate series input segments."""

    _input_type = IOType.MULTIVARIATE_SERIES


class SingleValueInputMixin(InputTypeMixin):
    """Mixin class for single value input segments."""

    _input_type = IOType.SINGLE_VALUE


class MultipleValuesInputMixin(InputTypeMixin):
    """Mixin class for multiple values input segments."""

    _input_type = IOType.MULTIPLE_VALUES


class AnyInputMixin(InputTypeMixin):
    """Mixin class for any input segments."""

    _input_type = IOType.ANY


class OtherInputMixin(InputTypeMixin):
    """Mixin class for other input segments."""

    _input_type = IOType.OTHER
