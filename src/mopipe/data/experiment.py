"""Experiment structure classes."""

import logging
import typing as t


class ExperimentLevel:
    """Base class for experiment structure classes.

    This class can be used to drop in data that applies to specific
    levels of an experiment, e.g. experiment-wide data, group-level,
    condition-level, trial-level etc.
    """

    _parent: t.Optional["ExperimentLevel"] = None
    _child: t.Optional["ExperimentLevel"] = None
    _leveldata: t.Optional[list] = None
    _timeseries: t.Optional[list] = None
    _level_name: str
    _level_id: str
    _depth: int = 1

    def __init__(self, level_name: str, level_id: str) -> None:
        """Initialize an ExperimentLevel."""
        self._level_name = level_name
        self._level_id = level_id

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
                f"with {child.level_name} ({child.l})."
            )
        child._parent = self
        self._child = child
        self.relevel_stack()

    @property
    def depth(self) -> int:
        """Depth of the level."""
        return self._depth

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
            return self
        return self._parent.top()

    def bottom(self) -> "ExperimentLevel":
        """Get the bottom level."""
        if self._child is None:
            return self
        return self._child.bottom()

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
        depth = 0 if type(top) is Experiment else 1
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
