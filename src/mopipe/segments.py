import typing as t

import pandas as pd

from mopipe.core.segments import (
    Segment,
    inputs,
    outputs,
    segmenttypes,
)


class Mean(segmenttypes.SummaryType, outputs.SingleValueOutput):
    """Mean

    Calculate the mean of the input.
    """



class SeriesMean(inputs.UnivariateSeriesInput, Mean, Segment):
    """SeriesMean

    Calculate the mean of a univariate series input.
    """

    def process(self, *args, **kwargs) -> pd.Series:
        """Process the inputs and return the output."""
        return kwargs["input"].mean()