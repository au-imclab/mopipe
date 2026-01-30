import typing as t

import numpy as np
import pandas as pd

from mopipe.core.analysis import calc_rqa
from mopipe.core.common.util import int_or_str_slice
from mopipe.core.segments.inputs import AnySeriesInput, MultivariateSeriesInput, UnivariateSeriesInput
from mopipe.core.segments.outputs import (
    AnySeriesOutput,
    MultivariateSeriesOutput,
    SingleNumericValueOutput,
    UnivariateSeriesOutput,
)
from mopipe.core.segments.seg import Segment
from mopipe.core.segments.segmenttypes import AnalysisType, SummaryType, TransformType


class Mean(SummaryType, AnySeriesInput, SingleNumericValueOutput, Segment):
    """Calculate the mean of the input series."""

    def process(self, x: t.Union[pd.Series, pd.DataFrame], **kwargs) -> float:  # noqa: ARG002
        """Process the input series and return the mean value.

        Args:
            x (pd.Series | pd.DataFrame): The input series.

        Returns:
            float: The mean value.
        """
        if x.empty:
            return np.nan
        mean = np.nanmean(x)
        return float(mean)


class ColMeans(SummaryType, MultivariateSeriesInput, UnivariateSeriesOutput, Segment):
    """Calculate the mean of each column in the input dataframe."""

    def process(
        self,
        x: pd.DataFrame,
        col: t.Union[str, int, slice, None] = None,
        **kwargs,  # noqa: ARG002
    ) -> pd.Series:
        """Process the input dataframe and return the mean value of each column.

        Args:
            x (pd.DataFrame): The input dataframe.
            col (str | int | slice | None, optional): The column to calculate the mean for. Defaults to None.

        Returns:
            pd.Series: The mean value of each column.
        """
        slice_type = None
        if x.empty:
            return pd.Series(dtype=float)
        if isinstance(col, slice):
            slice_type = int_or_str_slice(col)
            if slice_type is int:
                return pd.Series(x.iloc(axis=1)[col].mean(), dtype=float)
            elif slice_type is str:
                return pd.Series(x.loc(axis=1)[col].mean(), dtype=float)
        if isinstance(col, int):
            return pd.Series(x.iloc(axis=1)[col].mean(), dtype=float)
        if isinstance(col, str):
            return pd.Series(x.loc(axis=1)[col].mean(), dtype=float)
        if col is None:
            return x.select_dtypes(include="number").mean()
        msg = f"Invalid col type {type(col)} provided, Must be None, int, str, or a slice."
        raise ValueError(msg)


class CalcShift(TransformType, MultivariateSeriesInput, MultivariateSeriesOutput, Segment):
    """Calculate the difference between the input series and a shifted version of itself."""

    def process(
        self,
        x: pd.DataFrame,
        cols: pd.Index | t.Iterable[str] | None = None,
        shift: int = 1,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        """Process the input dataframe and return the difference between the input series and a shifted version of
        itself.

        Args:
            x (pd.DataFrame): The input dataframe.
            cols (pd.Index | None, optional): The columns to calculate the difference for. Defaults to None.
            shift (int, optional): The number of periods to shift. Defaults to 1.

        Returns:
            pd.DataFrame: The difference between the input series and a shifted version of itself.
        """
        if cols is None:
            cols = x.columns
        for col_name in cols:
            col_data = x[col_name].values
            # ensure column data is numeric
            if col_data is None or not isinstance(col_data, np.ndarray):
                msg = f"Column {col_name} data is not a numpy array."
                raise ValueError(msg)
            if not np.issubdtype(col_data.dtype, np.number):
                msg = f"Column {col_name} is not numeric."
                raise ValueError(msg)
            new_col_name = col_name + "_shift"
            new_col_data = np.concatenate((np.zeros(shift), col_data[shift:] - col_data[:-shift]))
            x[new_col_name] = new_col_data
        return x


class SimpleGapFilling(TransformType, MultivariateSeriesInput, MultivariateSeriesOutput, Segment):
    """Fill gaps in the input series with the linear interpolation."""

    def process(
        self,
        x: pd.DataFrame,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        """Process the input dataframe and fill gaps in the input series with the linear interpolation.

        Args:
            x (pd.DataFrame): The input dataframe.

        Returns:
            pd.DataFrame: The input dataframe with gaps filled using linear interpolation.
        """
        return x.interpolate(method="linear")


class RQAStats(AnalysisType, UnivariateSeriesInput, AnySeriesOutput, Segment):
    """Calculate Recurrence Quantification Analysis (RQA) statistics for the input series."""

    def process(
        self,
        x: pd.Series,
        dim: int = 1,
        tau: int = 1,
        threshold: float = 0.1,
        lmin: int = 2,
        **kwargs,  # noqa: ARG002
    ) -> pd.DataFrame:
        """Process the input series and return the RQA statistics.

        Args:
            x (pd.Series): The input series.
            dim (int, optional): The embedding dimension. Defaults to 1.
            tau (int, optional): The time delay. Defaults to 1.
            threshold (float, optional): The recurrence threshold. Defaults to 0.1.
            lmin (int, optional): The minimum line length. Defaults to 2.

        Returns:
            pd.DataFrame: The RQA statistics.
        """
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


class CrossRQAStats(AnalysisType, MultivariateSeriesInput, AnySeriesOutput, Segment):
    """Calculate Recurrence Quantification Analysis (RQA) statistics between two input series."""

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
        """Process the input dataframe and return the RQA statistics between two input series.

        Args:
            x (pd.DataFrame): The input dataframe.
            col_a (str | int): The first column to calculate the RQA statistics for.
            col_b (str | int): The second column to calculate the RQA statistics for.
            dim (int, optional): The embedding dimension. Defaults to 1.
            tau (int, optional): The time delay. Defaults to 1.
            threshold (float, optional): The recurrence threshold. Defaults to 0.1.
            lmin (int, optional): The minimum line length. Defaults to 2.

        Returns:
            pd.DataFrame: The RQA statistics.
        """
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


class WindowedCrossRQAStats(AnalysisType, MultivariateSeriesInput, AnySeriesOutput, Segment):
    """Calculate Recurrence Quantification Analysis (RQA) statistics between two input series in a moving window."""

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
        """Process the input dataframe and return the RQA statistics between two input series in a moving window.

        Args:
            x (pd.DataFrame): The input dataframe.
            col_a (str | int): The first column to calculate the RQA statistics for.
            col_b (str | int): The second column to calculate the RQA statistics for.
            dim (int, optional): The embedding dimension. Defaults to 1.
            tau (int, optional): The time delay. Defaults to 1.
            threshold (float, optional): The recurrence threshold. Defaults to 0.1.
            lmin (int, optional): The minimum line length. Defaults to 2.
            window (int, optional): The window size. Defaults to 100.
            step (int, optional): The step size. Defaults to 10.

        Returns:
            pd.DataFrame: The RQA statistics.
        """
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
