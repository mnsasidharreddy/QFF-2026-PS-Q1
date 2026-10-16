"""Load and validate processor configuration JSON files."""
from __future__ import annotations
import json
from pathlib import Path
import networkx as nx

def load_processor_config(path):
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        config = json.load(f)
    required = {"name", "num_qubits", "coupling_map"}
    missing = required - config.keys()
    if missing:
        raise ValueError(f"{path} is missing required keys: {sorted(missing)}")
    n = int(config["num_qubits"])
    edges = config["coupling_map"]
    for edge in edges:
        if len(edge) != 2 or any(not isinstance(q, int) or q < 0 or q >= n for q in edge):
            raise ValueError(f"Invalid coupling edge {edge!r} for {n} qubits")
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(tuple(edge) for edge in edges)
    config["graph"] = graph
    return config
