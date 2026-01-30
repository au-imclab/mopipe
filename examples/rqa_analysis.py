"""Example: Recurrence Quantification Analysis (RQA) for a leader-follower dance dyad.

This example demonstrates progressively richer RQA analyses:
    1. Auto-RQA on a single marker, single axis (follower left hip x-velocity)
    2. Cross-RQA on a single axis between opposite hips (follower left hip vs leader right hip)
    3. Cross-RQA on 3D speed (Euclidean norm of velocity) for opposite hips
    4. Cross-RQA on 3D speed for both hip sides combined
    5. Windowed cross-RQA to see coordination over time
    6. Cross-RQA on vertical hip displacement (the "bounce") using deltas from start

Notes on threshold selection:
    RQA compares absolute values, so raw marker positions won't work for
    cross-person comparison — the dancers are in different locations (~1200
    units apart). We use velocity (first difference of position), 3D speed
    (Euclidean norm of velocity), or displacement from the initial position
    to compare movement dynamics instead.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from mopipe.core.analysis import Pipeline
from mopipe.core.data import MocapReader
from mopipe.segment import CrossRQAStats, RQAStats, SimpleGapFilling, WindowedCrossRQAStats

# --- Load and preprocess ---
data_path = Path("tests/fixtures/sample_dance_with_header.tsv")
reader = MocapReader(source=data_path, name="dance_trial")
data = reader.read()

preprocess = Pipeline([SimpleGapFilling("fill_gaps")])
cleaned = preprocess.run(x=data.data)

print(f"Loaded {data.name}: {data.data.shape[0]} frames, {data.data.shape[1]} columns")
print("Markers include Follow_* (follower) and Lead_* (leader) hip markers\n")


# ==========================================================================
# 1. Auto-RQA: single marker, single axis
# ==========================================================================
# Compute x-velocity for the follower's left hip
follow_lhip_vx = cleaned["Follow_left_hip_x"].diff().dropna()

rqa_pipeline = Pipeline([RQAStats("auto_rqa")])
auto_result = rqa_pipeline.run(x=follow_lhip_vx, dim=1, tau=1, threshold=0.1)
print("1) Auto-RQA: Follower left hip x-velocity (threshold=0.1)")
print(auto_result.to_string(index=False))


# ==========================================================================
# 2. Cross-RQA: single axis, opposite hips (follower left vs leader right)
# ==========================================================================
# In partner dancing, opposite hips often mirror each other's movement.
follow_lhip_vx_arr = cleaned["Follow_left_hip_x"].diff().dropna().values
lead_rhip_vx_arr = cleaned["Lead_right_hip_x"].diff().dropna().values

cross_1d = pd.DataFrame(
    {
        "follow_lhip_vx": follow_lhip_vx_arr,
        "lead_rhip_vx": lead_rhip_vx_arr,
    }
)

cross_pipeline = Pipeline([CrossRQAStats("cross_rqa")])
cross_1d_result = cross_pipeline.run(x=cross_1d, col_a=0, col_b=1, threshold=0.1)
print("\n2) Cross-RQA: Follower left hip vs Leader right hip, x-velocity (threshold=0.1)")
print(cross_1d_result.to_string(index=False))


# ==========================================================================
# 3. Cross-RQA: 3D speed for opposite hips
# ==========================================================================
# Euclidean norm of the velocity vector captures overall movement intensity
# regardless of direction, and works across all three spatial dimensions.


def marker_speed(df: pd.DataFrame, marker: str) -> np.ndarray:
    """Compute 3D speed (frame-to-frame Euclidean distance) for a marker."""
    vx = np.diff(df[f"{marker}_x"].values)
    vy = np.diff(df[f"{marker}_y"].values)
    vz = np.diff(df[f"{marker}_z"].values)
    return np.sqrt(vx**2 + vy**2 + vz**2)


follow_lhip_speed = marker_speed(cleaned, "Follow_left_hip")
lead_rhip_speed = marker_speed(cleaned, "Lead_right_hip")

cross_3d = pd.DataFrame(
    {
        "follow_lhip_speed": follow_lhip_speed,
        "lead_rhip_speed": lead_rhip_speed,
    }
)

cross_3d_result = cross_pipeline.run(x=cross_3d, col_a=0, col_b=1, threshold=0.1)
print("\n3) Cross-RQA: Follower left hip vs Leader right hip, 3D speed (threshold=0.1)")
print(cross_3d_result.to_string(index=False))


# ==========================================================================
# 4. Cross-RQA: both hip sides averaged
# ==========================================================================
# Average the left and right hip speeds per person to get a single
# bilateral hip movement signal, reducing noise from asymmetric steps.

follow_hip_speed = (marker_speed(cleaned, "Follow_left_hip") + marker_speed(cleaned, "Follow_right_hip")) / 2
lead_hip_speed = (marker_speed(cleaned, "Lead_left_hip") + marker_speed(cleaned, "Lead_right_hip")) / 2

cross_bilateral = pd.DataFrame(
    {
        "follow_hip_speed": follow_hip_speed,
        "lead_hip_speed": lead_hip_speed,
    }
)

cross_bilateral_result = cross_pipeline.run(x=cross_bilateral, col_a=0, col_b=1, threshold=0.1)
print("\n4) Cross-RQA: Follower vs Leader bilateral hip speed (threshold=0.1)")
print(cross_bilateral_result.to_string(index=False))


# ==========================================================================
# 5. Windowed Cross-RQA: coordination over time
# ==========================================================================
# Track how leader-follower coordination evolves across the trial.
windowed_pipeline = Pipeline([WindowedCrossRQAStats("windowed_cross_rqa")])
windowed_result = windowed_pipeline.run(
    x=cross_bilateral,
    col_a=0,
    col_b=1,
    threshold=0.1,
    window=10,
    step=5,
)
print("\n5) Windowed Cross-RQA: bilateral hip speed (window=10, step=5)")
print(f"   {len(windowed_result)} windows:")
for i, row in windowed_result.iterrows():
    print(f"   Window {i}: RR={row['recurrence_rate']:.4f}, DET={row['determinism']:.4f}")


# ==========================================================================
# 6. Cross-RQA: vertical hip displacement ("bounce")
# ==========================================================================
# During dancing, the vertical (z-axis) hip movement shows a rhythmic bounce.
# By subtracting the initial position we get displacement from start (delta),
# which is comparable across dancers regardless of their height or room position.

follow_lhip_z = cleaned["Follow_left_hip_z"].values
lead_rhip_z = cleaned["Lead_right_hip_z"].values

# Displacement from initial position (assume start at 0)
follow_lhip_dz = follow_lhip_z - follow_lhip_z[0]
lead_rhip_dz = lead_rhip_z - lead_rhip_z[0]

bounce_df = pd.DataFrame(
    {
        "follow_lhip_dz": follow_lhip_dz,
        "lead_rhip_dz": lead_rhip_dz,
    }
)

# Auto-RQA on follower's vertical bounce
auto_bounce = rqa_pipeline.run(
    x=pd.Series(follow_lhip_dz, name="follow_lhip_dz"),
    dim=1,
    tau=1,
    threshold=0.2,
)
print("\n6a) Auto-RQA: Follower left hip vertical displacement (threshold=0.2)")
print(auto_bounce.to_string(index=False))

# Cross-RQA: compare the bounce between dancers
cross_bounce_result = cross_pipeline.run(x=bounce_df, col_a=0, col_b=1, threshold=0.2)
print("\n6b) Cross-RQA: Follower vs Leader vertical hip displacement (threshold=0.2)")
print(cross_bounce_result.to_string(index=False))

print("\nDone!")
