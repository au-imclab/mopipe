<a id="mopipe.core.segments.seg"></a>

# mopipe.core.segments.seg

seg.py

Base segment class for all pipeline steps.

<a id="mopipe.core.segments.seg.Segment"></a>

## Segment Objects

```python
class Segment(metaclass=SegmentMeta)
```

Base class for all pipeline steps.

<a id="mopipe.core.segments.seg.Segment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, segment_id: t.Optional[str] = None) -> None
```

Initialize a Segment.

<a id="mopipe.core.segments.seg.Segment.name"></a>

#### name

```python
@property
def name() -> str
```

The name of the segment.

<a id="mopipe.core.segments.seg.Segment.segment_id"></a>

#### segment\_id

```python
@property
def segment_id() -> str
```

The id of the segment.

<a id="mopipe.core.segments.seg.Segment.validate_input"></a>

#### validate\_input

```python
@abstractmethod
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.seg.Segment.validate_output"></a>

#### validate\_output

```python
@abstractmethod
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.seg.Segment.process"></a>

#### process

```python
@abstractmethod
def process(x: t.Any, **kwargs) -> t.Any
```

Process the inputs and return the output.

<a id="mopipe.core.segments.seg.Segment.input_type"></a>

#### input\_type

```python
@property
@abstractmethod
def input_type() -> IOType
```

The type of the input.

<a id="mopipe.core.segments.seg.Segment.output_type"></a>

#### output\_type

```python
@property
@abstractmethod
def output_type() -> IOType
```

The type of the output.

<a id="mopipe.core.segments.seg.Segment.segment_type"></a>

#### segment\_type

```python
@property
@abstractmethod
def segment_type() -> SegmentType
```

The type of the segment.

<a id="mopipe.core.segments.seg.Segment.__call__"></a>

#### \_\_call\_\_

```python
def __call__(**kwargs) -> t.Any
```

Process the inputs and return the output.

