import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_edge(3, 1)
G.add_node(4)
G.add_edge(4,1)
G.add_weighted_edges_from([(4,2,5),(3,4,6)])

plt.plot()
nx.draw(G, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
