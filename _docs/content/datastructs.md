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

