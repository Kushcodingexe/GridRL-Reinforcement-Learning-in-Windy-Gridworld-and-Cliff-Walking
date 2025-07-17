import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.cluster import average_clustering

# Load the graph dataset
# Assume the dataset is in a format compatible with NetworkX, e.g., edge list
graph = nx.read_edgelist("deezer_europe.edgelist", create_using=nx.Graph())

# Visualize the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(graph)  # Force-directed layout
nx.draw(
    graph,
    pos,
    node_size=20,
    node_color="blue",
    edge_color="gray",
    with_labels=False,
    alpha=0.7,
)
plt.title("Visualization of Deezer User Social Network")
plt.show()

# Calculate the required metrics
max_degree = max(dict(graph.degree()).values())
average_clustering_coefficient = average_clustering(graph)

print("Maximum Node Degree (Undirected):", max_degree)
print("Average Clustering Coefficient:", average_clustering_coefficient)
