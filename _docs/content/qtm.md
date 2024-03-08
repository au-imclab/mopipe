<a id="mopipe.core.common.qtm"></a>

# mopipe.core.common.qtm

<a id="mopipe.core.common.qtm.TrajectoryType"></a>

## TrajectoryType Objects

```python
class TrajectoryType(Enum)
```

TrajectoryType

Enum for the different types of trajectories that can be exported by
QTM.

<a id="mopipe.core.common.qtm.TrajectoryType.from_str"></a>

#### from\_str

```python
@staticmethod
def from_str(string: str) -> "TrajectoryType"
```

Convert string to TrajectoryType.

Parameters
----------
string : str
    String to convert to TrajectoryType.

Returns
-------
TrajectoryType
    TrajectoryType corresponding to string.

<a id="mopipe.core.common.qtm.parse_time_stamp"></a>

#### parse\_time\_stamp

```python
def parse_time_stamp(time_stamp: list[str]) -> tuple[datetime, float]
```

Parse the time stamp from a list of strings.

Parameters
----------
time_stamp : List[str]
    List of strings containing the time stamp.

Returns
-------
Tuple[datetime, float]
    Tuple containing the time stamp and ?????.

<a id="mopipe.core.common.qtm.parse_event"></a>

#### parse\_event

```python
def parse_event(event: list[str]) -> list[tuple[str, int, float]]
```

Parse the event data from a list of strings.

Parameters
----------
event : List[str]
    List of strings containing the event.

Returns
-------
Tuple[str, float, float]
    Tuple containing the event name, index and elapsed time.

<a id="mopipe.core.common.qtm.parse_marker_names"></a>

#### parse\_marker\_names

```python
def parse_marker_names(marker_names: list[str]) -> list[str]
```

Parse the marker names from a list of strings.

Parameters
----------
marker_names : List[str]
    List of strings containing the marker names.

Returns
-------
List[str]
    List containing the marker names.

<a id="mopipe.core.common.qtm.parse_trajectory_types"></a>

#### parse\_trajectory\_types

```python
def parse_trajectory_types(
        trajectory_types: list[str]) -> list[TrajectoryType]
```

Parse the trajectory types from a list of strings.

Parameters
----------
trajectory_types : List[str]
    List of strings containing the trajectory types.

Returns
-------
List[TrajectoryType]
    List containing the trajectory types.

<a id="mopipe.core.common.qtm.parse_metadata_row"></a>

#### parse\_metadata\_row

```python
def parse_metadata_row(key: str, values: list[t.Any]) -> tuple[str, t.Any]
```

Parse a metadata row and return the key and value.

Parameters
----------
key : str
    The key of the metadata row.
values : List[Any]
    The values of the metadata row.

Returns
-------
Tuple[str, Any]
    Tuple containing the key and value of the metadata row.

