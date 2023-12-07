import sys

import pytest  # type: ignore

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum

from mopipe.core.common import datastructs as ds


def test_strenumcontainsmeta():
    class TSECM(StrEnum, metaclass=ds.EnumContainsMeta):
        A = "a"
        B = "b"

    assert "a" in TSECM
    assert "b" in TSECM
    assert "A" in TSECM
    assert "B" in TSECM

    assert "c" not in TSECM

    assert TSECM["a"] == "a"
    assert TSECM["b"] == "b"
    assert TSECM["A"] == "a"
    assert TSECM["B"] == "b"

    with pytest.raises(KeyError):
        TSECM["c"]

    assert TSECM.A == "a"
    assert TSECM.B == "b"
    with pytest.raises(AttributeError):
        TSECM.C  # type: ignore # noqa: B018
    with pytest.raises(AttributeError):
        TSECM.a  # type: ignore # noqa: B018
