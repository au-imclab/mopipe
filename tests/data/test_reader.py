from pathlib import Path

import pandas as pd

from mopipe.common import MocapMetadataEntries
from mopipe.data import MocapReader


def test_metadata():
    assert MocapReader is not None
    reader = MocapReader(
        source=Path("tests/fixtures/sample_dance_with_header.tsv"),
        name="test",
    )
    assert reader is not None
    metadata = reader.metadata
    assert metadata is not None
    assert metadata[MocapMetadataEntries.sample_rate] == 300
    assert metadata[MocapMetadataEntries.frame_count] == 30


def test_reader():
    reader = MocapReader(
        source=Path("tests/fixtures/sample_dance_with_header.tsv"),
        name="test",
    )
    assert reader is not None
    data = reader.read()
    metadata = reader.metadata
    assert data is not None
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 30
    # ensure the right length
    # number of markers * 3 (x,y,z) + 1 (time)
    # frame number becomes the index
    assert len(data.columns) == metadata[MocapMetadataEntries.marker_count] * 3 + 1
