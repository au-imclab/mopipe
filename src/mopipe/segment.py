import typing as t

import numpy as np
import pandas as pd

from mopipe.core.common.util import int_or_str_slice
from mopipe.core.segments.inputs import AnySeriesInput, MultivariateSeriesInput
from mopipe.core.segments.outputs import SingleNumericValueOutput, UnivariateSeriesOutput
from mopipe.core.segments.seg import Segment
from mopipe.core.segments.segmenttypes import SummaryType


class Mean(SummaryType, AnySeriesInput, SingleNumericValueOutput, Segment):
    def process(self, x: t.Union[pd.Series, pd.DataFrame], **kwargs) -> float:  # noqa: ARG002
        if x.empty:
            return np.nan
        mean = np.nanmean(x)
        return float(mean)


class ColMeans(SummaryType, MultivariateSeriesInput, UnivariateSeriesOutput, Segment):
    def process(
        self, x: pd.DataFrame, col: t.Union[str, int, slice, None] = None, **kwargs  # noqa: ARG002
    ) -> pd.Series:
        slice_type = None
        if x.empty:
            return pd.Series()
        if isinstance(col, slice):
            slice_type = int_or_str_slice(col)
        if isinstance(col, int) or slice_type == int:
            return x.iloc(axis=1)[col].mean()
        if isinstance(col, str) or slice_type == str:
            return x.loc(axis=1)[col].mean()
        if col is None:
            return x.select_dtypes(include="number").mean()
        msg = f"Invalid col type {type(col)} provided, Must be None, int, str, or a slice."
        raise ValueError(msg)
