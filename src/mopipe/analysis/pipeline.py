"""pipeline.py

This module contains the Pipeline class, which is used to run a series of
analysis steps (segments) on the data.
"""

import typing as t

from mopipe.segments import Segment


class Pipeline(t.MutableSequence[Segment]):
    """Pipeline

    A pipeline is a series of segments that are run on the data.
    """

    _segments: t.MutableSequence[Segment]

    def __init__(self, segments: t.Optional[t.MutableSequence[Segment]] = None) -> None:
        """Initialize a Pipeline."""
        self._segments = [] if segments is None else segments

    @property
    def segments(self) -> t.MutableSequence[Segment]:
        """The segments in the pipeline."""
        return self._segments

    def _check_kwargs(self, **kwargs) -> None:
        """Check the arguments for the pipeline."""
        if "input" not in kwargs:
            msg = "No input provided to pipeline."
            raise ValueError(msg)

    def segment(self, index: int) -> Segment:
        """Get a segment from the pipeline."""
        return self._segments[index]

    def add_segment(self, segment: Segment) -> int:
        """Add a segment to the pipeline."""
        self._segments.append(segment)
        return len(self._segments) - 1

    def run(self, *args, **kwargs) -> t.Any:
        """Run the pipeline."""
        output = None
        self._check_kwargs(**kwargs)
        for segment in self._segments:
            # most basic version here
            # we could also keep track of the output from each step
            # if that is useful, for now it's just I -> Segment -> O -> Segment -> O -> ...
            kwargs["input"] = segment(*args, **kwargs)
        return output

    def __repr__(self) -> str:
        return f"Pipeline(segments={self._segments})"

    @t.overload
    def __getitem__(self, index: int) -> Segment:
        ...

    @t.overload
    def __getitem__(self, index: slice) -> t.MutableSequence[Segment]:
        ...

    def __getitem__(self, index: t.Union[int, slice]):
        return self._segments[index]

    def __len__(self) -> int:
        return len(self._segments)

    def __iter__(self) -> t.Iterator[Segment]:
        return iter(self._segments)

    def __reversed__(self) -> t.Iterator[Segment]:
        return reversed(self._segments)

    def __contains__(self, value: object) -> bool:
        return value in self._segments
