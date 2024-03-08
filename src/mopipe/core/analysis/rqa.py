import numpy as np
import scipy  # type: ignore
from pandas.api.extensions import ExtensionArray


def calc_rqa(
    x: ExtensionArray | np.ndarray,
    y: ExtensionArray | np.ndarray,
    dim: int = 1,
    tau: int = 1,
    threshold: float = 0.1,
    lmin: int = 2,
) -> list[float]:
    """Calculate Recurrence Quantification Analysis (RQA) statistics for the input series.

    Args:
        x (ExtensionArray | np.ndarray): The input series.
        y (ExtensionArray | np.ndarray): The input series.
        dim (int, optional): The embedding dimension. Defaults to 1.
        tau (int, optional): The time delay. Defaults to 1.
        threshold (float, optional): The recurrence threshold. Defaults to 0.1.
        lmin (int, optional): The minimum line length. Defaults to 2.

    Returns:
        list[float]: The RQA statistics.
    """
    embed_data_x: list[np.ndarray] | np.ndarray = []
    embed_data_y: list[np.ndarray] | np.ndarray = []
    for i in range(dim):
        embed_data_x.append(x[i * tau : x.shape[0] - (dim - i - 1) * tau])  # type: ignore
        embed_data_y.append(y[i * tau : y.shape[0] - (dim - i - 1) * tau])  # type: ignore
    embed_data_x, embed_data_y = np.array(embed_data_x), np.array(embed_data_y)

    distance_matrix = scipy.spatial.distance_matrix(embed_data_x.T, embed_data_y.T)
    recurrence_matrix = distance_matrix < threshold
    msize = recurrence_matrix.shape[0]

    d_line_dist = np.zeros(msize + 1)
    for i in range(-msize + 1, msize):
        cline = 0
        for e in np.diagonal(recurrence_matrix, i):
            if e:
                cline += 1
            else:
                d_line_dist[cline] += 1
                cline = 0
        d_line_dist[cline] += 1

    v_line_dist = np.zeros(msize + 1)
    for i in range(msize):
        cline = 0
        for e in recurrence_matrix[:, i]:
            if e:
                cline += 1
            else:
                v_line_dist[cline] += 1
                cline = 0
        v_line_dist[cline] += 1

    rr_sum = recurrence_matrix.sum()
    rr = rr_sum / msize**2
    det = (d_line_dist[lmin:] * np.arange(msize + 1)[lmin:]).sum() / rr_sum if rr_sum > 0 else 0
    lam = (v_line_dist[lmin:] * np.arange(msize + 1)[lmin:]).sum() / rr_sum if rr_sum > 0 else 0

    d_sum = d_line_dist[lmin:].sum()
    avg_diag_length = (d_line_dist[lmin:] * np.arange(msize + 1)[lmin:]).sum() / d_sum if d_sum > 0 else 0
    v_sum = d_line_dist[lmin:].sum()
    avg_vert_length = (v_line_dist[lmin:] * np.arange(msize + 1)[lmin:]).sum() / v_sum if v_sum > 0 else 0

    d_probs = d_line_dist[lmin:][d_line_dist[lmin:] > 0]
    d_probs /= d_probs.sum()
    d_entropy = -(d_probs * np.log(d_probs)).sum()

    v_probs = v_line_dist[lmin:][v_line_dist[lmin:] > 0]
    v_probs /= v_probs.sum()
    v_entropy = -(v_probs * np.log(v_probs)).sum()

    return [rr, det, lam, avg_diag_length, avg_vert_length, d_entropy, v_entropy]
