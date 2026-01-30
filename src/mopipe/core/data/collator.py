"""collator.py

This module contains the Mocap Data Collator class, which is used to
collate data from multiple sources and save it.
"""

import typing as t
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import interpolate as sp_interpolate

from mopipe.core.data import AbstractReader, EmpiricalData, MetaData

_INTERPOLATION_METHODS = ("linear", "cubic", "nearest")


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

    @property
    def primary_reader(self) -> int:
        """Index of the primary reader that determines the output sample rate."""
        return self._primary_reader

    def set_primary_reader(self, index: int) -> None:
        """Set the primary reader by index.

        Parameters
        ----------
        index : int
            The index of the reader to set as primary.

        Raises
        ------
        IndexError
            If the index is out of range.
        """
        if index < 0 or index >= len(self._readers):
            msg = f"Reader index {index} is out of range (0-{len(self._readers) - 1})."
            raise IndexError(msg)
        self._primary_reader = index

    def add_reader(self, reader: AbstractReader, *, is_primary: bool = False) -> int:
        """Add a reader to the collator.

        Parameters
        ----------
        reader : AbstractReader
            The reader to be added.
        is_primary : bool, optional
            Whether this reader should be the primary reader (determines output sample rate).
            Defaults to False.

        Returns
        -------
        int
            The reader index.
        """
        self._readers.append(reader)
        idx = len(self._readers) - 1
        if is_primary:
            self._primary_reader = idx
        return idx

    @staticmethod
    def _get_sample_rate(data: EmpiricalData) -> t.Optional[float]:
        """Extract sample rate from EmpiricalData metadata.

        Parameters
        ----------
        data : EmpiricalData
            The data to extract the sample rate from.

        Returns
        -------
        float or None
            The sample rate, or None if not available.
        """
        metadata = data.metadata
        for key in ("sample_rate", "FREQUENCY"):
            if key in metadata:
                return float(metadata[key])
        return None

    @staticmethod
    def _resample(
        data: pd.DataFrame,
        from_rate: float,
        to_rate: float,
        method: str = "linear",
    ) -> pd.DataFrame:
        """Resample data from one sample rate to another.

        Parameters
        ----------
        data : DataFrame
            The data to resample.
        from_rate : float
            The source sample rate.
        to_rate : float
            The target sample rate.
        method : str, optional
            Interpolation method: 'linear', 'cubic', or 'nearest'. Defaults to 'linear'.

        Returns
        -------
        DataFrame
            The resampled data.
        """
        if from_rate == to_rate:
            return data

        if method not in _INTERPOLATION_METHODS:
            msg = f"Unknown interpolation method: {method}. Must be one of {_INTERPOLATION_METHODS}."
            raise ValueError(msg)

        n_samples_from = len(data)
        n_samples_to = int(n_samples_from * to_rate / from_rate)

        x_from = np.arange(n_samples_from)
        x_to = np.linspace(0, n_samples_from - 1, n_samples_to)

        resampled: dict[str, np.ndarray] = {}
        for col in data.columns:
            col_data = np.asarray(data[col].values, dtype=float)
            kind = method if method != "nearest" else "nearest"
            f = sp_interpolate.interp1d(x_from, col_data, kind=kind, fill_value="extrapolate")  # type: ignore[arg-type]
            resampled[str(col)] = f(x_to)

        return pd.DataFrame(resampled, index=range(n_samples_to))

    def collate(self, method: str = "linear") -> EmpiricalData:
        """Collate the data from the readers.

        Reads data from all readers, resamples non-primary data to match
        the primary reader's sample rate, truncates to the shortest length,
        and concatenates along columns.

        Parameters
        ----------
        method : str, optional
            Interpolation method for resampling: 'linear', 'cubic', or 'nearest'.
            Defaults to 'linear'.

        Returns
        -------
        EmpiricalData
            The collated data with combined metadata.

        Raises
        ------
        ValueError
            If no readers have been added or sample rates cannot be determined.
        """
        if not self._readers:
            msg = "No readers have been added to the collator."
            raise ValueError(msg)

        # Read all data
        datasets: list[EmpiricalData] = []
        for reader in self._readers:
            data = reader.read()
            if data is None:
                msg = f"Reader '{reader.name}' returned None."
                raise ValueError(msg)
            datasets.append(data)

        # Get primary sample rate
        primary_data = datasets[self._primary_reader]
        target_rate = self._get_sample_rate(primary_data)
        if target_rate is None:
            msg = "Could not determine sample rate from primary reader's metadata."
            raise ValueError(msg)

        # Align all data to primary sample rate
        aligned: list[pd.DataFrame] = []
        for i, dataset in enumerate(datasets):
            if i == self._primary_reader:
                aligned.append(dataset.data)
            else:
                source_rate = self._get_sample_rate(dataset)
                if source_rate is None:
                    msg = f"Could not determine sample rate from reader {i} metadata."
                    raise ValueError(msg)
                resampled = self._resample(dataset.data, source_rate, target_rate, method)
                aligned.append(resampled)

        # Truncate to shortest length
        min_len = min(len(df) for df in aligned)
        aligned = [df.iloc[:min_len].reset_index(drop=True) for df in aligned]

        # Concatenate along columns
        result = pd.concat(aligned, axis=1)

        # Build combined metadata
        combined_metadata = MetaData(
            sample_rate=target_rate,
            n_frames=len(result),
            n_sources=len(self._readers),
            source_names=[r.name for r in self._readers],
        )

        return EmpiricalData(
            data=result,
            metadata=combined_metadata,
            name=self._output_name,
        )
