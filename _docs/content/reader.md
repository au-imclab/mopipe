<a id="mopipe.core.data.reader"></a>

# mopipe.core.data.reader

reader.py

This module contains the default Reader classes, including the
AbstractReader base class which can be used for creating new
readers.

<a id="mopipe.core.data.reader.AbstractReader"></a>

## AbstractReader Objects

```python
class AbstractReader(ABC)
```

AbstractReader

Abstract base class for all Readers. Readers are used to read
data from a source and return it in a pandas dataframe.

<a id="mopipe.core.data.reader.AbstractReader.__init__"></a>

#### \_\_init\_\_

```python
@abstractmethod
def __init__(source: t.Union[str, Path, pd.DataFrame],
             name: str,
             data_id: t.Optional[str] = None,
             sample_rate: t.Optional[float] = None,
             **kwargs)
```

Initialize the AbstractReader.

Parameters
----------
source : Path or DataFrame
    The source of the data to be read.
name : str
    The name of the data/experiment to be read.
data_id : str, optional
    The id of the data to be read.
    If not provided, a random id will be generated.
sample_rate : float, optional
    The sample rate of the data to be read.

<a id="mopipe.core.data.reader.AbstractReader.source"></a>

#### source

```python
@property
def source() -> t.Union[Path, pd.DataFrame]
```

The source of the data to be read.

<a id="mopipe.core.data.reader.AbstractReader.sample_rate"></a>

#### sample\_rate

```python
@property
def sample_rate() -> t.Optional[float]
```

The sample rate of the data to be read.

<a id="mopipe.core.data.reader.AbstractReader.allowed_extensions"></a>

#### allowed\_extensions

```python
@property
def allowed_extensions() -> list[str]
```

The allowed extensions for the source.

<a id="mopipe.core.data.reader.AbstractReader.metadata"></a>

#### metadata

```python
@property
def metadata() -> MetaData
```

The metadata for the data to be read.

<a id="mopipe.core.data.reader.AbstractReader.name"></a>

#### name

```python
@property
def name() -> str
```

The name of the data/experiment to be read.

<a id="mopipe.core.data.reader.AbstractReader.data_id"></a>

#### data\_id

```python
@property
def data_id() -> str
```

The id of the data/experiment to be read.

<a id="mopipe.core.data.reader.AbstractReader.read"></a>

#### read

```python
@abstractmethod
def read() -> t.Optional[EmpiricalData]
```

Read the data from the source and return it as a dataframe.

<a id="mopipe.core.data.reader.MocapReader"></a>

## MocapReader Objects

```python
class MocapReader(AbstractReader)
```

MocapReader

The MocapReader class is used to read motion capture data from
a source and return it as a pandas dataframe.

<a id="mopipe.core.data.reader.MocapReader.__init__"></a>

#### \_\_init\_\_

```python
def __init__(source: t.Union[Path, pd.DataFrame],
             name: str,
             data_id: t.Optional[str] = None,
             sample_rate: t.Optional[float] = None,
             **kwargs)
```

Initialize the MocapReader.

Parameters
----------
source : Path or DataFrame
    The source of the data to be read.
name : str
    The name of the data/experiment to be read.
sample_rate : float, optional
    The sample rate of the data to be read.
level : DataLevel, optional
    The level of the data to be read.

<a id="mopipe.core.data.reader.MocapReader.metadata"></a>

#### metadata

```python
@property
def metadata() -> MocapMetaData
```

The metadata for the data to be read.

<a id="mopipe.core.data.reader.MocapReader.read"></a>

#### read

```python
def read() -> MocapTimeSeries
```

Read the data from the source and return it as a dataframe.

Returns
-------
MocapTimeSeries
    The data read from the source.

