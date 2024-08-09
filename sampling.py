import os
import json
import random
import networkx as nx
from algorithm import random_walk, random_walk_with_flyback, unbiased_BFS

# Directory containing the graph JSON files
INPUT_DIR = './graph'
OUTPUT_DIR = './sampled_graph'
steps = 50
flyback_prob = 0.15
start_node = 0


# Function to load graph from JSON file
def load_graph_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    graph = nx.Graph()
    for node, neighbors in data.items():
        for neighbor in neighbors:
            graph.add_edge(int(node), int(neighbor))
    return graph


# Function to save sampled data as JSON
def save_sampled_data(sampled_data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(sampled_data, f, indent=4)


# Perform sampling on each graph using random walk
for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith('.json'):
        file_path = os.path.join(INPUT_DIR, file_name)
        graph = load_graph_from_json(file_path)

        # Check if node 0 exists in the graph
        if 0 not in graph.nodes:
            print(f"Node 0 not found in {file_name}, selecting a random start")
            start_node = random.choice(list(graph.nodes))

        # Perform random walk sampling
        for walk_type in ['RW', 'RWF', 'BFS']:
            if walk_type == 'RW':
                output_dir = OUTPUT_DIR + '_RW'
                walk = random_walk(graph, start_node, steps)
            elif walk_type == 'RWF':
                output_dir = OUTPUT_DIR + '_RWF'
                walk = random_walk_with_flyback(
                    graph, start_node, steps, flyback_prob)
            elif walk_type == 'BFS':
                output_dir = OUTPUT_DIR + '_BFS'
                walk = unbiased_BFS(graph, start_node, steps)

            # Convert walk to adjacency list format
            sampled_graph = {str(node): [] for node in walk}
            for i in range(len(walk) - 1):
                sampled_graph[str(walk[i])].append(walk[i + 1])
                sampled_graph[str(walk[i + 1])].append(walk[i])

            # Save sampled graph
            base_name = os.path.splitext(file_name)[0]
            output_file_name = f"{base_name}.json"
            output_file_path = os.path.join(output_dir, output_file_name)
            save_sampled_data(sampled_graph, output_file_path)

print(f"Sampled graphs have been saved in the directory")
