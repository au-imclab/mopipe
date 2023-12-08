"""This contains base classes for defining data associated with experiemnts"""

import typing as t

from pandas import DataFrame, Series

from mopipe.core.common import MocapMetadataEntries, maybe_generate_id

if t.TYPE_CHECKING:
    from mopipe.core.data import ExperimentLevel


class MetaData(dict):
    """MetaData

    Base class for all metadata associated with data.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MocapMetaData(MetaData):
    """MocapMetaData

    This automatically transforms the keys of the metadata to the
    known names in MocapMetadataEntries.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in MocapMetadataEntries:
                kwargs[MocapMetadataEntries[key]] = value
        super().__init__(**kwargs)

    def __setitem__(self, key: str, value: t.Any):
        if key in MocapMetadataEntries:
            key = MocapMetadataEntries[key]
        super().__setitem__(key, value)

    def __getitem__(self, key: str):
        if key in MocapMetadataEntries:
            key = MocapMetadataEntries[key]
        return super().__getitem__(key)


class EmpiricalData:
    """EmpiricalData

    Base class for all empirical data.
    """

    data: DataFrame
    metadata: MetaData
    level: "ExperimentLevel"
    name: str
    data_id: str

    def __getitem__(self, key: t.Union[str, int]) -> Series:
        if isinstance(key, int):
            return self.data.iloc[key]
        return self.data[key]

    def __init__(self, data: DataFrame, metadata: MetaData, name: str, data_id: t.Optional[str] = None):
        self.data = data
        self.metadata = metadata
        self.name = name
        self.data_id = maybe_generate_id(data_id, prefix=name)


class DiscreteData(EmpiricalData):
    """DiscreteData

    For data that is associated with a level, but not timeseries.
    """

    pass


class TimeseriesData(EmpiricalData):
    """TimeseriesData

    For timeserioes data that is associated with a level.
    """

    pass


class MocapTimeSeries(TimeseriesData):
    """MocapTimeSeries

    For Mocap data (i.e. 3D marker positions).
    """

    metadata: MocapMetaData

    def __init__(self, data: DataFrame, metadata: MocapMetaData, name: str, data_id: t.Optional[str] = None):
        super().__init__(data, metadata, name, data_id)
