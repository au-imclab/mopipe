"""Experiment structure classes."""

import logging
import sys
import typing as t

if sys.version_info >= (3, 11):
    from enum import StrEnum, auto
else:
    from enum import auto

    from strenum import StrEnum

from mopipe.common import maybe_generate_id

if t.TYPE_CHECKING:
    from mopipe.data import EmpiricalData

from mopipe.data import MetaData


class LDType(StrEnum):
    """Type of data associated with a level."""

    TIMESERIES = auto()
    LEVELDATA = auto()


class ExperimentLevel:
    """Base class for experiment structure classes.

    This class can be used to drop in data that applies to specific
    levels of an experiment, e.g. experiment-wide data, group-level,
    condition-level, trial-level etc.
    """

    _parent: t.Optional["ExperimentLevel"] = None
    _child: t.Optional["ExperimentLevel"] = None
    _leveldata: list["EmpiricalData"]
    _timeseries: list["EmpiricalData"]
    _data_names_map: dict[str, t.Any]
    _data_ids_map: dict[str, t.Any]
    _level_metadata: "MetaData"
    _level_name: str
    _level_id: str
    _depth: int = 1

    def __init__(
        self, level_name: str, level_id: t.Optional[str] = None, level_metadata: t.Optional[MetaData] = None
    ) -> None:
        """Initialize an ExperimentLevel."""
        self._level_name = level_name
        self._level_id = maybe_generate_id(level_id, prefix=level_name)
        self._leveldata = []
        self._timeseries = []
        self._level_metadata = level_metadata if level_metadata is not None else MetaData()
        self._data_names_map = {
            LDType.TIMESERIES: {},
            LDType.LEVELDATA: {},
        }

    @property
    def level_name(self) -> str:
        """Name of the level."""
        return self._level_name

    @property
    def level_id(self) -> str:
        """ID of the level."""
        return self._level_id

    @property
    def parent(self) -> t.Optional["ExperimentLevel"]:
        """Parent level."""
        return self._parent

    @parent.setter
    def parent(self, parent: "ExperimentLevel") -> None:
        """Set the parent level."""
        if self._parent is not None:
            self._parent._child = None
            logging.warning(
                f"Overwriting parent level {self._parent.level_name} (ID: {self._parent.level_id})"
                f"with {parent.level_name} ({parent.level_id})."
            )
        parent._child = self
        self._parent = parent
        self.relevel_stack()

    @property
    def child(self) -> t.Optional["ExperimentLevel"]:
        """Child level."""
        return self._child

    @child.setter
    def child(self, child: "ExperimentLevel") -> None:
        """Set the child level."""
        if self._child is not None:
            self._child._parent = None
            logging.warning(
                f"Overwriting child level {self._child.level_name} (ID: {self._child.level_id})"
                f"with {child.level_name} ({child.level_id})."
            )
        child._parent = self
        self._child = child
        self.relevel_stack()

    @property
    def depth(self) -> int:
        """Depth of the level."""
        return self._depth

    def _update_map_entry(self, key: str, data_map: dict[str, list[int]], idx: int) -> None:
        """Update a specific entry in the data map."""
        if key in data_map:
            logging.warn(f"Data {key} already exists in level {self.level_name} (ID: {self.level_id}).")
            if not isinstance(data_map[key], list):
                msg = f"Expected data {key} to be a list, but got {type(data_map[key])}."
                raise RuntimeError(msg)

            # compare to see if it is the same object, if so, then we should raise an error
            for existing_idx in data_map[key]:
                if self._leveldata[existing_idx] is self._leveldata[idx]:
                    msg = (
                        f"Data {key} already exists in level {self.level_name} (ID: {self.level_id}),"
                        f" but the data object is the same."
                    )
                    raise ValueError(msg)

            # add it if the existing data is not the same object
            data_map[key].append(idx)
        else:
            data_map[key] = [idx]

    def _update_data_map(self, data_id: str, data_name: str, idx: int, ld_type: LDType) -> None:
        """Update the appropriate data maps."""
        self._update_map_entry(data_name, self._data_names_map[ld_type], idx)
        self._update_map_entry(data_id, self._data_ids_map[ld_type], idx)

    def _new_data_added(self, data: "EmpiricalData", ld_type: LDType) -> None:
        """New data was added to the level.

        Update the appropriate data maps.
        """
        idx = (len(self._timeseries) - 1) if ld_type == LDType.TIMESERIES else (len(self._leveldata) - 1)
        data_id = data.data_id
        data_name = data.name
        self._update_data_map(data_id, data_name, idx, ld_type)

    def _remap_data(self, ld_type: LDType) -> None:
        """Remap the data."""
        self._data_names_map[ld_type] = {}
        self._data_ids_map[ld_type] = {}
        items = self._timeseries if ld_type == LDType.TIMESERIES else self._leveldata
        for idx, data in enumerate(items):
            data_id = data.data_id
            data_name = data.name
            self._update_data_map(data_id, data_name, idx, ld_type)

    @property
    def leveldata(self) -> list["EmpiricalData"]:
        """Level data."""
        return self._leveldata

    @leveldata.setter
    def leveldata(self, leveldata: t.Iterable["EmpiricalData"]) -> None:
        """Set the level data."""
        self._leveldata = list(leveldata)

    def add_leveldata(self, leveldata: "EmpiricalData") -> None:
        """Add level data to the level."""
        self._leveldata.append(leveldata)
        self._new_data_added(leveldata, LDType.LEVELDATA)

    @property
    def timeseries(self) -> list["EmpiricalData"]:
        """Timeseries data."""
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries: t.Iterable["EmpiricalData"]) -> None:
        """Set the timeseries data."""
        self._timeseries = list(timeseries)

    def add_timeseries(self, timeseries: "EmpiricalData") -> None:
        """Add a timeseries to the level."""
        self._timeseries.append(timeseries)
        self._new_data_added(timeseries, LDType.TIMESERIES)

    @property
    def level_metadata(self) -> "MetaData":
        """Level metadata."""
        return self._level_metadata

    @level_metadata.setter
    def level_metadata(self, level_metadata: "MetaData") -> None:
        """Set the level metadata."""
        self._level_metadata = level_metadata

    def climb(self) -> t.Iterator["ExperimentLevel"]:
        """Climb the experiment structure."""
        yield self
        if self._parent is not None:
            yield from self._parent.climb()

    def descend(self) -> t.Iterator["ExperimentLevel"]:
        """Descend the experiment structure."""
        yield self
        if self._child is not None:
            yield from self._child.descend()

    def top(self) -> "ExperimentLevel":
        """Get the top level."""
        if self._parent is None:
            top = self
        else:
            top = self._parent.top()

        if not isinstance(top, Experiment):
            logging.warning(f"Top level of experiment {self.level_name} (ID: {self.level_id}) is not an Experiment.")
        return top

    def bottom(self) -> "ExperimentLevel":
        """Get the bottom level."""
        if self._child is None:
            bottom = self
        else:
            bottom = self._child.bottom()

        if not isinstance(bottom, Trial):
            logging.warning(f"Bottom level of experiment {self.level_name} (ID: {self.level_id}) is not a Trial.")
        return bottom

    def _relevel(self, depth: int) -> None:
        """Relevel the experiment structure."""
        self._depth = depth
        if self._child is not None:
            self._child._relevel(depth + 1)

    def relevel_stack(self):
        """Relevel the experiment structure.

        This method will relevel the experiment structure, so that the
        top level is at depth 0, and each level below it is at depth 1.
        If the top level is not an Experiment, then the depth of the
        top level will be 1.
        """
        top = self.top()
        depth = 0 if isinstance(top, Experiment) else 1
        top._relevel(depth)

    def relevel_children(self) -> None:
        """Relevel the children of the experiment structure."""
        self._relevel(self._depth)


class Experiment(ExperimentLevel):
    _parent = None
    _depth = 0

    def __init__(self, experiment_id: str) -> None:
        """Initialize an Experiment."""
        super().__init__("experiment", experiment_id)

    @property
    def parent(self) -> ExperimentLevel | None:
        """Parent level."""
        return None

    @parent.setter
    def parent(self, parent: t.Any) -> None:  # noqa: ARG002
        """Set the parent level."""
        msg = "An Experiment cannot have a parent level."
        raise ValueError(msg)


class Trial(ExperimentLevel):
    _child = None

    def __init__(self, trial_id: str) -> None:
        """Initialize a Trial."""
        super().__init__("trial", trial_id)

    @property
    def child(self) -> ExperimentLevel | None:
        """Child level."""
        return None

    @child.setter
    def child(self, child: t.Any) -> None:  # noqa: ARG002
        """Set the child level."""
        msg = "A Trial cannot have a child level."
        raise ValueError(msg)
