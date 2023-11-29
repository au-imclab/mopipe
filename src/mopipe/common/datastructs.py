"""datastructs.py

This module contains the data structures used by the mopipe package.
"""

import sys
import typing as t

# Python 3.11 has built-in StrEnum
if sys.version_info >= (3, 11):
    from enum import EnumMeta, IntEnum, StrEnum
else:
    from enum import EnumMeta, IntEnum

    from strenum import StrEnum


class DataLevel(IntEnum):
    """DataLevel

    Enum for the different levels of data that can be read by the
    mopipe package.
    """

    EXPERIMENT = 0
    TRIAL = 1
    SUBJECT = 2


class EnumContainsMeta(EnumMeta):
    """ExtendedStrEnum

    This is an extension of the StrEnum class from the enum module.
    It adds the __contains__ method, which allows checking if a
    string is a valid member of the enum.
    """

    def __contains__(self, item: object) -> bool:
        try:
            self(item)
        except ValueError:
            return False
        else:
            return True


class StrEnumExtended(StrEnum, metaclass=EnumContainsMeta):
    def __getitem__(self, item: t.SupportsIndex | slice) -> str:
        if not isinstance(item, str):
            return super().__getitem__(item)
        try:
            value = str(self.__class__(item).value)
            return value
        except ValueError as err:
            error_message = f"{item} is not a valid member of {self.__class__.__name__}"
            raise KeyError(error_message) from err


class MocapMetadataEntries(StrEnumExtended):
    """MocapMetadata

    Common metadata for all MoCap data, and their transformed names.
    This allows a common interface for all MoCap data.
    """

    cam_count = "n_cameras"
    frame_count = "n_frames"
    marker_names = "marker_names"
    marker_count = "n_markers"
    sample_rate = "sample_rate"
    time_stamp = "time_stamp"
