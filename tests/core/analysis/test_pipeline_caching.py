import shutil
import tempfile
from pathlib import Path

import pytest  # type: ignore

from mopipe.core.analysis import Pipeline


class MockSegment:
    """Mock segment that tracks call count."""

    def __init__(self):
        self.call_count = 0
        self.name = "mock"

    def __call__(self, **kwargs):
        self.call_count += 1
        return kwargs["x"] + 1


class TestPipelineCaching:
    @pytest.fixture
    def cache_dir(self):
        d = tempfile.mkdtemp()
        yield Path(d)
        shutil.rmtree(d, ignore_errors=True)

    def test_no_cache_by_default(self):
        pipeline = Pipeline([])
        assert pipeline.cache_dir is None

    def test_cache_dir_set(self, cache_dir):
        pipeline = Pipeline([], cache_dir=cache_dir)
        assert pipeline.cache_dir == cache_dir

    def test_backwards_compatible_init(self):
        seg = MockSegment()
        pipeline = Pipeline([seg])
        result = pipeline.run(x=1)
        assert result == 2

    def test_run_with_cache(self, cache_dir):
        seg = MockSegment()
        pipeline = Pipeline([seg], cache_dir=cache_dir)
        result = pipeline.run(x=1)
        assert result == 2

    def test_run_cache_false_bypasses_cache(self, cache_dir):
        seg = MockSegment()
        pipeline = Pipeline([seg], cache_dir=cache_dir)
        result = pipeline.run(x=1, cache=False)
        assert result == 2
        assert seg.call_count == 1

    def test_run_without_cache_dir_ignores_cache_param(self):
        seg = MockSegment()
        pipeline = Pipeline([seg])
        result = pipeline.run(x=1, cache=True)
        assert result == 2
        assert seg.call_count == 1

    def test_clear_cache(self, cache_dir):
        seg = MockSegment()
        pipeline = Pipeline([seg], cache_dir=cache_dir)
        pipeline.run(x=1)
        # Should not raise
        pipeline.clear_cache()

    def test_clear_cache_no_cache_dir(self):
        pipeline = Pipeline([])
        # Should not raise even without cache_dir
        pipeline.clear_cache()

    def test_multiple_segments_with_cache(self, cache_dir):
        seg1 = MockSegment()
        seg2 = MockSegment()
        pipeline = Pipeline([seg1, seg2], cache_dir=cache_dir)
        result = pipeline.run(x=1)
        assert result == 3
