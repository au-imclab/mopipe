<a id="mopipe.core.analysis.rqa"></a>

# mopipe.core.analysis.rqa

<a id="mopipe.core.analysis.rqa.calc_rqa"></a>

#### calc\_rqa

```python
def calc_rqa(x: ExtensionArray | np.ndarray,
             y: ExtensionArray | np.ndarray,
             dim: int = 1,
             tau: int = 1,
             threshold: float = 0.1,
             lmin: int = 2) -> list[float]
```

Calculate Recurrence Quantification Analysis (RQA) statistics for the input series.

**Arguments**:

- `x` _ExtensionArray | np.ndarray_ - The input series.
- `y` _ExtensionArray | np.ndarray_ - The input series.
- `dim` _int, optional_ - The embedding dimension. Defaults to 1.
- `tau` _int, optional_ - The time delay. Defaults to 1.
- `threshold` _float, optional_ - The recurrence threshold. Defaults to 0.1.
- `lmin` _int, optional_ - The minimum line length. Defaults to 2.
  

**Returns**:

- `list[float]` - The RQA statistics.

<a id="mopipe.core.common.util"></a>

# mopipe.core.common.util

util.py

Common utility functions.

<a id="mopipe.core.common.util.maybe_generate_id"></a>

#### maybe\_generate\_id

```python
def maybe_generate_id(_id: t.Optional[str] = None,
                      prefix: t.Optional[str] = None,
                      suffix: t.Optional[str] = None) -> str
```

Generate a random id if not provided.

This provides a fluid interface for generating unique ids for various classes.
Sometimes, a user may want to provide their own id, and if so, this function
will simply return the id they provided. If no id is provided, a random id
will be generated.

Parameters
----------
_id : str, optional
    The id to use.
prefix : str, optional
    The prefix to use for the id.
suffix : str, optional
    The suffix to use for the id.

Returns
-------
str
    The id.

