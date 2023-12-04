"""util.py

Common utility functions.
"""

import typing as t
from uuid import uuid4


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
