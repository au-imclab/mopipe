import math
import typing as t
from enum import Enum, auto

import pandas as pd


class IOType(Enum):
    """Type of segment inputs/outputs.

    This is used to determine whether a segment can be run on a given
    input, or if the output of a segment can be used as input to another.
    """

    UNIVARIATE_SERIES = auto()
    MULTIVARIATE_SERIES = auto()
    SINGLE_VALUE = auto()
    MULTIPLE_VALUES = auto()
    ANY = auto()
    OTHER = auto()


class IOTypeBaseMixin:
    """Mixin class for all segments input/output types."""

    def _validate_series(self, x: t.Any) -> bool:
        """Validate that the input is a pandas Series."""
        if isinstance(x, pd.Series):
            return True
        return False

    def _validate_dataframe(self, x: t.Any) -> bool:
        """Validate that the input is a pandas DataFrame."""
        if isinstance(x, pd.DataFrame):
            return True
        return False

    def _validate_series_or_dataframe(self, x: t.Any) -> bool:
        """Validate that the input is a pandas Series or DataFrame."""
        if self._validate_series(x) or self._validate_dataframe(x):
            return True
        return False

    def _validate_single_value(self, x: t.Any) -> bool:
        """Validate that the input is a single value."""
        if isinstance(x, (int, float, str)):
            return True
        return False

    def _validate_multiple_values(self, x: t.Any) -> bool:
        """Validate that the input is a list of values."""
        if isinstance(x, t.Sequence):
            if len(x) > 1:
                return True
        return False

    def _validate_any(self, x: t.Any) -> bool:  # noqa: ARG002
        """Validate that the input is anything."""
        return True

    def _validate_shape(
        self,
        x: t.Union[pd.Series, pd.DataFrame],
        row_min: int = 1,
        col_min: int = 1,
        row_max: t.Optional[t.Union[int, float]] = None,
        col_max: t.Optional[t.Union[int, float]] = None,
    ) -> bool:
        """Validate that the input has the correct shape."""
        if row_max is None:
            row_max = math.inf
        if col_max is None:
            col_max = math.inf
        if row_min <= x.shape[0] <= row_max:
            if col_max == 1 and x.ndim == 1:
                return True
            if x.ndim == 1:
                return False
            if col_min <= x.shape[1] <= col_max:
                return True
        return False
