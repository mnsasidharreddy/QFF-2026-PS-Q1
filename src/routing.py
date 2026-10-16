"""Circuit transpilation helpers for Processor A/B."""
from __future__ import annotations

def transpile_for_processor(circuit, config, optimization_level=1, seed_transpiler=7):
    """Transpile a Qiskit circuit to the configured coupling map.

    The config must be verified against the actual project specification first.
    """
    from qiskit import transpile
    return transpile(
        circuit,
        basis_gates=config.get("basis_gates") or None,
        coupling_map=config["coupling_map"],
        optimization_level=optimization_level,
        seed_transpiler=seed_transpiler,
    )
