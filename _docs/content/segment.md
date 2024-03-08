<a id="mopipe.segment"></a>

# mopipe.segment

<a id="mopipe.segment.Mean"></a>

## Mean Objects

```python
class Mean(SummaryType, AnySeriesInput, SingleNumericValueOutput, Segment)
```

Calculate the mean of the input series.

<a id="mopipe.segment.Mean.process"></a>

#### process

```python
def process(x: t.Union[pd.Series, pd.DataFrame], **kwargs) -> float
```

Process the input series and return the mean value.

**Arguments**:

- `x` _pd.Series | pd.DataFrame_ - The input series.
  

**Returns**:

- `float` - The mean value.

<a id="mopipe.segment.ColMeans"></a>

## ColMeans Objects

```python
class ColMeans(SummaryType, MultivariateSeriesInput, UnivariateSeriesOutput,
               Segment)
```

Calculate the mean of each column in the input dataframe.

<a id="mopipe.segment.ColMeans.process"></a>

#### process

```python
def process(x: pd.DataFrame,
            col: t.Union[str, int, slice, None] = None,
            **kwargs) -> pd.Series
```

Process the input dataframe and return the mean value of each column.

**Arguments**:

- `x` _pd.DataFrame_ - The input dataframe.
- `col` _str | int | slice | None, optional_ - The column to calculate the mean for. Defaults to None.
  

**Returns**:

- `pd.Series` - The mean value of each column.

<a id="mopipe.segment.CalcShift"></a>

## CalcShift Objects

```python
class CalcShift(TransformType, MultivariateSeriesInput,
                MultivariateSeriesOutput, Segment)
```

Calculate the difference between the input series and a shifted version of itself.

<a id="mopipe.segment.CalcShift.process"></a>

#### process

```python
def process(x: pd.DataFrame,
            cols: pd.Index | None = None,
            shift: int = 1,
            **kwargs) -> pd.DataFrame
```

Process the input dataframe and return the difference between the input series and a shifted version of
itself.

**Arguments**:

- `x` _pd.DataFrame_ - The input dataframe.
- `cols` _pd.Index | None, optional_ - The columns to calculate the difference for. Defaults to None.
- `shift` _int, optional_ - The number of periods to shift. Defaults to 1.
  

**Returns**:

- `pd.DataFrame` - The difference between the input series and a shifted version of itself.

<a id="mopipe.segment.SimpleGapFilling"></a>

## SimpleGapFilling Objects

```python
class SimpleGapFilling(TransformType, MultivariateSeriesInput,
                       MultivariateSeriesOutput, Segment)
```

Fill gaps in the input series with the linear interpolation.

<a id="mopipe.segment.SimpleGapFilling.process"></a>

#### process

```python
def process(x: pd.DataFrame, **kwargs) -> pd.DataFrame
```

Process the input dataframe and fill gaps in the input series with the linear interpolation.

**Arguments**:

- `x` _pd.DataFrame_ - The input dataframe.
  

**Returns**:

- `pd.DataFrame` - The input dataframe with gaps filled using linear interpolation.

<a id="mopipe.segment.RQAStats"></a>

## RQAStats Objects

```python
class RQAStats(AnalysisType, UnivariateSeriesInput, MultivariateSeriesOutput,
               Segment)
```

Calculate Recurrence Quantification Analysis (RQA) statistics for the input series.

<a id="mopipe.segment.RQAStats.process"></a>

#### process

```python
def process(x: pd.Series,
            dim: int = 1,
            tau: int = 1,
            threshold: float = 0.1,
            lmin: int = 2,
            **kwargs) -> pd.DataFrame
```

Process the input series and return the RQA statistics.

**Arguments**:

- `x` _pd.Series_ - The input series.
- `dim` _int, optional_ - The embedding dimension. Defaults to 1.
- `tau` _int, optional_ - The time delay. Defaults to 1.
- `threshold` _float, optional_ - The recurrence threshold. Defaults to 0.1.
- `lmin` _int, optional_ - The minimum line length. Defaults to 2.
  

**Returns**:

- `pd.DataFrame` - The RQA statistics.

<a id="mopipe.segment.CrossRQAStats"></a>

## CrossRQAStats Objects

```python
class CrossRQAStats(AnalysisType, MultivariateSeriesInput,
                    MultivariateSeriesOutput, Segment)
```

Calculate Recurrence Quantification Analysis (RQA) statistics between two input series.

<a id="mopipe.segment.CrossRQAStats.process"></a>

#### process

```python
def process(x: pd.DataFrame,
            col_a: t.Union[str, int] = 0,
            col_b: t.Union[str, int] = 0,
            dim: int = 1,
            tau: int = 1,
            threshold: float = 0.1,
            lmin: int = 2,
            **kwargs) -> pd.DataFrame
```

Process the input dataframe and return the RQA statistics between two input series.

**Arguments**:

- `x` _pd.DataFrame_ - The input dataframe.
- `col_a` _str | int_ - The first column to calculate the RQA statistics for.
- `col_b` _str | int_ - The second column to calculate the RQA statistics for.
- `dim` _int, optional_ - The embedding dimension. Defaults to 1.
- `tau` _int, optional_ - The time delay. Defaults to 1.
- `threshold` _float, optional_ - The recurrence threshold. Defaults to 0.1.
- `lmin` _int, optional_ - The minimum line length. Defaults to 2.
  

**Returns**:

- `pd.DataFrame` - The RQA statistics.

<a id="mopipe.segment.WindowedCrossRQAStats"></a>

## WindowedCrossRQAStats Objects

```python
class WindowedCrossRQAStats(AnalysisType, MultivariateSeriesInput,
                            MultivariateSeriesOutput, Segment)
```

Calculate Recurrence Quantification Analysis (RQA) statistics between two input series in a moving window.

<a id="mopipe.segment.WindowedCrossRQAStats.process"></a>

#### process

```python
def process(x: pd.DataFrame,
            col_a: t.Union[str, int] = 0,
            col_b: t.Union[str, int] = 0,
            dim: int = 1,
            tau: int = 1,
            threshold: float = 0.1,
            lmin: int = 2,
            window: int = 100,
            step: int = 10,
            **kwargs) -> pd.DataFrame
```

Process the input dataframe and return the RQA statistics between two input series in a moving window.

**Arguments**:

- `x` _pd.DataFrame_ - The input dataframe.
- `col_a` _str | int_ - The first column to calculate the RQA statistics for.
- `col_b` _str | int_ - The second column to calculate the RQA statistics for.
- `dim` _int, optional_ - The embedding dimension. Defaults to 1.
- `tau` _int, optional_ - The time delay. Defaults to 1.
- `threshold` _float, optional_ - The recurrence threshold. Defaults to 0.1.
- `lmin` _int, optional_ - The minimum line length. Defaults to 2.
- `window` _int, optional_ - The window size. Defaults to 100.
- `step` _int, optional_ - The step size. Defaults to 10.
  

**Returns**:

- `pd.DataFrame` - The RQA statistics.

