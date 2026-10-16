"""Plot processor coupling graphs and benchmark comparisons."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx

def plot_coupling_graph(graph, title, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pos = nx.spring_layout(graph, seed=7)
    plt.figure(figsize=(6, 4))
    nx.draw_networkx(graph, pos=pos, with_labels=True, node_size=700)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()

def plot_metric_comparison(rows, metric, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    names = [row["processor"] for row in rows]
    values = [row[metric] for row in rows]
    plt.figure(figsize=(6, 4))
    plt.bar(names, values)
    plt.ylabel(metric)
    plt.title(f"Processor comparison: {metric}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()
