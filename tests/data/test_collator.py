from pathlib import Path

from mopipe.data import MocapReader
from mopipe.data.collator import MocapDataCollator


def test_collator():
    collator = MocapDataCollator(
        output_dir=Path("tests/fixtures"),
        output_name="test",
    )
    assert collator is not None
    reader = MocapReader(
        source=Path("tests/fixtures/sample_dance_with_header.tsv"),
        name="test",
    )
    assert reader is not None
    collator.add_reader(reader)
    assert len(collator.readers) == 1
    # collator.collate()
