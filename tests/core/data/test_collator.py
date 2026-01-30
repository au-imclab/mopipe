import typing as t
from pathlib import Path

import numpy as np
import pandas as pd
import pytest  # type: ignore

from mopipe.core.data import EmpiricalData, MetaData, MocapReader
from mopipe.core.data.collator import MocapDataCollator


class FakeReader:
    """Fake reader that returns controlled data for testing."""

    _allowed_extensions: t.ClassVar[list[str]] = [".csv"]

    def __init__(self, data, metadata, name="fake"):
        self._data = data
        self._metadata = metadata
        self._name = name

    @property
    def name(self):
        return self._name

    def read(self):
        return EmpiricalData(
            data=self._data,
            metadata=self._metadata,
            name=self._name,
        )


class TestCollatorBasic:
    def test_constructor(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        assert collator is not None
        assert len(collator.readers) == 0

    def test_add_reader(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        reader = FakeReader(
            data=pd.DataFrame({"a": [1, 2, 3]}),
            metadata=MetaData(sample_rate=100.0),
            name="r1",
        )
        idx = collator.add_reader(reader)
        assert idx == 0
        assert len(collator.readers) == 1

    def test_add_reader_with_primary(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        r1 = FakeReader(pd.DataFrame({"a": [1]}), MetaData(sample_rate=100.0), "r1")
        r2 = FakeReader(pd.DataFrame({"b": [1]}), MetaData(sample_rate=200.0), "r2")
        collator.add_reader(r1)
        collator.add_reader(r2, is_primary=True)
        assert collator.primary_reader == 1

    def test_set_primary_reader(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        r1 = FakeReader(pd.DataFrame({"a": [1]}), MetaData(sample_rate=100.0), "r1")
        r2 = FakeReader(pd.DataFrame({"b": [1]}), MetaData(sample_rate=200.0), "r2")
        collator.add_reader(r1)
        collator.add_reader(r2)
        collator.set_primary_reader(1)
        assert collator.primary_reader == 1

    def test_set_primary_reader_out_of_range(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        with pytest.raises(IndexError):
            collator.set_primary_reader(0)


class TestCollatorCollate:
    def test_no_readers_raises(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        with pytest.raises(ValueError, match="No readers"):
            collator.collate()

    def test_single_reader(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        df = pd.DataFrame({"a": [1.0, 2.0, 3.0], "b": [4.0, 5.0, 6.0]})
        reader = FakeReader(df, MetaData(sample_rate=100.0), "r1")
        collator.add_reader(reader)

        result = collator.collate()
        assert isinstance(result, EmpiricalData)
        assert result.data.shape == (3, 2)
        assert result.metadata["sample_rate"] == 100.0

    def test_same_rate_collation(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        df1 = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
        df2 = pd.DataFrame({"b": [4.0, 5.0, 6.0]})
        r1 = FakeReader(df1, MetaData(sample_rate=100.0), "r1")
        r2 = FakeReader(df2, MetaData(sample_rate=100.0), "r2")
        collator.add_reader(r1)
        collator.add_reader(r2)

        result = collator.collate()
        assert result.data.shape == (3, 2)
        assert list(result.data.columns) == ["a", "b"]
        assert np.array_equal(result.data["a"].values, [1.0, 2.0, 3.0])
        assert np.array_equal(result.data["b"].values, [4.0, 5.0, 6.0])

    def test_different_rate_collation(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        # Primary at 100 Hz, 10 samples
        df1 = pd.DataFrame({"a": np.linspace(0, 1, 10)})
        # Secondary at 50 Hz, 5 samples (same duration)
        df2 = pd.DataFrame({"b": np.linspace(0, 1, 5)})
        r1 = FakeReader(df1, MetaData(sample_rate=100.0), "primary")
        r2 = FakeReader(df2, MetaData(sample_rate=50.0), "secondary")
        collator.add_reader(r1, is_primary=True)
        collator.add_reader(r2)

        result = collator.collate()
        # Secondary should be resampled to 10 samples to match primary
        assert result.data.shape[0] == 10
        assert "a" in result.data.columns
        assert "b" in result.data.columns

    def test_metadata_in_result(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="combined",
        )
        df = pd.DataFrame({"a": [1.0, 2.0]})
        r1 = FakeReader(df, MetaData(sample_rate=100.0), "source1")
        collator.add_reader(r1)

        result = collator.collate()
        assert result.name == "combined"
        assert result.metadata["sample_rate"] == 100.0
        assert result.metadata["n_frames"] == 2
        assert result.metadata["n_sources"] == 1
        assert result.metadata["source_names"] == ["source1"]

    def test_truncate_to_shortest(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        df1 = pd.DataFrame({"a": [1.0, 2.0, 3.0, 4.0, 5.0]})
        df2 = pd.DataFrame({"b": [1.0, 2.0, 3.0]})
        r1 = FakeReader(df1, MetaData(sample_rate=100.0), "r1")
        r2 = FakeReader(df2, MetaData(sample_rate=100.0), "r2")
        collator.add_reader(r1)
        collator.add_reader(r2)

        result = collator.collate()
        assert result.data.shape[0] == 3


class TestCollatorWithRealReader:
    def test_with_mocap_reader(self):
        collator = MocapDataCollator(
            output_dir=Path("tests/fixtures"),
            output_name="test",
        )
        reader = MocapReader(
            source=Path("tests/fixtures/sample_dance_with_header.tsv"),
            name="test",
        )
        collator.add_reader(reader)
        assert len(collator.readers) == 1
