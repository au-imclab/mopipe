import pytest  # type: ignore

from mopipe.core.data import Experiment, ExperimentLevel, Trial


def test_levels():
    ex = Experiment("test")
    assert ex is not None
    assert ex.level_name == "experiment"
    assert ex.level_id == "test"
    assert ex.parent is None
    assert ex.child is None
    assert ex.depth == 0

    group = ExperimentLevel("group", "group1")
    assert group is not None
    assert group.level_name == "group"
    assert group.level_id == "group1"
    assert group.parent is None
    assert group.child is None
    assert group.depth == 1

    ex.child = group
    assert ex.child is not None
    assert ex.child.level_name == "group"
    assert ex.child.level_id == "group1"
    assert ex.child.parent is not None
    assert ex.child.parent.level_name == "experiment"

    trial = Trial("trial1")
    assert trial is not None
    assert trial.level_name == "trial"
    assert trial.level_id == "trial1"
    assert trial.parent is None
    assert trial.child is None
    assert trial.depth == 1

    group.child = trial
    assert group.child is not None
    assert group.child.level_name == "trial"
    assert group.child.level_id == "trial1"
    assert group.child.depth == 2
    assert group.child.parent is not None
    assert group.child.parent.level_name == "group"
    assert group.child.parent.parent is not None
    assert group.child.parent.parent.level_name == "experiment"

    assert group.top() is ex
    assert group.bottom() is trial
    assert trial.top() is ex
    assert trial.bottom() is trial
    assert ex.top() is ex
    assert ex.bottom() is trial

    test = ExperimentLevel("test_level", "test_level")
    with pytest.raises(ValueError):
        trial.child = test
    with pytest.raises(ValueError):
        ex.parent = test
