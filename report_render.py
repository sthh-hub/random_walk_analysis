import csv

SUMMARY_REPORT_FILE = 'summary_report.txt'
SUMMARY_CSV_FILE = 'summary_report.csv'


def parse_summary_report(file_path):
    reports = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_report = {}
        for line in lines:
            if line.startswith("Report for"):
                if current_report:
                    reports.append(current_report)
                current_report = {'Graph': line.split(' ')[2], 'Walk Type': line.split(': ')[1].strip()}
            elif ': ' in line:
                parts = line.split(': ', 1)
                key = parts[0].strip()
                value = parts[1].strip()
                current_report[key] = value
        if current_report:
            reports.append(current_report)
    return reports


def format_table(reports):
    headers = ["Graph", "Indicator", "RW", "RWF", "BFS"]
    table = [headers]
    
    data_dict = {}
    
    for report in reports:
        graph = report['Graph']
        walk_type = report['Walk Type']
        for key, value in report.items():
            if key not in ['Graph', 'Walk Type']:
                if (graph, key) not in data_dict:
                    data_dict[(graph, key)] = {}
                data_dict[(graph, key)][walk_type] = value
    
    for (graph, key), values in data_dict.items():
        row = [
            graph,
            key,
            values.get('RW', 'N/A'),
            values.get('RWF', 'N/A'),
            values.get('BFS', 'N/A')
        ]
        table.append(row)
    
    return table


def write_csv(table, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in table:
            csvwriter.writerow(row)

# Parse summary report
reports = parse_summary_report(SUMMARY_REPORT_FILE)

# Format table
summary_table = format_table(reports)

# Write summary table to CSV file
write_csv(summary_table, SUMMARY_CSV_FILE)

print(f"Summary table has been saved to {SUMMARY_CSV_FILE}")