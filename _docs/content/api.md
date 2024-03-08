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

<a id="mopipe.core.analysis.rqa"></a>

# mopipe.core.analysis.rqa

<a id="mopipe.core.analysis"></a>

# mopipe.core.analysis

<a id="mopipe.core.common.datastructs"></a>

# mopipe.core.common.datastructs

datastructs.py

This module contains the data structures used by the mopipe package.

<a id="mopipe.core.common.datastructs.DataLevel"></a>

## DataLevel Objects

```python
class DataLevel(IntEnum)
```

DataLevel

Enum for the different levels of data that can be read by the
mopipe package.

<a id="mopipe.core.common.datastructs.EnumContainsMeta"></a>

## EnumContainsMeta Objects

```python
class EnumContainsMeta(EnumMeta)
```

ExtendedStrEnum

This is an extension of the StrEnum class from the enum module.
It adds the __contains__ method, which allows checking if a
string is a valid member of the enum.

It also adds the __getitem__ method, which allows getting the
value of a member from its name, or if you already pass in a value,
it will return the value.

<a id="mopipe.core.common.datastructs.MocapMetadataEntries"></a>

## MocapMetadataEntries Objects

```python
class MocapMetadataEntries(StrEnum, metaclass=EnumContainsMeta)
```

MocapMetadata

Common metadata for all MoCap data, and their transformed names.
This allows a common interface for all MoCap data.

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

<a id="mopipe.core.common.util"></a>

# mopipe.core.common.util

util.py

Common utility functions.

<a id="mopipe.core.common.util.maybe_generate_id"></a>

#### maybe\_generate\_id

```python
def maybe_generate_id(_id: t.Optional[str] = None,
                      prefix: t.Optional[str] = None,
                      suffix: t.Optional[str] = None) -> str
```

Generate a random id if not provided.

This provides a fluid interface for generating unique ids for various classes.
Sometimes, a user may want to provide their own id, and if so, this function
will simply return the id they provided. If no id is provided, a random id
will be generated.

Parameters
----------
_id : str, optional
    The id to use.
prefix : str, optional
    The prefix to use for the id.
suffix : str, optional
    The suffix to use for the id.

Returns
-------
str
    The id.

<a id="mopipe.core.common"></a>

# mopipe.core.common

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

<a id="mopipe.core.data.empirical"></a>

# mopipe.core.data.empirical

This contains base classes for defining data associated with experiemnts

<a id="mopipe.core.data.empirical.MetaData"></a>

## MetaData Objects

```python
class MetaData(dict)
```

MetaData

Base class for all metadata associated with data.

<a id="mopipe.core.data.empirical.MocapMetaData"></a>

## MocapMetaData Objects

```python
class MocapMetaData(MetaData)
```

MocapMetaData

This automatically transforms the keys of the metadata to the
known names in MocapMetadataEntries.

<a id="mopipe.core.data.empirical.EmpiricalData"></a>

## EmpiricalData Objects

```python
class EmpiricalData()
```

EmpiricalData

Base class for all empirical data.

<a id="mopipe.core.data.empirical.DiscreteData"></a>

## DiscreteData Objects

```python
class DiscreteData(EmpiricalData)
```

DiscreteData

For data that is associated with a level, but not timeseries.

<a id="mopipe.core.data.empirical.TimeseriesData"></a>

## TimeseriesData Objects

```python
class TimeseriesData(EmpiricalData)
```

TimeseriesData

For timeserioes data that is associated with a level.

<a id="mopipe.core.data.empirical.MocapTimeSeries"></a>

## MocapTimeSeries Objects

```python
class MocapTimeSeries(TimeseriesData)
```

MocapTimeSeries

For Mocap data (i.e. 3D marker positions).

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

<a id="mopipe.core.data"></a>

# mopipe.core.data

<a id="mopipe.core.segments.inputs"></a>

# mopipe.core.segments.inputs

<a id="mopipe.core.segments.inputs.InputTypeBaseMixin"></a>

## InputTypeBaseMixin Objects

```python
class InputTypeBaseMixin(IOTypeBaseMixin)
```

Mixin class for all segments input types.

<a id="mopipe.core.segments.inputs.InputTypeBaseMixin.input_type"></a>

#### input\_type

```python
@property
def input_type() -> IOType
```

The type of the input.

<a id="mopipe.core.segments.inputs.InputTypeBaseMixin.validate_input"></a>

#### validate\_input

```python
@abstractmethod
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.UnivariateSeriesInput"></a>

## UnivariateSeriesInput Objects

```python
class UnivariateSeriesInput(InputTypeBaseMixin)
```

Mixin class for univariate series input segments.

<a id="mopipe.core.segments.inputs.UnivariateSeriesInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.MultivariateSeriesInput"></a>

## MultivariateSeriesInput Objects

```python
class MultivariateSeriesInput(InputTypeBaseMixin)
```

Mixin class for multivariate series input segments.

<a id="mopipe.core.segments.inputs.MultivariateSeriesInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.SingleValueInput"></a>

## SingleValueInput Objects

```python
class SingleValueInput(InputTypeBaseMixin)
```

Mixin class for single value input segments.

<a id="mopipe.core.segments.inputs.SingleValueInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.MultiValueInput"></a>

## MultiValueInput Objects

```python
class MultiValueInput(InputTypeBaseMixin)
```

Mixin class for multiple values input segments.

<a id="mopipe.core.segments.inputs.MultiValueInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.SingleNumericValueInput"></a>

## SingleNumericValueInput Objects

```python
class SingleNumericValueInput(InputTypeBaseMixin)
```

Mixin class for single numeric value input segments.

<a id="mopipe.core.segments.inputs.SingleNumericValueInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.AnySeriesInput"></a>

## AnySeriesInput Objects

```python
class AnySeriesInput(InputTypeBaseMixin)
```

Mixin class for any series input segments.

<a id="mopipe.core.segments.inputs.AnySeriesInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.AnyNumericInput"></a>

## AnyNumericInput Objects

```python
class AnyNumericInput(InputTypeBaseMixin)
```

Mixin class for any numeric input segments.

<a id="mopipe.core.segments.inputs.AnyNumericInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.AnyInput"></a>

## AnyInput Objects

```python
class AnyInput(InputTypeBaseMixin)
```

Mixin class for any input segments.

<a id="mopipe.core.segments.inputs.AnyInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.OtherInput"></a>

## OtherInput Objects

```python
class OtherInput(InputTypeBaseMixin)
```

Mixin class for other input segments.

<a id="mopipe.core.segments.inputs.OtherInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.io"></a>

# mopipe.core.segments.io

<a id="mopipe.core.segments.io.IOType"></a>

## IOType Objects

```python
class IOType(Enum)
```

Type of segment inputs/outputs.

This is used to determine whether a segment can be run on a given
input, or if the output of a segment can be used as input to another.

<a id="mopipe.core.segments.io.IOTypeBaseMixin"></a>

## IOTypeBaseMixin Objects

```python
class IOTypeBaseMixin()
```

Mixin class for all segments input/output types.

<a id="mopipe.core.segments.outputs"></a>

# mopipe.core.segments.outputs

<a id="mopipe.core.segments.outputs.OutputTypeBaseMixin"></a>

## OutputTypeBaseMixin Objects

```python
class OutputTypeBaseMixin(IOTypeBaseMixin)
```

Mixin class for all segments output types.

<a id="mopipe.core.segments.outputs.OutputTypeBaseMixin.output_type"></a>

#### output\_type

```python
@property
def output_type() -> IOType
```

The type of the output.

<a id="mopipe.core.segments.outputs.OutputTypeBaseMixin.validate_output"></a>

#### validate\_output

```python
@abstractmethod
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.UnivariateSeriesOutput"></a>

## UnivariateSeriesOutput Objects

```python
class UnivariateSeriesOutput(OutputTypeBaseMixin)
```

Mixin class for univariate series output segments.

<a id="mopipe.core.segments.outputs.UnivariateSeriesOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.MultivariateSeriesOutput"></a>

## MultivariateSeriesOutput Objects

```python
class MultivariateSeriesOutput(OutputTypeBaseMixin)
```

Mixin class for multivariate series output segments.

<a id="mopipe.core.segments.outputs.MultivariateSeriesOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.SingleValueOutput"></a>

## SingleValueOutput Objects

```python
class SingleValueOutput(OutputTypeBaseMixin)
```

Mixin class for single value output segments.

<a id="mopipe.core.segments.outputs.SingleValueOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.MultiValueOutput"></a>

## MultiValueOutput Objects

```python
class MultiValueOutput(OutputTypeBaseMixin)
```

Mixin class for multiple values output segments.

<a id="mopipe.core.segments.outputs.MultiValueOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.SingleNumericValueOutput"></a>

## SingleNumericValueOutput Objects

```python
class SingleNumericValueOutput(OutputTypeBaseMixin)
```

Mixin class for single numeric value output segments.

<a id="mopipe.core.segments.outputs.SingleNumericValueOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.AnySeriesOutput"></a>

## AnySeriesOutput Objects

```python
class AnySeriesOutput(OutputTypeBaseMixin)
```

Mixin class for any series output segments.

<a id="mopipe.core.segments.outputs.AnySeriesOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.AnyNumericOutput"></a>

## AnyNumericOutput Objects

```python
class AnyNumericOutput(OutputTypeBaseMixin)
```

Mixin class for any numeric output segments.

<a id="mopipe.core.segments.outputs.AnyNumericOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.AnyOutput"></a>

## AnyOutput Objects

```python
class AnyOutput(OutputTypeBaseMixin)
```

Mixin class for any output segments.

<a id="mopipe.core.segments.outputs.AnyOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.OtherOutput"></a>

## OtherOutput Objects

```python
class OtherOutput(OutputTypeBaseMixin)
```

Mixin class for other output segments.

<a id="mopipe.core.segments.outputs.OtherOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.preprocessor"></a>

# mopipe.core.segments.preprocessor

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

<a id="mopipe.core.segments"></a>

# mopipe.core.segments

<a id="mopipe.core"></a>

# mopipe.core

<a id="mopipe.segment"></a>

# mopipe.segment

<a id="mopipe.__about__"></a>

# mopipe.\_\_about\_\_

