from enum import Enum, auto


class IOType(Enum):
    """Type of segment inputs/outputs.

    This is used to determine whether a segment can be run on a given
    input, or if the output of a segment can be used as input to another.
    """

    UNIVARIATE_SERIES = auto()
    MULTIVARIATE_SERIES = auto()
    SINGLE_VALUE = auto()
    MULTIPLE_VALUES = auto()
    ANY = auto()
    OTHER = auto()
