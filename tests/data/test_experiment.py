from mopipe.data.experiment import ExperimentLevel, Experiment, Trial


def test_levels():
    ex = Experiment("test")
    assert ex is not None
    assert ex.level_name == "experiment"
    assert ex.id == "test"
    assert ex.parent is None
    assert ex.child is None
    


