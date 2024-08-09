import os
import json
import networkx as nx

INPUT_PATH = './graph'
OUTPUT_PATH = INPUT_PATH
NODES = 100
COMMUNITIES = int(NODES / 10)


def save_graph_as_json(graph, file_path):
    adj_list = {str(node): list(map(str, neighbors))
                for node, neighbors in graph.adjacency()}
    with open(file_path, 'w') as f:
        json.dump(adj_list, f, indent=4)


def generate_all_data():
    # 1. Random Graph
    G1 = nx.gnp_random_graph(NODES, 0.05)
    # G1 = nx.karate_club_graph()
    save_graph_as_json(G1, os.path.join(OUTPUT_PATH, '1_random_graph.json'))

    # 2. High Average Degree Graph
    G2 = nx.gnp_random_graph(NODES, 0.4)
    save_graph_as_json(G2, os.path.join(OUTPUT_PATH, '2_high_avg_degree.json'))

    # 3. Low Average Degree Graph
    G3 = nx.gnp_random_graph(NODES, 0.02)
    save_graph_as_json(G3, os.path.join(OUTPUT_PATH, '3_low_avg_degree.json'))

    # 4. Graph with Isolated Nodes
    G4 = nx.gnp_random_graph(NODES, 0.01)
    save_graph_as_json(G4, os.path.join(OUTPUT_PATH, '4_isolated_nodes.json'))

    # 5. Multi-level Star Graph
    r = 3  # Number of children per node
    h = 4  # Number of levels to maintain a larger structure
    G5 = nx.balanced_tree(r, h)
    save_graph_as_json(G5, os.path.join(OUTPUT_PATH, '5_star.json'))

    # 6. Community Graph
    sizes = [int(NODES / COMMUNITIES) for _ in range(COMMUNITIES)]
    p_in = 0.8
    p_out = 0.05
    probs = [[p_in if i == j else p_out for j in range(COMMUNITIES)] for i in range(COMMUNITIES)]
    G6 = nx.stochastic_block_model(sizes, probs)
    save_graph_as_json(G6, os.path.join(OUTPUT_PATH, '6_community.json'))

    # 7. Scale-Free Graph
    G7 = nx.barabasi_albert_graph(NODES, 2)
    save_graph_as_json(G7, os.path.join(OUTPUT_PATH, '7_scale_free.json'))

    # 8. Power Law Degree Graph
    G8 = nx.powerlaw_cluster_graph(NODES, 3, 0.1) 
    save_graph_as_json(G8, os.path.join(OUTPUT_PATH, '8_power_law_degree.json'))

    # 9. Random Graph with Cycles
    G9 = nx.gnp_random_graph(NODES, 0.1)
    while not nx.is_connected(G9):
        G9 = nx.gnp_random_graph(NODES, 0.1)
    save_graph_as_json(G9, os.path.join(OUTPUT_PATH, '9_cycles.json'))

    print(f"Graphs have been saved in the directory: {OUTPUT_PATH}")


def main():
    generate_all_data()


if __name__ == "__main__":
    main()
