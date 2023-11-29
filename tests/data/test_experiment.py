from mopipe.data import Experiment


def test_levels():
    ex = Experiment("test")
    assert ex is not None
    assert ex.level_name == "experiment"
    assert ex.level_id == "test"
    assert ex.parent is None
    assert ex.child is None
