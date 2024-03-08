<a id="mopipe.core.data.collator"></a>

# mopipe.core.data.collator

collator.py

This module contains the Mocap Data Collator class, which is used to
collate data from multiple sources and save it.

<a id="mopipe.core.data.collator.MocapDataCollator"></a>

## MocapDataCollator Objects

```python
class MocapDataCollator()
```

MocapDataCollator

The MocapDataCollator class is used to collate data from multiple
sources and save it.

<a id="mopipe.core.data.collator.MocapDataCollator.__init__"></a>

#### \_\_init\_\_

```python
def __init__(output_dir: Path, output_name: str)
```

Initialize the MocapDataCollator.

Parameters
----------
output_dir : Path
    The directory to save the collated data in.
output_name : str
    The base name to save the collated data under.
level : DataLevel
    The level of the data to be read.

<a id="mopipe.core.data.collator.MocapDataCollator.readers"></a>

#### readers

```python
@property
def readers() -> list[AbstractReader]
```

The readers to be used to read the data.

<a id="mopipe.core.data.collator.MocapDataCollator.output_dir"></a>

#### output\_dir

```python
@property
def output_dir() -> Path
```

The directory to save the collated data in.

<a id="mopipe.core.data.collator.MocapDataCollator.output_name"></a>

#### output\_name

```python
@property
def output_name() -> str
```

The name to save the collated data under.

<a id="mopipe.core.data.collator.MocapDataCollator.add_reader"></a>

#### add\_reader

```python
def add_reader(reader: AbstractReader) -> int
```

Add a reader to the collator.

Parameters
----------
reader : AbstractReader
    The reader to be added.

Returns
-------
int
    The reader index.

<a id="mopipe.core.data.collator.MocapDataCollator.collate"></a>

#### collate

```python
def collate() -> DataFrame
```

Collate the data from the readers.

Returns
-------
DataFrame
    The collated data.

