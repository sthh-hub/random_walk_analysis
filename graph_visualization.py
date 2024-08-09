import os
import json
import networkx as nx
import matplotlib.pyplot as plt

# Directory paths
original_graph_dir = './graph'
SAMPLED_GRAPH_DIR = './sampled_graph'
LAYOUT_DIR = './graph_layout'
os.makedirs(LAYOUT_DIR, exist_ok=True)


# Function to load graph from JSON file
def load_graph_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    graph = nx.Graph()
    for node, neighbors in data.items():
        for neighbor in neighbors:
            graph.add_edge(int(node), int(neighbor))
    return graph


# Function to save the layout of a graph
def save_layout(graph, layout, file_path):
    with open(file_path, 'w') as f:
        json.dump({node: pos.tolist() for node, pos in layout.items()}, f)


# Function to load the layout of a graph
def load_layout(file_path):
    with open(file_path, 'r') as f:
        layout_data = json.load(f)
    return {int(node): pos for node, pos in layout_data.items()}


# Function to ensure all nodes have positions in the layout
def ensure_layout_complete(graph, layout):
    for node in graph.nodes():
        if node not in layout:
            layout[node] = [0, 0]  # Assign a default position if missing
    return layout


# Function to visualize the original graph and sampled nodes
def visualize_graph(original_graph, sampled_nodes, layout, output_path):
    plt.figure(figsize=(12, 8))
    nx.draw(
        original_graph, layout, with_labels=True,
        node_color='lightblue', node_size=500, edge_color='gray')

    sampled_node_list = list(map(int, sampled_nodes))
    nx.draw_networkx_nodes(original_graph, layout, nodelist=sampled_node_list,
                           node_color='red', node_size=500)

    plt.title("Original Graph with Sampled Nodes")
    plt.savefig(output_path)
    plt.close()


# Function to visualize the original graph without sampling nodes
def visualize_original_graph(original_graph, layout, output_path):
    plt.figure(figsize=(12, 8))
    nx.draw(original_graph, layout, with_labels=True, node_color='lightblue',
            node_size=500, edge_color='gray')
    plt.title("Original Graph")
    plt.savefig(output_path)
    plt.close()


# Process each pair of original and sampled graph files
for file_name in os.listdir(original_graph_dir):
    if file_name.endswith('.json'):
        original_graph_path = os.path.join(original_graph_dir, file_name)
        layout_file_path = os.path.join(LAYOUT_DIR, file_name.replace(
            '.json', '_layout.json'))

        original_graph = load_graph_from_json(original_graph_path)

        # Check if layout exists, if not, create and save it
        if os.path.exists(layout_file_path):
            layout = load_layout(layout_file_path)
            layout = ensure_layout_complete(original_graph, layout)
        else:
            layout = nx.spring_layout(original_graph)
            save_layout(original_graph, layout, layout_file_path)

        # Save the original graph image
        original_graph_image_path = original_graph_path.replace(
            '.json', '.png')
        visualize_original_graph(original_graph, layout,
                                 original_graph_image_path)

        for walk_type in ['_RW', '_RWF', '_BFS']:
            sampled_graph_dir = SAMPLED_GRAPH_DIR + walk_type
            sampled_graph_path = os.path.join(sampled_graph_dir, file_name)

            if os.path.exists(sampled_graph_path):
                sampled_graph = load_graph_from_json(sampled_graph_path)
                sampled_nodes = sampled_graph.nodes()

                output_image_path = os.path.join(
                    sampled_graph_dir, file_name.replace('.json', '.png'))
                visualize_graph(original_graph, sampled_nodes,
                                layout, output_image_path)

print("Visualizations have been saved in the directories")
