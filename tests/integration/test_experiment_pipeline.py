import numpy as np
import pandas as pd
import pytest  # type: ignore

from mopipe.core.analysis import Pipeline
from mopipe.core.data import EmpiricalData, Experiment, ExperimentLevel, MetaData, TimeseriesData, Trial


class MockSegment:
    """Mock segment that doubles the input."""

    def __init__(self):
        self.name = "mock_double"

    def __call__(self, **kwargs):
        return kwargs["x"] * 2


class TestGetTimeseriesByName:
    def test_found(self):
        trial = Trial("t1")
        ts = TimeseriesData(
            data=pd.DataFrame({"a": [1, 2, 3]}),
            metadata=MetaData(),
            name="my_data",
        )
        trial.add_timeseries(ts)
        result = trial.get_timeseries_by_name("my_data")
        assert result is ts

    def test_not_found(self):
        trial = Trial("t1")
        result = trial.get_timeseries_by_name("nonexistent")
        assert result is None

    def test_empty_timeseries(self):
        trial = Trial("t1")
        result = trial.get_timeseries_by_name("anything")
        assert result is None


class TestGetTimeseriesById:
    def test_found(self):
        trial = Trial("t1")
        ts = TimeseriesData(
            data=pd.DataFrame({"a": [1, 2, 3]}),
            metadata=MetaData(),
            name="my_data",
            data_id="fixed_id",
        )
        trial.add_timeseries(ts)
        result = trial.get_timeseries_by_id("fixed_id")
        assert result is ts

    def test_not_found(self):
        trial = Trial("t1")
        result = trial.get_timeseries_by_id("nonexistent")
        assert result is None


class TestRunPipeline:
    def test_basic_run(self):
        trial = Trial("t1")
        df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
        ts = TimeseriesData(data=df, metadata=MetaData(), name="input")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        result = trial.run_pipeline(pipeline)

        assert isinstance(result, EmpiricalData)
        assert result.name == "input_processed"
        assert np.array_equal(result.data.values, (df * 2).values)
        # Result should be stored
        assert len(trial.timeseries) == 2

    def test_with_data_name(self):
        trial = Trial("t1")
        ts1 = TimeseriesData(data=pd.DataFrame({"a": [1.0]}), metadata=MetaData(), name="first")
        ts2 = TimeseriesData(data=pd.DataFrame({"a": [10.0]}), metadata=MetaData(), name="second")
        trial.add_timeseries(ts1)
        trial.add_timeseries(ts2)

        pipeline = Pipeline([MockSegment()])
        result = trial.run_pipeline(pipeline, data_name="second")

        assert np.array_equal(result.data.values, np.array([[20.0]]))

    def test_custom_result_name(self):
        trial = Trial("t1")
        ts = TimeseriesData(data=pd.DataFrame({"a": [1.0]}), metadata=MetaData(), name="input")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        result = trial.run_pipeline(pipeline, result_name="custom_output")

        assert result.name == "custom_output"

    def test_no_store(self):
        trial = Trial("t1")
        ts = TimeseriesData(data=pd.DataFrame({"a": [1.0]}), metadata=MetaData(), name="input")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        trial.run_pipeline(pipeline, store_result=False)

        # Only the original timeseries should remain
        assert len(trial.timeseries) == 1

    def test_no_timeseries_raises(self):
        trial = Trial("t1")
        pipeline = Pipeline([MockSegment()])
        with pytest.raises(ValueError, match="No timeseries data available"):
            trial.run_pipeline(pipeline)

    def test_name_not_found_raises(self):
        trial = Trial("t1")
        ts = TimeseriesData(data=pd.DataFrame({"a": [1.0]}), metadata=MetaData(), name="input")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        with pytest.raises(ValueError, match="not found"):
            trial.run_pipeline(pipeline, data_name="nonexistent")


class TestRunPipelineOnDescendants:
    def test_basic(self):
        ex = Experiment("exp1")
        group = ExperimentLevel("group", "g1")
        trial = Trial("t1")
        ex.child = group
        group.child = trial

        ts = TimeseriesData(data=pd.DataFrame({"a": [1.0, 2.0]}), metadata=MetaData(), name="data")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        results = ex.run_pipeline_on_descendants(pipeline)

        # Trial has data, so should get one result
        assert len(results) == 1
        assert np.array_equal(results[0].data.values, np.array([[2.0], [4.0]]))

    def test_target_depth(self):
        ex = Experiment("exp1")
        group = ExperimentLevel("group", "g1")
        trial = Trial("t1")
        ex.child = group
        group.child = trial

        # Add data to both group and trial
        ts_group = TimeseriesData(data=pd.DataFrame({"a": [1.0]}), metadata=MetaData(), name="data")
        ts_trial = TimeseriesData(data=pd.DataFrame({"a": [10.0]}), metadata=MetaData(), name="data")
        group.add_timeseries(ts_group)
        trial.add_timeseries(ts_trial)

        pipeline = Pipeline([MockSegment()])

        # Only run on trial (depth=2)
        results = ex.run_pipeline_on_descendants(pipeline, target_depth=2)
        assert len(results) == 1
        assert np.array_equal(results[0].data.values, np.array([[20.0]]))

    def test_skip_levels_without_data(self):
        ex = Experiment("exp1")
        group = ExperimentLevel("group", "g1")
        trial = Trial("t1")
        ex.child = group
        group.child = trial

        # Only add data to trial, not group
        ts = TimeseriesData(data=pd.DataFrame({"a": [5.0]}), metadata=MetaData(), name="data")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        results = ex.run_pipeline_on_descendants(pipeline)

        assert len(results) == 1

    def test_skip_levels_without_matching_name(self):
        ex = Experiment("exp1")
        trial = Trial("t1")
        ex.child = trial

        ts = TimeseriesData(data=pd.DataFrame({"a": [5.0]}), metadata=MetaData(), name="data")
        trial.add_timeseries(ts)

        pipeline = Pipeline([MockSegment()])
        results = ex.run_pipeline_on_descendants(pipeline, data_name="nonexistent")

        assert len(results) == 0
