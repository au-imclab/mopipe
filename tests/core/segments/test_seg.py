from typing import Any

import pytest  # type: ignore

from mopipe.core.segments.inputs import AnyInput
from mopipe.core.segments.outputs import AnyOutput
from mopipe.core.segments.seg import Segment
from mopipe.core.segments.segmenttypes import OtherType


class AnyAnySegment(AnyInput, AnyOutput, OtherType, Segment):
    def process(self, x=Any, **kwargs) -> Any:  # noqa: ARG002
        return x

    def validate_input(self, **kwargs) -> bool:
        if "fail" in kwargs:
            return False
        return super().validate_input(**kwargs)

    def validate_output(self, output: Any) -> bool:
        if output == "fail":
            return False
        return super().validate_output(output)


class TestSegment:
    @pytest.fixture
    def segment(self) -> Segment:
        return AnyAnySegment("TestSegment")

    def test_name(self, segment: Segment) -> None:
        assert segment.name == "TestSegment"

    def test_segment_id(self, segment: Segment) -> None:
        assert isinstance(segment.segment_id, str)

    def test_preprocess_input(self, segment: Segment) -> None:
        kwargs = {"a": 1, "b": 2, "x": 3}
        assert segment._preprocess_input(**kwargs) == kwargs

    def test_postprocess_output(self, segment: Segment) -> None:
        output = "output"
        assert segment._postprocess_output(output) == output

    def test_call_invalid_input(self, segment: Segment) -> None:
        with pytest.raises(ValueError):
            segment(a=1, b=2, fail=True)

    def test_call_invalid_output(self, segment: Segment) -> None:
        with pytest.raises(ValueError):
            segment(a=1, b=2, x="fail")

    def test_call_valid_input_and_output(self, segment: Segment) -> None:
        assert segment(a=1, b=2, x="output") == "output"
