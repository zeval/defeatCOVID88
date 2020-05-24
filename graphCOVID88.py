# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

import sys
from os import path
from SocialNetwork import SocialNetwork
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def showGraph(networkFile):
    """
    Creates visual representation of given social network.
    Requires: networkFile is a string representing the network
    file name. networkx and matplotlib modules are installed. 
    Ensures: an image with a graph representing all Person nodes,
    their immunity status and all connections between them.
    """

    G = nx.MultiDiGraph()
    colors = []
    socialNetwork = SocialNetwork(networkFile)
    for person in socialNetwork.itemsUsers():
        G.add_node(person)
        for person2, weight in socialNetwork.contactsOf(person):
            G.add_edge(person, person2)

    pos = nx.spring_layout(G, k=0.5)  # positions for all nodes
    for person in G:
        if person.getImmune():
            colors.append('lightblue')
        else:
            colors.append('lightgreen')

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color=colors)

    # edges
    nx.draw_networkx_edges(G, pos, width=2)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    # Legend
    lightBlue = Line2D([0], [0], marker='o', color='w', label='Circle', markerfacecolor='lightblue', markersize=15)
    lightGreen = Line2D([0], [0], marker='o', color='w', label='Circle', markerfacecolor='lightgreen', markersize=15)
    
    plt.legend(handles=(lightBlue, lightGreen), labels=('Immune', 'Not Immune'))

    plt.savefig("graphTestSet.png")  # save as png
    plt.show()  # display


try:
    # Checks if both required modules are installed.
    import networkx as nx
    import matplotlib.pyplot as plt

    networkFileName = sys.argv[1]

    if not path.isfile(networkFileName):
        raise FileNotFoundError

    showGraph(networkFileName)

except FileNotFoundError:
    print("Error: File not found. Double-check your input and try again.")
except (ValueError, IndexError) as error:
    print("Error: You must specify the network file's name. Double-check your input and try again.")
except ImportError:
    print("Error: Both networkx and matplotlib packages are required.")
