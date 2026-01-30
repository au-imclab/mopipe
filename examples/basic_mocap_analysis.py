"""Example: Basic motion capture analysis workflow.

This example demonstrates how to:
    1. Load QTM TSV motion capture data
    2. Create an experiment structure
    3. Build and run an analysis pipeline
    4. Run the pipeline via the experiment structure
"""

from pathlib import Path

from mopipe.core.analysis import Pipeline
from mopipe.core.data import Experiment, MocapReader, Trial
from mopipe.segment import ColMeans, SimpleGapFilling

# --- Load data ---
data_path = Path("tests/fixtures/sample_dance_with_header.tsv")
reader = MocapReader(source=data_path, name="dance_trial")
data = reader.read()

print(f"Loaded data: {data.name}")
print(f"  Shape: {data.data.shape}")
print(f"  Columns: {list(data.data.columns[:5])}...")
print(f"  Metadata keys: {list(data.metadata.keys())}")

# --- Create experiment structure ---
experiment = Experiment("mocap_study")
trial = Trial("trial_001")
trial.add_timeseries(data)
experiment.child = trial

print("\nExperiment structure:")
for level in experiment.descend():
    indent = "  " * level.depth
    print(f"{indent}{level.level_name} (depth={level.depth}, timeseries={len(level.timeseries)})")

# --- Build and run pipeline directly ---
pipeline = Pipeline(
    [
        SimpleGapFilling("fill_gaps"),
        ColMeans("marker_means"),
    ]
)

result_direct = pipeline.run(x=data.data)
print(f"\nDirect pipeline result shape: {result_direct.shape}")
print(f"First 5 values:\n{result_direct.head()}")

# --- Run pipeline via experiment structure ---
# Build a gap-filling-only pipeline to store back on the trial
gap_fill_pipeline = Pipeline(
    [
        SimpleGapFilling("fill_gaps"),
    ]
)

result = trial.run_pipeline(gap_fill_pipeline, result_name="cleaned_data")
print("\nPipeline via experiment:")
print(f"  Result name: {result.name}")
print(f"  Result shape: {result.data.shape}")
print(f"  Trial now has {len(trial.timeseries)} timeseries")

# Look up the stored result by name
found = trial.get_timeseries_by_name("cleaned_data")
print(f"  Found stored result by name: {found is not None}")

# --- Run pipeline on all descendants ---
results = experiment.run_pipeline_on_descendants(
    gap_fill_pipeline,
    data_name="dance_trial",
    result_name="cleaned",
)
print(f"\nRan pipeline on {len(results)} descendant level(s)")

print("\nDone!")
