"""datastructs.py

This module contains the data structures used by the mopipe package.
"""

import sys

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

    It also adds the __getitem__ method, which allows getting the
    value of a member from its name, or if you already pass in a value,
    it will return the value.
    """

    def __contains__(cls, item: object) -> bool:
        if not isinstance(item, str):
            return super().__contains__(item)
        try:
            cls[item]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(cls, item: str) -> str:  # type: ignore
        if not isinstance(item, str):
            return str(super().__getitem__(item))
        if item in cls._member_map_:
            return str(cls._member_map_[item].value)
        if item in cls._value2member_map_:
            return item
        msg = f"{item} is not a valid member of {cls.__name__}"
        raise KeyError(msg)


class MocapMetadataEntries(StrEnum, metaclass=EnumContainsMeta):
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
