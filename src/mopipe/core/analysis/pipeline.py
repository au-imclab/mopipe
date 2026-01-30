"""pipeline.py

This module contains the Pipeline class, which is used to run a series of
analysis steps (segments) on the data.
"""

import typing as t
from pathlib import Path

from joblib import Memory

from mopipe.core.segments import Segment


def _execute_segment(segment: Segment, **kwargs) -> t.Any:
    """Execute a segment. Top-level function for joblib caching compatibility."""
    return segment(**kwargs)


class Pipeline(t.MutableSequence[Segment]):
    """Pipeline

    A pipeline is a series of segments that are run on the data.
    """

    _segments: t.MutableSequence[Segment]

    def __init__(
        self,
        segments: t.Optional[t.MutableSequence[Segment]] = None,
        cache_dir: t.Optional[t.Union[str, Path]] = None,
    ) -> None:
        """Initialize a Pipeline.

        Parameters
        ----------
        segments : MutableSequence[Segment], optional
            The segments to include in the pipeline.
        cache_dir : str or Path, optional
            Directory for caching segment results using joblib.Memory.
            If None, caching is disabled.
        """
        self._segments = [] if segments is None else segments
        self._cache_dir = cache_dir
        self._memory: t.Optional[Memory] = None
        if cache_dir is not None:
            self._memory = Memory(str(cache_dir), verbose=0)

    @property
    def segments(self) -> t.MutableSequence[Segment]:
        """The segments in the pipeline."""
        return self._segments

    @property
    def cache_dir(self) -> t.Optional[t.Union[str, Path]]:
        """The cache directory."""
        return self._cache_dir

    def _check_kwargs(self, **kwargs) -> None:
        """Check the arguments for the pipeline."""
        if "x" not in kwargs:
            msg = "No input provided to pipeline."
            raise ValueError(msg)

    def segment(self, index: int) -> Segment:
        """Get a segment from the pipeline."""
        return self._segments[index]

    def add_segment(self, segment: Segment) -> int:
        """Add a segment to the pipeline."""
        self._segments.append(segment)
        return len(self._segments) - 1

    def clear_cache(self) -> None:
        """Clear the pipeline cache."""
        if self._memory is not None:
            self._memory.clear(warn=False)

    def run(self, *, cache: bool = True, **kwargs) -> t.Any:
        """Run the pipeline.

        Parameters
        ----------
        cache : bool, optional
            Whether to use caching (if cache_dir was set). Defaults to True.
        **kwargs
            Arguments passed to the segments. Must include 'x' as the input data.

        Returns
        -------
        Any
            The output of the last segment in the pipeline.
        """
        self._check_kwargs(**kwargs)
        use_cache = cache and self._memory is not None
        for segment in self._segments:
            if use_cache:
                cached_fn = self._memory.cache(_execute_segment)  # type: ignore[union-attr]
                kwargs["x"] = cached_fn(segment, **kwargs)
            else:
                kwargs["x"] = segment(**kwargs)
        return kwargs["x"]

    def __repr__(self) -> str:
        return f"Pipeline(segments={self._segments})"

    @t.overload
    def __getitem__(self, index: int) -> Segment: ...

    @t.overload
    def __getitem__(self, index: slice) -> t.MutableSequence[Segment]: ...

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

    @t.overload
    def __setitem__(self, index: int, value: Segment) -> None: ...

    @t.overload
    def __setitem__(self, index: slice, value: t.Iterable[Segment]) -> None: ...

    def __setitem__(self, index: t.Union[int, slice], value: t.Union[Segment, t.Iterable[Segment]]) -> None:
        if isinstance(index, int):
            if not isinstance(value, Segment):
                msg = "Single value must be a Segment."
                raise ValueError(msg)
            self._segments[index] = value
        else:
            if not isinstance(value, t.Iterable):
                msg = "Value must be an iterable of Segments."
                raise ValueError(msg)
            if not all(isinstance(v, Segment) for v in value):
                msg = "All values must be Segments."
                raise ValueError(msg)
            self._segments[index] = list(value)

    @t.overload
    def __delitem__(self, index: int) -> None: ...

    @t.overload
    def __delitem__(self, index: slice) -> None: ...

    def __delitem__(self, index: t.Union[int, slice]) -> None:
        del self._segments[index]

    def insert(self, index: int, value: Segment) -> None:
        self._segments.insert(index, value)
