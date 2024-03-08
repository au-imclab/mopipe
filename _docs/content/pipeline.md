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
def __init__(segments: t.Optional[t.MutableSequence[Segment]] = None) -> None
```

Initialize a Pipeline.

<a id="mopipe.core.analysis.pipeline.Pipeline.segments"></a>

#### segments

```python
@property
def segments() -> t.MutableSequence[Segment]
```

The segments in the pipeline.

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

<a id="mopipe.core.analysis.pipeline.Pipeline.run"></a>

#### run

```python
def run(**kwargs) -> t.Any
```

Run the pipeline.

