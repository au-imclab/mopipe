import pandas as pd
import pytest  # type: ignore

from mopipe.core.data.empirical import MocapMetaData, MocapTimeSeries


class TestMocapMetaData:
    def test_metadata_transform(self):
        metadata = MocapMetaData(key1="value1", key2="value2")
        assert metadata["key1"] == "value1"
        assert metadata["key2"] == "value2"

    def test_setitem(self):
        metadata = MocapMetaData()
        metadata["key1"] = "value1"
        assert metadata["key1"] == "value1"

    def test_getitem(self):
        metadata = MocapMetaData(key1="value1")
        assert metadata["key1"] == "value1"


class TestMocapTimeSeries:
    @pytest.fixture
    def mocap_time_series(self) -> MocapTimeSeries:
        data = pd.DataFrame({"X": [1, 2, 3], "Y": [4, 5, 6], "Z": [7, 8, 9]})
        metadata = MocapMetaData(key1="value1", key2="value2")
        return MocapTimeSeries(data, metadata, "mocap_data")

    def test_getitem(self, mocap_time_series: MocapTimeSeries):
        assert mocap_time_series["X"].tolist() == [1, 2, 3]
        assert mocap_time_series[0].tolist() == [1, 4, 7]

    def test_data_id_generation(self, mocap_time_series: MocapTimeSeries):
        assert mocap_time_series.data_id.startswith("mocap_data")

    def test_metadata_access(self, mocap_time_series: MocapTimeSeries):
        assert mocap_time_series.metadata["key1"] == "value1"
        assert mocap_time_series.metadata["key2"] == "value2"
