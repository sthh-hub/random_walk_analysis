# Random Walk with Flyback Probability

## Project Overview

This project implements a **Random Walk with Flyback Probability** algorithm, designed to improve traditional random walks by introducing a probability of returning to the starting node. This enhancement helps address some limitations of the traditional random walk, such as getting trapped in loops or biased sampling toward high-degree nodes. The goal is to achieve more balanced and representative sampling in large graphs. The project also compares the performance of this method with other algorithms, such as the traditional Random Walk (RW) and Breadth-First Search (BFS).

## Demo
<img width="675" alt="image" src="https://github.com/user-attachments/assets/202cd03f-8ea0-4e2f-9533-1ebdc61c60a8">



## Project Structure

- **graph/** - Contains scripts and data related to graph creation and management.
- **graph_layout/** - Contains scripts for visualizing graph layouts.
- **sampled_graph_BFS/** - Stores the sampled graphs generated using the Breadth-First Search (BFS) algorithm.
- **sampled_graph_RW/** - Stores the sampled graphs generated using the traditional Random Walk (RW) algorithm.
- **sampled_graph_RWF/** - Stores the sampled graphs generated using the Random Walk with Flyback Probability (RWF) algorithm.
- **algorithm.py** - Contains the implementation of the Random Walk with Flyback Probability algorithm.
- **compute_theoretical_probabilities.py** - Computes the theoretical probabilities for different algorithms.
- **formatted_summary_report.csv** - A formatted summary of the report in CSV format.
- **graph_data_generator.py** - Script for generating graph data used in the project.
- **graph_visualization.py** - Script for visualizing the graphs and their sampled versions.
- **report_generator.py** - Generates reports summarizing the findings and analysis.
- **report_render.py** - Renders the generated reports into readable formats (e.g., PDF, HTML).
- **sampling.py** - Contains functions and utilities related to the sampling process.
- **summary_report_and_analysis.xlsx** - Excel file containing the summary report and analysis.
- **summary_report.csv** - CSV file containing the summary report.
- **summary_report.txt** - Text file containing the summary report.


## Usage

1. **Generate Graph Data:**

   Use the `graph_data_generator.py` script to create the necessary graph data:

   ```bash
   python graph_data_generator.py
   ```

2. **Run the Algorithms:**

   - To execute the Random Walk with Flyback Probability algorithm:

     ```bash
     python algorithm.py
     ```

   - To compute theoretical probabilities:

     ```bash
     python compute_theoretical_probabilities.py
     ```

3. **Visualize the Graphs:**

   Use the `graph_visualization.py` script to visualize the graphs and their sampled versions:

   ```bash
   python graph_visualization.py
   ```

4. **Generate and Render Reports:**

   - To generate the analysis report:

     ```bash
     python report_generator.py
     ```

   - To render the report into a readable format:

     ```bash
     python report_render.py
     ```

## Project Takeaways

This project provided a valuable learning experience in algorithm design, implementation, and data analysis. By comparing different sampling techniques, we gained insights into how flyback probability can enhance the performance of random walks in large graphs. The project also helped in improving coding skills, attention to detail, and understanding the practical applications of graph theory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to Prof. Aanchan for their guidance and support throughout this project.

