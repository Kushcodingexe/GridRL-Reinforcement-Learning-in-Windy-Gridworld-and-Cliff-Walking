import os
import gzip
import urllib.request
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import defaultdict

def download_facebook_combined(url="https://snap.stanford.edu/data/facebook_combined.txt.gz", dest_path="facebook_combined.txt.gz"):
    if not os.path.exists(dest_path):
        print("Downloading Facebook Combined dataset...")
        urllib.request.urlretrieve(url, dest_path)
        print("Download complete.")
    else:
        print("Dataset already downloaded.")
    return dest_path

def load_facebook_combined(file_path):
    print("Loading graph from dataset...")
    with gzip.open(file_path, 'rt') as f:
        G = nx.parse_edgelist(f, nodetype=int)
    G = nx.Graph(G)  # Ensure undirected
    print(f"Graph loaded with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G

class LabelPropagation:
    def __init__(self, G, max_iter=50):
        self.G = G
        self.max_iter = max_iter
        self.labels = {node: node for node in G.nodes()}
    
    def propagate_labels(self):
        for it in range(self.max_iter):
            nodes = list(self.G.nodes())
            random.shuffle(nodes)
            change = 0
            for node in nodes:
                neighbors = list(self.G.neighbors(node))
                if not neighbors:
                    continue
                
                neighbor_labels = [self.labels[neighbor] for neighbor in neighbors]
                most_common = max(set(neighbor_labels), key=neighbor_labels.count)
                
                if self.labels[node] != most_common:
                    self.labels[node] = most_common
                    change += 1
            
            print(f"Iteration {it+1}: {change} label changes")
            if change == 0:
                print("Convergence reached.")
                break
        return self.labels

def visualize_communities(G, labels):
    communities = defaultdict(list)
    for node, label in labels.items():
        communities[label].append(node)
    
    colors = plt.cm.rainbow(np.linspace(0, 1, len(communities)))
    node_color = {}
    for color, (comm, nodes) in zip(colors, communities.items()):
        for node in nodes:
            node_color[node] = color
    
    plt.figure(figsize=(10, 10))
    nx.draw(G, node_color=[node_color[node] for node in G.nodes()], node_size=30, with_labels=False)
    plt.title("Detected Communities in Facebook Network")
    plt.show()
    
    print("Detected Communities:")
    for label, nodes in communities.items():
        print(f"Community {label}: {nodes[:10]} ... ({len(nodes)} nodes)")

if __name__ == "__main__":
    dataset_path = download_facebook_combined()
    G = load_facebook_combined(dataset_path)
    
    lp = LabelPropagation(G, max_iter=50)
    final_labels = lp.propagate_labels()
    
    visualize_communities(G, final_labels)