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

<a id="mopipe.core.data.collator.MocapDataCollator.primary_reader"></a>

#### primary\_reader

```python
@property
def primary_reader() -> int
```

Index of the primary reader that determines the output sample rate.

<a id="mopipe.core.data.collator.MocapDataCollator.set_primary_reader"></a>

#### set\_primary\_reader

```python
def set_primary_reader(index: int) -> None
```

Set the primary reader by index.

Parameters
----------
index : int
    The index of the reader to set as primary.

Raises
------
IndexError
    If the index is out of range.

<a id="mopipe.core.data.collator.MocapDataCollator.add_reader"></a>

#### add\_reader

```python
def add_reader(reader: AbstractReader, *, is_primary: bool = False) -> int
```

Add a reader to the collator.

Parameters
----------
reader : AbstractReader
    The reader to be added.
is_primary : bool, optional
    Whether this reader should be the primary reader (determines output sample rate).
    Defaults to False.

Returns
-------
int
    The reader index.

<a id="mopipe.core.data.collator.MocapDataCollator.collate"></a>

#### collate

```python
def collate(method: str = "linear") -> EmpiricalData
```

Collate the data from the readers.

Reads data from all readers, resamples non-primary data to match
the primary reader's sample rate, truncates to the shortest length,
and concatenates along columns.

Parameters
----------
method : str, optional
    Interpolation method for resampling: 'linear', 'cubic', or 'nearest'.
    Defaults to 'linear'.

Returns
-------
EmpiricalData
    The collated data with combined metadata.

Raises
------
ValueError
    If no readers have been added or sample rates cannot be determined.

