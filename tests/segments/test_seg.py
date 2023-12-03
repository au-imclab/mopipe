from typing import Any

import pytest  # type: ignore

from mopipe.segments.inputs import AnyInput
from mopipe.segments.outputs import AnyOutput
from mopipe.segments.seg import Segment
from mopipe.segments.segmenttypes import OtherType


class AnyAnySegment(AnyInput, AnyOutput, OtherType, Segment):
    def process(self, *args, **kwargs) -> Any:  # noqa: ARG002
        return kwargs["input"]

    def validate_input(self, *args, **kwargs) -> bool:
        if "fail" in kwargs:
            return False
        return super().validate_input(*args, **kwargs)

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
        args = (1, 2, 3)
        kwargs = {"a": 1, "b": 2, "input": 3}
        assert segment._preprocess_input(*args, **kwargs) == (args, kwargs)

    def test_postprocess_output(self, segment: Segment) -> None:
        output = "output"
        assert segment._postprocess_output(output) == output

    def test_call_invalid_input(self, segment: Segment) -> None:
        with pytest.raises(ValueError):
            segment(1, 2, a=1, b=2, fail=True)

    def test_call_invalid_output(self, segment: Segment) -> None:
        with pytest.raises(ValueError):
            segment(1, 2, a=1, b=2, input="fail")

    def test_call_valid_input_and_output(self, segment: Segment) -> None:
        assert segment(1, 2, a=1, b=2, input="output") == "output"
