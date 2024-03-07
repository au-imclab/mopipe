import typing as t
from datetime import datetime
from enum import Enum


class TrajectoryType(Enum):
    """TrajectoryType

    Enum for the different types of trajectories that can be exported by
    QTM.
    """

    MEASURED = 0
    MIXED = 1

    @staticmethod
    def from_str(string: str) -> "TrajectoryType":
        """Convert string to TrajectoryType.

        Parameters
        ----------
        string : str
            String to convert to TrajectoryType.

        Returns
        -------
        TrajectoryType
            TrajectoryType corresponding to string.
        """
        string = string.lower()
        if string == "measured":
            return TrajectoryType.MEASURED
        elif string == "mixed":
            return TrajectoryType.MIXED
        else:
            err = f"Invalid trajectory type: {string}"
            raise ValueError(err)


def parse_time_stamp(time_stamp: list[str]) -> tuple[datetime, float]:
    """Parse the time stamp from a list of strings.

    Parameters
    ----------
    time_stamp : List[str]
        List of strings containing the time stamp.

    Returns
    -------
    Tuple[datetime, float]
        Tuple containing the time stamp and ?????.
    """
    ts = None
    if len(time_stamp) == 2:  # noqa: PLR2004
        ts = datetime.strptime(time_stamp[0], "%Y-%m-%d, %H:%M:%S.%f").astimezone()
        unk = float(time_stamp[1])
    else:
        try:
            ts = datetime.strptime(time_stamp[0], "%Y-%m-%d, %H:%M:%S.%f").astimezone()
        except ValueError:
            pass
        unk = 0.0
    if ts is None:
        err = f"Invalid time stamp: {time_stamp}"
        raise ValueError(err)
    return ts, unk


def parse_event(event: list[str]) -> list[tuple[str, int, float]]:
    """Parse the event data from a list of strings.

    Parameters
    ----------
    event : List[str]
        List of strings containing the event.

    Returns
    -------
    Tuple[str, float, float]
        Tuple containing the event name, index and elapsed time.
    """
    event_name = event[0]
    index = int(event[1])
    elapsed_time = float(event[2])
    return [(event_name, index, elapsed_time)]


def parse_marker_names(marker_names: list[str]) -> list[str]:
    """Parse the marker names from a list of strings.

    Parameters
    ----------
    marker_names : List[str]
        List of strings containing the marker names.

    Returns
    -------
    List[str]
        List containing the marker names.
    """
    return marker_names


def parse_trajectory_types(trajectory_types: list[str]) -> list[TrajectoryType]:
    """Parse the trajectory types from a list of strings.

    Parameters
    ----------
    trajectory_types : List[str]
        List of strings containing the trajectory types.

    Returns
    -------
    List[TrajectoryType]
        List containing the trajectory types.
    """
    return [TrajectoryType.from_str(t) for t in trajectory_types]


METADATA_MAP: dict[str, t.Any] = {
    "NO_OF_FRAMES": {"key": "n_frames", "type": int},
    "NO_OF_CAMERAS": {"key": "n_cameras", "type": int},
    "NO_OF_MARKERS": {"key": "n_markers", "type": int},
    "FREQUENCY": {"key": "sample_rate", "type": float},
    "NO_OF_ANALOG": {"key": "n_analog", "type": int},
    "ANALOG_FREQUENCY": {"key": "analog_sample_rate", "type": float},
    "DESCRIPTION": {"key": "description", "type": str},
    "EVENT": {"key": "event", "type_handler": parse_event},
    "DATA_INCLUDED": {
        "key": "data_included",
    },
    "TIME_STAMP": {"key": "time_stamp", "type_handler": parse_time_stamp},
    "MARKER_NAMES": {
        "key": "marker_names",
    },
    "TRAJECTORY_TYPES": {"key": "trajectory_types", "type_handler": parse_trajectory_types},
}


def parse_metadata_row(key: str, values: list[t.Any]) -> tuple[str, t.Any]:
    """Parse a metadata row and return the key and value.

    Parameters
    ----------
    key : str
        The key of the metadata row.
    values : List[Any]
        The values of the metadata row.

    Returns
    -------
    Tuple[str, Any]
        Tuple containing the key and value of the metadata row.
    """
    if key not in METADATA_MAP:
        return key, values
    metadata = METADATA_MAP[key]
    k = metadata["key"]

    if "type" in metadata:
        value = metadata["type"](values[0])
    elif "type_handler" in metadata:
        value = metadata["type_handler"](values)
    else:
        value = values
    return k, value
