from abc import abstractmethod
from typing import Any

from mopipe.core.segments.io import IOType, IOTypeBaseMixin


class InputTypeBaseMixin(IOTypeBaseMixin):
    """Mixin class for all segments input types."""

    _input_type: IOType

    @property
    def input_type(self) -> IOType:
        """The type of the input."""
        return self._input_type

    def _ensure_input_exists(self, **kwargs) -> bool:
        """Ensure that the input exists."""
        if "x" in kwargs:
            return True
        return False

    @abstractmethod
    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        raise NotImplementedError


class UnivariateSeriesInput(InputTypeBaseMixin):
    """Mixin class for univariate series input segments."""

    _input_type = IOType.UNIVARIATE_SERIES

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_series_or_dataframe(kwargs["x"]):
            return False
        if not self._validate_shape(kwargs["x"], row_min=2, col_max=1):
            return False
        return True


class MultivariateSeriesInput(InputTypeBaseMixin):
    """Mixin class for multivariate series input segments."""

    _input_type = IOType.MULTIVARIATE_SERIES

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_series_or_dataframe(kwargs["x"]):
            return False
        if not self._validate_shape(kwargs["x"], row_min=2, col_min=2):
            return False
        return True


class SingleValueInput(InputTypeBaseMixin):
    """Mixin class for single value input segments."""

    _input_type = IOType.SINGLE_VALUE

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_single_value(kwargs["x"]):
            return False
        return True


class MultiValueInput(InputTypeBaseMixin):
    """Mixin class for multiple values input segments."""

    _input_type = IOType.MULTIPLE_VALUES

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_multiple_values(kwargs["x"]):
            return False
        return True


class SingleNumericValueInput(InputTypeBaseMixin):
    """Mixin class for single numeric value input segments."""

    _input_type = IOType.SINGLE_NUMERIC_VALUE

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_single_numeric_value(kwargs["x"]):
            return False
        return True


class AnySeriesInput(InputTypeBaseMixin):
    """Mixin class for any series input segments."""

    _input_type = IOType.ANY_SERIES

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_any_series(kwargs["x"]):
            return False
        return True


class AnyNumericInput(InputTypeBaseMixin):
    """Mixin class for any numeric input segments."""

    _input_type = IOType.ANY_NUMERIC

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_any_numeric(kwargs["x"]):
            return False
        return True


class AnyInput(InputTypeBaseMixin):
    """Mixin class for any input segments."""

    _input_type = IOType.ANY

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(**kwargs):
            return False
        if not self._validate_any(kwargs["x"]):
            return False
        return True


class OtherInput(InputTypeBaseMixin):
    """Mixin class for other input segments."""

    _input_type = IOType.OTHER

    @abstractmethod
    def _validate_other(self, x: Any) -> bool:
        """Validate that the input is other type."""
        msg = "Other input type must be implemented by subclass."
        raise NotImplementedError(msg)

    def validate_input(self, **kwargs) -> bool:
        """Validate the input."""
        if not self._validate_other(kwargs["x"]):
            return False
        return True
