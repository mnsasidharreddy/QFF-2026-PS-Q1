"""Problem formulation helpers for the biomedical signal classifier."""
from __future__ import annotations

def validate_features(features):
    """Validate a 2-D numeric feature matrix (samples x features)."""
    import numpy as np
    array = np.asarray(features, dtype=float)
    if array.ndim != 2:
        raise ValueError("features must be a 2-D array: samples x features")
    if array.shape[0] < 1 or array.shape[1] < 1:
        raise ValueError("features must contain at least one sample and one feature")
    if not np.isfinite(array).all():
        raise ValueError("features contain NaN or infinite values")
    return array

def make_binary_labels(labels):
    """Map labels to integers; currently intended for a binary classification task."""
    import numpy as np
    y = np.asarray(labels).reshape(-1)
    unique = sorted(set(y.tolist()))
    if len(unique) != 2:
        raise ValueError(f"Expected exactly 2 classes; found {len(unique)}")
    mapping = {label: i for i, label in enumerate(unique)}
    return np.array([mapping[v] for v in y], dtype=int), mapping
