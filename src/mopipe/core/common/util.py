"""util.py

Common utility functions.
"""

import typing as t
from uuid import uuid4

import pandas as pd


def maybe_generate_id(
    _id: t.Optional[str] = None, prefix: t.Optional[str] = None, suffix: t.Optional[str] = None
) -> str:
    """Generate a random id if not provided.

    This provides a fluid interface for generating unique ids for various classes.
    Sometimes, a user may want to provide their own id, and if so, this function
    will simply return the id they provided. If no id is provided, a random id
    will be generated.

    Parameters
    ----------
    _id : str, optional
        The id to use.
    prefix : str, optional
        The prefix to use for the id.
    suffix : str, optional
        The suffix to use for the id.

    Returns
    -------
    str
        The id.
    """
    if _id is not None:
        return _id
    prefix = "" if prefix is None else prefix + "_"
    suffix = "" if suffix is None else "_" + suffix
    return prefix + str(uuid4()) + suffix


def int_or_str_slice(s: slice) -> t.Union[type[int], type[str]]:
    start = s.start
    stop = s.stop
    if isinstance(start, int) and isinstance(stop, int):
        return int
    if isinstance(start, str) and isinstance(stop, str):
        return str
    msg = "Invalid slice."
    raise ValueError(msg)


def df_slice(df: pd.DataFrame, s: slice) -> t.Union[pd.DataFrame, pd.Series]:
    slice_type = int_or_str_slice(s)
    if slice_type is int:
        return df.iloc[s]
    if slice_type is str:
        return df.loc[s]
    msg = "Invalid slice."
    raise ValueError(msg)
