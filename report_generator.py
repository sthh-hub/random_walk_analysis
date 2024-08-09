import os
import json
import networkx as nx

# Directory paths
ORIGINAL_GRAPH_DIR = './graph'
SAMPLED_GRAPH_DIRS = ['./sampled_graph_BFS', './sampled_graph_RW', './sampled_graph_RWF']
REPORT_DIR = './'
SUMMARY_REPORT_FILE = os.path.join(REPORT_DIR, 'summary_report.txt')
os.makedirs(REPORT_DIR, exist_ok=True)

# Function to load graph from JSON file
def load_graph_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    graph = nx.Graph()
    for node, neighbors in data.items():
        for neighbor in neighbors:
            graph.add_edge(int(node), int(neighbor))
    return graph

# Function to generate report for the sampled graph
def generate_report(graph, sampled_graph, walk):
    report = {}
    report['Number of Nodes Visited'] = len(sampled_graph.nodes)
    report['Average Degree'] = round(sum(dict(sampled_graph.degree()).values()) / len(sampled_graph.nodes), 2)
    report['Max Degree'] = max(dict(sampled_graph.degree()).values())
    
    # Clustering coefficient
    report['Average Clustering Coefficient'] = round(nx.average_clustering(sampled_graph), 2)
    report['Diameter'] = nx.diameter(sampled_graph) if nx.is_connected(sampled_graph) else "N/A"
    report['Average Shortest Path Length'] = round(nx.average_shortest_path_length(sampled_graph), 2) if nx.is_connected(sampled_graph) else "N/A"
    report['Number of Triangles'] = sum(nx.triangles(sampled_graph).values()) // 3

    return report

# Function to format report as a table
def format_table(reports):
    headers = ["Graph", "Walk Type", "Number of Nodes Visited", "Average Degree", "Max Degree", "Average Clustering Coefficient", "Diameter", "Average Shortest Path Length", "Number of Triangles"]
    table = [headers]
    
    for report in reports:
        row = [
            report['Graph'],
            report['Walk Type'],
            report['Number of Nodes Visited'],
            report['Average Degree'],
            report['Max Degree'],
            report['Average Clustering Coefficient'],
            report['Diameter'] if report['Diameter'] is not None else "N/A",
            report['Average Shortest Path Length'] if report['Average Shortest Path Length'] is not None else "N/A",
            report['Number of Triangles']
        ]
        table.append(row)
    
    # Find max length of each column
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*table)]
    
    # Create format string
    format_str = " | ".join([f"{{:<{w}}}" for w in col_widths])
    
    # Format table
    formatted_table = [format_str.format(*row) for row in table]
    formatted_table = "\n".join(formatted_table)
    
    return formatted_table

# Generate summary report for all sampled graphs
all_reports = []

with open(SUMMARY_REPORT_FILE, 'w') as summary_file:
    for sampled_graph_dir in SAMPLED_GRAPH_DIRS:
        walk_type = sampled_graph_dir.split('_')[-1]
        for file_name in os.listdir(sampled_graph_dir):
            if file_name.endswith('.json'):
                sampled_graph_path = os.path.join(sampled_graph_dir, file_name)
                original_graph_path = os.path.join(ORIGINAL_GRAPH_DIR, file_name)

                if not os.path.exists(original_graph_path):
                    print(f"Original graph for {file_name} not found, skipping.")
                    continue

                original_graph = load_graph_from_json(original_graph_path)
                sampled_graph = load_graph_from_json(sampled_graph_path)

                # Assume walk can be reconstructed from sampled graph's adjacency list
                walk = list(sampled_graph.nodes)

                # Generate report
                report = generate_report(original_graph, sampled_graph, walk)
                report['Graph'] = os.path.splitext(file_name)[0]
                report['Walk Type'] = walk_type
                
                all_reports.append(report)
                
                # Write individual report to summary file
                summary_file.write(f"Report for {file_name} (Walk Type: {walk_type}):\n")
                for key, value in report.items():
                    summary_file.write(f"{key}: {value}\n")
                summary_file.write("\n")

    # Write summary table to summary file
    summary_file.write("Summary Table:\n")
    summary_table = format_table(all_reports)
    summary_file.write(summary_table)
    summary_file.write("\n")

print(f"Reports and summary have been saved in the directory: {REPORT_DIR}")