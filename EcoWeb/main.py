import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

species = [
    "okrzemki",
    "larwy jętki",
    "larwy widelnic",
    "pstrąg potokowy",
    "strzebla potokowa",
    "saprotrofy",
    "detrytus",
    "nieorganiczne składniki odżywcze"
]

edges = [
    ("okrzemki", "larwy jętki"),
    ("okrzemki", "larwy widelnic"),
    ("larwy jętki", "larwy widelnic"),
    ("larwy jętki", "strzebla potokowa"),
    ("larwy widelnic", "strzebla potokowa"),
    ("larwy jętki", "pstrąg potokowy"),
    ("larwy widelnic", "pstrąg potokowy"),
    ("strzebla potokowa", "pstrąg potokowy"),
    ("pstrąg potokowy", "pstrąg potokowy"),
    ("okrzemki", "detrytus"),
    ("larwy jętki", "detrytus"),
    ("larwy widelnic", "detrytus"),
    ("strzebla potokowa", "detrytus"),
    ("pstrąg potokowy", "detrytus"),
    ("detrytus", "saprotrofy"),
    ("saprotrofy", "nieorganiczne składniki odżywcze"),
    ("nieorganiczne składniki odżywcze", "okrzemki")
]
G.add_nodes_from(species)
G.add_edges_from(edges)


print("\nDegree Centrality:")
for node in G.nodes():
    print(f"{node}: in={G.in_degree(node)}, out={G.out_degree(node)}")

print("\nBetweenness Centrality:")
bet = nx.betweenness_centrality(G)
for node, val in bet.items():
    print(f"{node}: {val:.3f}")

print("\nEigenvector Centrality:")
try:
    eig = nx.eigenvector_centrality(G)
    for node, val in eig.items():
        print(f"{node}: {val:.3f}")
except nx.NetworkXException as e:
    print(f"Error: {e}")

print("\nSilnie spójne komponenty:")
scc = list(nx.strongly_connected_components(G))
for i, comp in enumerate(scc):
    print(f"Component {i + 1}: {comp}")

print("\nSymulacja usunięcia:")
G_removed = G.copy()
G_removed.remove_node("okrzemki")

print("Pozostałe węzły:", list(G_removed.nodes))
print("Nowe komponenty silnie spójne:")
new_scc = list(nx.strongly_connected_components(G_removed))
for i, comp in enumerate(new_scc):
    print(f"Component {i + 1}: {comp}")


def draw_graph(graph, title):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color="lightgreen", node_size=2000, font_size=10, arrowsize=20)
    plt.title(title)
    plt.show()


draw_graph(G, "Oryginal")
draw_graph(G_removed, "Missing animal")
