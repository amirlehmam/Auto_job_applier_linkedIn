import pygraphviz as pgv
import matplotlib.pyplot as plt
from PIL import Image

# Create a new directed graph using PyGraphviz
graph = pgv.AGraph(directed=True, strict=False, rankdir="LR")

# Define nodes with their labels and groups for coloring
nodes = {
    "DB1": {"label": "Base de données\nPrix d'achat", "group": "Data Sources"},
    "DB2": {"label": "Base de données\nPrix de vente", "group": "Data Sources"},
    "DB3": {"label": "Base de données\nVolume de ventes", "group": "Data Sources"},
    "PA_Interface": {"label": "Power Apps\nInterface Utilisateur", "group": "Power Apps"},
    "PA_Filter": {"label": "Power Apps\nSélection des Références", "group": "Power Apps"},
    "PA_Extraction": {"label": "Power Automate\nRappel d'utilisation", "group": "Power Automate"},
    "PA_Consolidation": {"label": "Power Automate\nAlerte nouvelle référence produit", "group": "Power Automate"},
    "BI_Dashboard": {"label": "Power BI\nMarge moyenne par fournisseur", "group": "Power BI"},
    "BI_Comparison": {"label": "Power BI\nMarge totale par fournisseur", "group": "Power BI"},
    "BI_Alerts": {"label": "Power BI\nMarge minimale", "group": "Power BI"},
    "ROI_Input": {"label": "ROI : Réduction des coûts\net gain de temps", "group": "ROI"}
}

# Define edges between nodes
edges = [
    ("DB1", "PA_Interface"), ("DB2", "PA_Interface"), ("DB3", "PA_Interface"),
    ("PA_Interface", "PA_Filter"),
    ("PA_Filter", "PA_Extraction"),
    ("PA_Extraction", "PA_Consolidation"),
    ("PA_Consolidation", "BI_Dashboard"),
    ("BI_Dashboard", "BI_Comparison"), ("BI_Dashboard", "BI_Alerts"),
    ("BI_Dashboard", "ROI_Input"), ("BI_Comparison", "ROI_Input"), ("BI_Alerts", "ROI_Input")
]

# Define colors for each group
colors = {
    "Data Sources": "#A8DADC",
    "Power Apps": "#FFC857",
    "Power Automate": "#457B9D",
    "Power BI": "#A788E4",
    "ROI": "#F4A261"
}

# Add nodes to the graph with colors and labels
for node, attributes in nodes.items():
    graph.add_node(node, label=attributes["label"], style="filled", fillcolor=colors[attributes["group"]],
                   shape="box", fontname="Arial", fontsize="10")

# Add edges to the graph
for start, end in edges:
    graph.add_edge(start, end, color="#333333", arrowsize="0.8")

# Render the graph to a PNG image file
output_file = "/mnt/data/workflow_diagram_pygraphviz.png"
graph.layout(prog="dot")
graph.draw(output_file)

# Display the graph using Matplotlib
img = Image.open(output_file)
plt.figure(figsize=(12, 8))
plt.imshow(img)
plt.axis("off")
plt.show()
