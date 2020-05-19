# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


import sys
from os import path
from SocialNetwork import SocialNetwork
import networkx as nx
import matplotlib.pyplot as plt


def showGraph(networkFile):

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
    nx.draw_networkx_edges(G, pos, width=2, label="yeetyeetyeet")

    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    plt.savefig("graphTestSet.png")  # save as png
    plt.show()  # display


try:
    networkFileName = sys.argv[1]

    if not path.isfile(networkFileName):
        raise FileNotFoundError

    showGraph(networkFileName)

except FileNotFoundError:
    print("Error: File not found. Double-check your input and try again.")
except ValueError as error:
    print("Error: " + str(error))
except AssertionError as error:
    print("Error: " + str(error))
