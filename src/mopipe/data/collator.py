"""collator.py

This module contains the Mocap Data Collator class, which is used to
collate data from multiple sources and save it.
"""

from pathlib import Path

from pandas import DataFrame

from mopipe.data import AbstractReader


class MocapDataCollator:
    """MocapDataCollator

    The MocapDataCollator class is used to collate data from multiple
    sources and save it.
    """

    def __init__(self, output_dir: Path, output_name: str):
        """Initialize the MocapDataCollator.

        Parameters
        ----------
        output_dir : Path
            The directory to save the collated data in.
        output_name : str
            The base name to save the collated data under.
        level : DataLevel
            The level of the data to be read.
        """
        self._output_dir = output_dir
        self._output_name = output_name
        self._readers: list[AbstractReader] = []
        self._primary_reader: int = 0

    @property
    def readers(self) -> list[AbstractReader]:
        """The readers to be used to read the data."""
        return self._readers

    @property
    def output_dir(self) -> Path:
        """The directory to save the collated data in."""
        return self._output_dir

    @property
    def output_name(self) -> str:
        """The name to save the collated data under."""
        return self._output_name

    def add_reader(self, reader: AbstractReader) -> int:
        """Add a reader to the collator.

        Parameters
        ----------
        reader : AbstractReader
            The reader to be added.

        Returns
        -------
        int
            The reader index.
        """
        self._readers.append(reader)
        idx = len(self._readers) - 1
        return idx

    def collate(self) -> DataFrame:
        """Collate the data from the readers.

        Returns
        -------
        DataFrame
            The collated data.
        """
        raise NotImplementedError
