import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import json

def compute_theoretical_probabilities(graph, p):
    n = len(graph.nodes)
    transition_matrix = np.zeros((n, n))

    # Create the transition matrix
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        if neighbors:
            prob = (1 - p) / len(neighbors)
            for neighbor in neighbors:
                transition_matrix[node][neighbor] = prob
        transition_matrix[node][node] += p

    # Compute the stationary distribution
    eigenvalues, eigenvectors = np.linalg.eig(transition_matrix.T)
    stationary_vector = np.real(eigenvectors[:, np.isclose(eigenvalues, 1)])
    stationary_vector /= stationary_vector.sum()
    stationary_vector = stationary_vector.flatten()

    return stationary_vector

def load_graph_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    graph = nx.Graph()
    for node, neighbors in data.items():
        for neighbor in neighbors:
            graph.add_edge(int(node), int(neighbor))
    return graph

def load_layout(file_path):
    with open(file_path, 'r') as f:
        layout_data = json.load(f)
    return {int(node): pos for node, pos in layout_data.items()}

# Load the graph and layout
graph_path = './graph/1_random_graph.json'
layout_path = './graph_layout/1_random_graph_layout.json'
G = load_graph_from_json(graph_path)
pos = load_layout(layout_path)

# Parameters
flyback_probability = 0.15

# Compute theoretical visit probabilities
theoretical_probabilities = compute_theoretical_probabilities(G, flyback_probability)

# Compute distances from the start node
start_node = 0
distances = nx.shortest_path_length(G, source=start_node)

# Visualize the graph and the theoretical visit probabilities
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=8, font_color='black')

# Highlight the nodes based on theoretical visit probabilities
nodes = G.nodes()
node_colors = [theoretical_probabilities[node] for node in nodes]
nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=node_colors, node_size=500, cmap=plt.cm.viridis)
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
plt.colorbar(sm, label='Theoretical Visit Probability')

plt.title(f'Random Walk with Flyback (p={flyback_probability}) - Theoretical Visit Probabilities')
plt.show()

# Print theoretical visit probabilities and distances for each node
for node, prob in enumerate(theoretical_probabilities):
    print(f'Node {node}: Theoretical Visit Probability {prob:.4f}, Distance from Start Node {distances[node]}')

# Plot theoretical visit probabilities and distances
nodes = list(G.nodes())
probabilities = [theoretical_probabilities[node] for node in nodes if node != start_node]  # Exclude the start node
distances_list = [distances[node] for node in nodes if node != start_node]  # Exclude the start node

fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:blue'
ax1.set_xlabel('Nodes')
ax1.set_ylabel('Theoretical Visit Probability', color=color)
ax1.bar([node for node in nodes if node != start_node], probabilities, color=color, alpha=0.6, label='Theoretical Visit Probability')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Distance from Start Node', color=color)
ax2.plot([node for node in nodes if node != start_node], distances_list, color=color, marker='o', linestyle='-', label='Distance from Start Node')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
fig.suptitle('Comparison of Theoretical Visit Probability and Distance from Start Node', y=1.02)
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)
plt.show()