from abc import abstractmethod
from typing import Any

from mopipe.segments.io import IOType, IOTypeBaseMixin


class InputTypeBaseMixin(IOTypeBaseMixin):
    """Mixin class for all segments input types."""

    _input_type: IOType

    @property
    def input_type(self) -> IOType:
        """The type of the input."""
        return self._input_type

    def _ensure_input_exists(self, *args, **kwargs) -> bool:  # noqa: ARG002
        """Ensure that the input exists."""
        if "input" in kwargs:
            return True
        return False

    @abstractmethod
    def validate_input(self, *args, **kwargs) -> bool:
        """Validate the input."""
        raise NotImplementedError


class UnivariateSeriesInput(InputTypeBaseMixin):
    """Mixin class for univariate series input segments."""

    _input_type = IOType.UNIVARIATE_SERIES

    def validate_input(self, *args, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(*args, **kwargs):
            return False
        if not self._validate_series_or_dataframe(kwargs["input"]):
            return False
        if not self._validate_shape(kwargs["input"], row_min=2, col_max=1):
            return False
        return True


class MultivariateSeriesInput(InputTypeBaseMixin):
    """Mixin class for multivariate series input segments."""

    _input_type = IOType.MULTIVARIATE_SERIES

    def validate_input(self, *args, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(*args, **kwargs):
            return False
        if not self._validate_series_or_dataframe(kwargs["input"]):
            return False
        if not self._validate_shape(kwargs["input"], row_min=2, col_min=2):
            return False
        return True


class SingleValueInput(InputTypeBaseMixin):
    """Mixin class for single value input segments."""

    _input_type = IOType.SINGLE_VALUE

    def validate_input(self, *args, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(*args, **kwargs):
            return False
        if not self._validate_single_value(kwargs["input"]):
            return False
        return True


class MultiValueInput(InputTypeBaseMixin):
    """Mixin class for multiple values input segments."""

    _input_type = IOType.MULTIPLE_VALUES

    def validate_input(self, *args, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(*args, **kwargs):
            return False
        if not self._validate_multiple_values(kwargs["input"]):
            return False
        return True


class AnyInput(InputTypeBaseMixin):
    """Mixin class for any input segments."""

    _input_type = IOType.ANY

    def validate_input(self, *args, **kwargs) -> bool:
        """Validate the input."""
        if not self._ensure_input_exists(*args, **kwargs):
            return False
        if not self._validate_any(kwargs["input"]):
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

    def validate_input(self, *args, **kwargs) -> bool:  # noqa: ARG002
        """Validate the input."""
        if not self._validate_other(kwargs["input"]):
            return False
        return True
