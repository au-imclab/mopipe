from enum import Enum, auto


class SegmentType(Enum):
    """Type of segment."""

    PREPROCESSING = auto()
    SUMMARY = auto()
    TRANSFORM = auto()
    ANALYSIS = auto()
    VISUALIZATION = auto()
    WRITE = auto()


class SegmentTypeMixin:
    """Mixin class for all segments types."""

    _segment_type: SegmentType

    @property
    def segment_type(self) -> SegmentType:
        """The type of the segment."""
        return self._segment_type


class PreprocessingMixin(SegmentTypeMixin):
    """Mixin class for preprocessing segments."""

    _segment_type = SegmentType.PREPROCESSING


class SummaryMixin(SegmentTypeMixin):
    """Mixin class for summary segments."""

    _segment_type = SegmentType.SUMMARY


class TransformMixin(SegmentTypeMixin):
    """Mixin class for transform segments."""

    _segment_type = SegmentType.TRANSFORM


class AnalysisMixin(SegmentTypeMixin):
    """Mixin class for analysis segments."""

    _segment_type = SegmentType.ANALYSIS


class VisualizationMixin(SegmentTypeMixin):
    """Mixin class for visualization segments."""

    _segment_type = SegmentType.VISUALIZATION


class WriteMixin(SegmentTypeMixin):
    """Mixin class for write segments."""

    _segment_type = SegmentType.WRITE
