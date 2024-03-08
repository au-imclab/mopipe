<a id="mopipe.core.segments.segmenttypes"></a>

# mopipe.core.segments.segmenttypes

<a id="mopipe.core.segments.segmenttypes.SegmentType"></a>

## SegmentType Objects

```python
class SegmentType(Enum)
```

Type of segment.

<a id="mopipe.core.segments.segmenttypes.SegmentTypeMixin"></a>

## SegmentTypeMixin Objects

```python
class SegmentTypeMixin()
```

Mixin class for all segments types.

<a id="mopipe.core.segments.segmenttypes.SegmentTypeMixin.segment_type"></a>

#### segment\_type

```python
@property
def segment_type() -> SegmentType
```

The type of the segment.

<a id="mopipe.core.segments.segmenttypes.PreprocessorType"></a>

## PreprocessorType Objects

```python
class PreprocessorType(SegmentTypeMixin)
```

Mixin class for preprocessing segments.

<a id="mopipe.core.segments.segmenttypes.SummaryType"></a>

## SummaryType Objects

```python
class SummaryType(SegmentTypeMixin)
```

Mixin class for summary segments.

<a id="mopipe.core.segments.segmenttypes.TransformType"></a>

## TransformType Objects

```python
class TransformType(SegmentTypeMixin)
```

Mixin class for transform segments.

<a id="mopipe.core.segments.segmenttypes.AnalysisType"></a>

## AnalysisType Objects

```python
class AnalysisType(SegmentTypeMixin)
```

Mixin class for analysis segments.

<a id="mopipe.core.segments.segmenttypes.VisualizationType"></a>

## VisualizationType Objects

```python
class VisualizationType(SegmentTypeMixin)
```

Mixin class for visualization segments.

<a id="mopipe.core.segments.segmenttypes.WriteType"></a>

## WriteType Objects

```python
class WriteType(SegmentTypeMixin)
```

Mixin class for write segments.

<a id="mopipe.core.segments.segmenttypes.OtherType"></a>

## OtherType Objects

```python
class OtherType(SegmentTypeMixin)
```

Mixin class for other segments.

