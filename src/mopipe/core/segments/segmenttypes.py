from enum import Enum, auto


class SegmentType(Enum):
    """Type of segment."""

    PREPROCESSOR = auto()
    SUMMARY = auto()
    TRANSFORM = auto()
    ANALYSIS = auto()
    VISUALIZATION = auto()
    WRITE = auto()
    OTHER = auto()


class SegmentTypeMixin:
    """Mixin class for all segments types."""

    _segment_type: SegmentType

    @property
    def segment_type(self) -> SegmentType:
        """The type of the segment."""
        return self._segment_type


class PreprocessorType(SegmentTypeMixin):
    """Mixin class for preprocessing segments."""

    _segment_type = SegmentType.PREPROCESSOR


class SummaryType(SegmentTypeMixin):
    """Mixin class for summary segments."""

    _segment_type = SegmentType.SUMMARY


class TransformType(SegmentTypeMixin):
    """Mixin class for transform segments."""

    _segment_type = SegmentType.TRANSFORM


class AnalysisType(SegmentTypeMixin):
    """Mixin class for analysis segments."""

    _segment_type = SegmentType.ANALYSIS


class VisualizationType(SegmentTypeMixin):
    """Mixin class for visualization segments."""

    _segment_type = SegmentType.VISUALIZATION


class WriteType(SegmentTypeMixin):
    """Mixin class for write segments."""

    _segment_type = SegmentType.WRITE


class OtherType(SegmentTypeMixin):
    """Mixin class for other segments."""

    _segment_type = SegmentType.OTHER
