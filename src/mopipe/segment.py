import typing as t

import numpy as np
import pandas as pd

from mopipe.core.analysis import calc_rqa
from mopipe.core.common.util import int_or_str_slice
from mopipe.core.segments.inputs import AnySeriesInput, MultivariateSeriesInput, UnivariateSeriesInput
from mopipe.core.segments.outputs import MultivariateSeriesOutput, SingleNumericValueOutput, UnivariateSeriesOutput
from mopipe.core.segments.seg import Segment
from mopipe.core.segments.segmenttypes import AnalysisType, SummaryType, TransformType


class Mean(SummaryType, AnySeriesInput, SingleNumericValueOutput, Segment):
    def process(self, x: t.Union[pd.Series, pd.DataFrame], **kwargs) -> float:  # noqa: ARG002
        if x.empty:
            return np.nan
        mean = np.nanmean(x)
        return float(mean)


class ColMeans(SummaryType, MultivariateSeriesInput, UnivariateSeriesOutput, Segment):
    def process(
        self,
        x: pd.DataFrame,
        col: t.Union[str, int, slice, None] = None,
        **kwargs,  # noqa: ARG002
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


class CalcShift(TransformType, MultivariateSeriesInput, MultivariateSeriesOutput, Segment):
    def process(
        self,
        x: pd.DataFrame,
        cols: pd.Index | None = None,
        shift: int = 1,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        if cols is None:
            cols = x.columns
        for col_name in cols:
            col_data = x[col_name].values
            new_col_name = col_name + "_shift"
            new_col_data = np.concatenate((np.zeros(shift), col_data[shift:] - col_data[:-shift]))
            x[new_col_name] = new_col_data
        return x


class SimpleGapFilling(TransformType, MultivariateSeriesInput, MultivariateSeriesOutput, Segment):
    def process(
        self,
        x: pd.DataFrame,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        return x.interpolate(method="linear")


class RQAStats(AnalysisType, UnivariateSeriesInput, MultivariateSeriesOutput, Segment):
    def process(
        self,
        x: pd.Series,
        dim: int = 1,
        tau: int = 1,
        threshold: float = 0.1,
        lmin: int = 2,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        out = pd.DataFrame(
            columns=[
                "recurrence_rate",
                "determinism",
                "laminarity",
                "avg_diag_length",
                "avg_vert_length",
                "d_entropy",
                "v_entropy",
            ]
        )
        if x.empty:
            return out

        xv = x.values
        out.loc[len(out)] = calc_rqa(xv, xv, dim, tau, threshold, lmin)
        return out


class CrossRQAStats(AnalysisType, MultivariateSeriesInput, MultivariateSeriesOutput, Segment):
    def process(
        self,
        x: pd.DataFrame,
        col_a: t.Union[str, int] = 0,
        col_b: t.Union[str, int] = 0,
        dim: int = 1,
        tau: int = 1,
        threshold: float = 0.1,
        lmin: int = 2,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        out = pd.DataFrame(
            columns=[
                "recurrence_rate",
                "determinism",
                "laminarity",
                "avg_diag_length",
                "avg_vert_length",
                "d_entropy",
                "v_entropy",
            ]
        )
        if x.empty:
            return out
        if isinstance(col_a, int):
            xa = x.iloc[:, col_a].values
        if isinstance(col_a, str):
            xa = x.loc[:, col_a].values
        if isinstance(col_b, int):
            xb = x.iloc[:, col_b].values
        if isinstance(col_b, str):
            xb = x.loc[:, col_b].values

        out.loc[len(out)] = calc_rqa(xa, xb, dim, tau, threshold, lmin)
        return out


class WindowedCrossRQAStats(AnalysisType, MultivariateSeriesInput, MultivariateSeriesOutput, Segment):
    def process(
        self,
        x: pd.DataFrame,
        col_a: t.Union[str, int] = 0,
        col_b: t.Union[str, int] = 0,
        dim: int = 1,
        tau: int = 1,
        threshold: float = 0.1,
        lmin: int = 2,
        window: int = 100,
        step: int = 10,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        out = pd.DataFrame(
            columns=[
                "recurrence_rate",
                "determinism",
                "laminarity",
                "avg_diag_length",
                "avg_vert_length",
                "d_entropy",
                "v_entropy",
            ]
        )
        if x.empty:
            return out
        if isinstance(col_a, int):
            xa = x.iloc[:, col_a].values
        if isinstance(col_a, str):
            xa = x.loc[:, col_a].values
        if isinstance(col_b, int):
            xb = x.iloc[:, col_b].values
        if isinstance(col_b, str):
            xb = x.loc[:, col_b].values

        for w in range(0, xa.shape[0] - window + 1, step):
            out.loc[len(out)] = calc_rqa(xa[w : w + window], xb[w : w + window], dim, tau, threshold, lmin)
        return out
