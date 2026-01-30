<a id="mopipe.core.data.experiment"></a>

# mopipe.core.data.experiment

Experiment structure classes.

<a id="mopipe.core.data.experiment.LDType"></a>

## LDType Objects

```python
class LDType(StrEnum)
```

Type of data associated with a level.

<a id="mopipe.core.data.experiment.ExperimentLevel"></a>

## ExperimentLevel Objects

```python
class ExperimentLevel()
```

Base class for experiment structure classes.

This class can be used to drop in data that applies to specific
levels of an experiment, e.g. experiment-wide data, group-level,
condition-level, trial-level etc.

<a id="mopipe.core.data.experiment.ExperimentLevel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(level_name: str,
             level_id: t.Optional[str] = None,
             level_metadata: t.Optional[MetaData] = None) -> None
```

Initialize an ExperimentLevel.

<a id="mopipe.core.data.experiment.ExperimentLevel.level_name"></a>

#### level\_name

```python
@property
def level_name() -> str
```

Name of the level.

<a id="mopipe.core.data.experiment.ExperimentLevel.level_id"></a>

#### level\_id

```python
@property
def level_id() -> str
```

ID of the level.

<a id="mopipe.core.data.experiment.ExperimentLevel.parent"></a>

#### parent

```python
@property
def parent() -> t.Optional["ExperimentLevel"]
```

Parent level.

<a id="mopipe.core.data.experiment.ExperimentLevel.parent"></a>

#### parent

```python
@parent.setter
def parent(parent: "ExperimentLevel") -> None
```

Set the parent level.

<a id="mopipe.core.data.experiment.ExperimentLevel.child"></a>

#### child

```python
@property
def child() -> t.Optional["ExperimentLevel"]
```

Child level.

<a id="mopipe.core.data.experiment.ExperimentLevel.child"></a>

#### child

```python
@child.setter
def child(child: "ExperimentLevel") -> None
```

Set the child level.

<a id="mopipe.core.data.experiment.ExperimentLevel.depth"></a>

#### depth

```python
@property
def depth() -> int
```

Depth of the level.

<a id="mopipe.core.data.experiment.ExperimentLevel.leveldata"></a>

#### leveldata

```python
@property
def leveldata() -> list["EmpiricalData"]
```

Level data.

<a id="mopipe.core.data.experiment.ExperimentLevel.leveldata"></a>

#### leveldata

```python
@leveldata.setter
def leveldata(leveldata: t.Iterable["EmpiricalData"]) -> None
```

Set the level data.

<a id="mopipe.core.data.experiment.ExperimentLevel.add_leveldata"></a>

#### add\_leveldata

```python
def add_leveldata(leveldata: "EmpiricalData") -> None
```

Add level data to the level.

<a id="mopipe.core.data.experiment.ExperimentLevel.timeseries"></a>

#### timeseries

```python
@property
def timeseries() -> list["EmpiricalData"]
```

Timeseries data.

<a id="mopipe.core.data.experiment.ExperimentLevel.timeseries"></a>

#### timeseries

```python
@timeseries.setter
def timeseries(timeseries: t.Iterable["EmpiricalData"]) -> None
```

Set the timeseries data.

<a id="mopipe.core.data.experiment.ExperimentLevel.add_timeseries"></a>

#### add\_timeseries

```python
def add_timeseries(timeseries: "EmpiricalData") -> None
```

Add a timeseries to the level.

<a id="mopipe.core.data.experiment.ExperimentLevel.level_metadata"></a>

#### level\_metadata

```python
@property
def level_metadata() -> "MetaData"
```

Level metadata.

<a id="mopipe.core.data.experiment.ExperimentLevel.level_metadata"></a>

#### level\_metadata

```python
@level_metadata.setter
def level_metadata(level_metadata: "MetaData") -> None
```

Set the level metadata.

<a id="mopipe.core.data.experiment.ExperimentLevel.get_timeseries_by_name"></a>

#### get\_timeseries\_by\_name

```python
def get_timeseries_by_name(name: str) -> t.Optional["EmpiricalData"]
```

Look up a timeseries by name.

Parameters
----------
name : str
    The name of the timeseries to find.

Returns
-------
EmpiricalData or None
    The first matching timeseries, or None if not found.

<a id="mopipe.core.data.experiment.ExperimentLevel.get_timeseries_by_id"></a>

#### get\_timeseries\_by\_id

```python
def get_timeseries_by_id(data_id: str) -> t.Optional["EmpiricalData"]
```

Look up a timeseries by data ID.

Parameters
----------
data_id : str
    The ID of the timeseries to find.

Returns
-------
EmpiricalData or None
    The first matching timeseries, or None if not found.

<a id="mopipe.core.data.experiment.ExperimentLevel.run_pipeline"></a>

#### run\_pipeline

```python
def run_pipeline(pipeline: "Pipeline",
                 data_name: t.Optional[str] = None,
                 result_name: t.Optional[str] = None,
                 *,
                 store_result: bool = True,
                 **kwargs) -> "EmpiricalData"
```

Run a pipeline on timeseries data at this level.

Parameters
----------
pipeline : Pipeline
    The pipeline to run.
data_name : str, optional
    Name of the timeseries to use as input. If None, uses the first available.
result_name : str, optional
    Name for the result timeseries. Defaults to "{source_name}_processed".
store_result : bool, optional
    Whether to store the result back on this level. Defaults to True.
**kwargs
    Additional keyword arguments passed to pipeline.run().

Returns
-------
EmpiricalData
    The result wrapped as a TimeseriesData.

Raises
------
ValueError
    If no timeseries data is available or the named timeseries is not found.

<a id="mopipe.core.data.experiment.ExperimentLevel.run_pipeline_on_descendants"></a>

#### run\_pipeline\_on\_descendants

```python
def run_pipeline_on_descendants(pipeline: "Pipeline",
                                target_depth: t.Optional[int] = None,
                                data_name: t.Optional[str] = None,
                                result_name: t.Optional[str] = None,
                                **kwargs) -> list["EmpiricalData"]
```

Run a pipeline on descendant levels that have timeseries data.

Parameters
----------
pipeline : Pipeline
    The pipeline to run.
target_depth : int, optional
    Only run on levels at this depth. If None, runs on all descendants with data.
data_name : str, optional
    Name of the timeseries to use as input on each level.
result_name : str, optional
    Name for the result timeseries on each level.
**kwargs
    Additional keyword arguments passed to pipeline.run().

Returns
-------
list[EmpiricalData]
    List of result EmpiricalData from each level that was processed.

<a id="mopipe.core.data.experiment.ExperimentLevel.climb"></a>

#### climb

```python
def climb() -> t.Iterator["ExperimentLevel"]
```

Climb the experiment structure.

<a id="mopipe.core.data.experiment.ExperimentLevel.descend"></a>

#### descend

```python
def descend() -> t.Iterator["ExperimentLevel"]
```

Descend the experiment structure.

<a id="mopipe.core.data.experiment.ExperimentLevel.top"></a>

#### top

```python
def top() -> "ExperimentLevel"
```

Get the top level.

<a id="mopipe.core.data.experiment.ExperimentLevel.bottom"></a>

#### bottom

```python
def bottom() -> "ExperimentLevel"
```

Get the bottom level.

<a id="mopipe.core.data.experiment.ExperimentLevel.relevel_stack"></a>

#### relevel\_stack

```python
def relevel_stack()
```

Relevel the experiment structure.

This method will relevel the experiment structure, so that the
top level is at depth 0, and each level below it is at depth 1.
If the top level is not an Experiment, then the depth of the
top level will be 1.

<a id="mopipe.core.data.experiment.ExperimentLevel.relevel_children"></a>

#### relevel\_children

```python
def relevel_children() -> None
```

Relevel the children of the experiment structure.

<a id="mopipe.core.data.experiment.Experiment"></a>

## Experiment Objects

```python
class Experiment(ExperimentLevel)
```

<a id="mopipe.core.data.experiment.Experiment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(experiment_id: str) -> None
```

Initialize an Experiment.

<a id="mopipe.core.data.experiment.Experiment.parent"></a>

#### parent

```python
@property
def parent() -> ExperimentLevel | None
```

Parent level.

<a id="mopipe.core.data.experiment.Experiment.parent"></a>

#### parent

```python
@parent.setter
def parent(parent: t.Any) -> None
```

Set the parent level.

<a id="mopipe.core.data.experiment.Trial"></a>

## Trial Objects

```python
class Trial(ExperimentLevel)
```

<a id="mopipe.core.data.experiment.Trial.__init__"></a>

#### \_\_init\_\_

```python
def __init__(trial_id: str) -> None
```

Initialize a Trial.

<a id="mopipe.core.data.experiment.Trial.child"></a>

#### child

```python
@property
def child() -> ExperimentLevel | None
```

Child level.

<a id="mopipe.core.data.experiment.Trial.child"></a>

#### child

```python
@child.setter
def child(child: t.Any) -> None
```

Set the child level.

