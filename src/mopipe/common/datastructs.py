"""datastructs.py

This module contains the data structures used by the mopipe package.
"""

from dataclasses import dataclass
from enum import IntEnum, StrEnum
from pandas import DataFrame


class DataLevel(IntEnum):
    """DataLevel

    Enum for the different levels of data that can be read by the
    mopipe package.
    """

    EXPERIMENT = 0
    TRIAL = 1
    SUBJECT = 2


class MocapMetadata(StrEnum):
    """MocapMetadata

    Common metadata for all MoCap data, and their transformed names.
    This allows a common interface for all MoCap data.
    """

    cam_count = ("n_cameras",)
    frame_count = ("n_frames",)
    marker_names = ("marker_names",)
    marker_count = ("n_markers",)
    sample_rate = ("sample_rate",)
    time_stamp = ("time_stamp",)


class MocapTimeSeries:
    tsdata: DataFrame
    metadata: MocapMetadata
