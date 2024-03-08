from mopipe.core.analysis import Pipeline


class TestPipeline:
    def test_run_with_no_segments(self):
        pipeline = Pipeline([])
        output = pipeline.run(x=None)
        assert output is None

    def test_run_with_single_segment(self):
        segment = MockSegment()
        pipeline = Pipeline([segment])
        output = pipeline.run(x=1)
        assert output == segment.process_output

    def test_run_with_multiple_segments(self):
        segment1 = MockSegment()
        segment2 = MockSegment()
        pipeline = Pipeline([segment1, segment2])
        output = pipeline.run(x=1)
        assert output == segment2.process_output


class MockSegment:
    def __init__(self):
        self.process_output = None

    def __call__(self, **kwargs):
        self.process_output = kwargs["x"] + 1
        return self.process_output
