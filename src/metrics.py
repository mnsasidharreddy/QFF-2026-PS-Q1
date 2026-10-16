"""Circuit metric extraction and benchmark table helpers."""
from __future__ import annotations

def circuit_metrics(circuit, processor_name):
    """Return transparent structural metrics; fidelity is not inferred from depth."""
    counts = circuit.count_ops()
    return {
        "processor": processor_name,
        "num_qubits": int(circuit.num_qubits),
        "depth": int(circuit.depth() or 0),
        "size": int(circuit.size() or 0),
        "cx_count": int(counts.get("cx", 0)),
        "swap_count": int(counts.get("swap", 0)),
        "operation_counts": {str(k): int(v) for k, v in counts.items()},
    }

def save_metrics_csv(rows, path):
    import pandas as pd
    pd.DataFrame(rows).to_csv(path, index=False)
