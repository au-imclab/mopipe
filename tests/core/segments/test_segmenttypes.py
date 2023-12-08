from mopipe.core.segments.segmenttypes import (
    AnalysisType,
    OtherType,
    PreprocessorType,
    SegmentType,
    SummaryType,
    TransformType,
    VisualizationType,
    WriteType,
)


class TestSegmentTypes:
    def test_preprocessor_type(self):
        preprocessor_type = PreprocessorType()
        assert preprocessor_type.segment_type == SegmentType.PREPROCESSOR

    def test_summary_type(self):
        summary_type = SummaryType()
        assert summary_type.segment_type == SegmentType.SUMMARY

    def test_transform_type(self):
        transform_type = TransformType()
        assert transform_type.segment_type == SegmentType.TRANSFORM

    def test_analysis_type(self):
        analysis_type = AnalysisType()
        assert analysis_type.segment_type == SegmentType.ANALYSIS

    def test_visualization_type(self):
        visualization_type = VisualizationType()
        assert visualization_type.segment_type == SegmentType.VISUALIZATION

    def test_write_type(self):
        write_type = WriteType()
        assert write_type.segment_type == SegmentType.WRITE

    def test_other_type(self):
        other_type = OtherType()
        assert other_type.segment_type == SegmentType.OTHER
