<a id="mopipe.core.analysis.pipeline"></a>

# mopipe.core.analysis.pipeline

pipeline.py

This module contains the Pipeline class, which is used to run a series of
analysis steps (segments) on the data.

<a id="mopipe.core.analysis.pipeline.Pipeline"></a>

## Pipeline Objects

```python
class Pipeline(t.MutableSequence[Segment])
```

Pipeline

A pipeline is a series of segments that are run on the data.

<a id="mopipe.core.analysis.pipeline.Pipeline.__init__"></a>

#### \_\_init\_\_

```python
def __init__(segments: t.Optional[t.MutableSequence[Segment]] = None,
             cache_dir: t.Optional[t.Union[str, Path]] = None) -> None
```

Initialize a Pipeline.

Parameters
----------
segments : MutableSequence[Segment], optional
    The segments to include in the pipeline.
cache_dir : str or Path, optional
    Directory for caching segment results using joblib.Memory.
    If None, caching is disabled.

<a id="mopipe.core.analysis.pipeline.Pipeline.segments"></a>

#### segments

```python
@property
def segments() -> t.MutableSequence[Segment]
```

The segments in the pipeline.

<a id="mopipe.core.analysis.pipeline.Pipeline.cache_dir"></a>

#### cache\_dir

```python
@property
def cache_dir() -> t.Optional[t.Union[str, Path]]
```

The cache directory.

<a id="mopipe.core.analysis.pipeline.Pipeline.segment"></a>

#### segment

```python
def segment(index: int) -> Segment
```

Get a segment from the pipeline.

<a id="mopipe.core.analysis.pipeline.Pipeline.add_segment"></a>

#### add\_segment

```python
def add_segment(segment: Segment) -> int
```

Add a segment to the pipeline.

<a id="mopipe.core.analysis.pipeline.Pipeline.clear_cache"></a>

#### clear\_cache

```python
def clear_cache() -> None
```

Clear the pipeline cache.

<a id="mopipe.core.analysis.pipeline.Pipeline.run"></a>

#### run

```python
def run(*, cache: bool = True, **kwargs) -> t.Any
```

Run the pipeline.

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

