import networkx as nx
import matplotlib.pyplot as plt

def print_graph(G):
    """
    This function is given and it allows to print on the console the list of nodes (with all atributes) and
    the list of edges (with all attributes) of a graph G
    :param G:
    :return:
    """
    print("Graph nodes: {0}".format(G.nodes(data=True)))
    print("Graph edges: {0}".format(G.edges(data=True)))

def display_and_save(G, file_name, layout = "fg"):
    """
    This function is given and allows you to (i) display a graph using matplotlib and (ii) save the graph
    is a png file named "file_name"
    :param G: the graph
    :param file_name: the name of the file, e.g. "graph" will save the image in a file named "graph.png"
    :param layout: the layout chosen to visualise the graph (default is  fruchterman_reingold_layout)
    """

    if layout == "spring":
       pos = nx.spring_layout(G)
    elif layout == "shell":
       pos = nx.shell_layout(G)
    elif layout == "spectral":
       pos = nx.spectral_layout(G)
    else:
       pos = nx.fruchterman_reingold_layout(G)

    # nodes
    nx.draw_networkx_nodes(G, pos,
                           nodelist=G.nodes(),
                           node_color='r',
                           node_size=500,
                           alpha=0.8)

    nx.draw_networkx_edges(G, pos,
                           edgelist=G.edges(),
                           width=2, alpha=0.5, edge_color='r')

    labels = {}
    i = 0
    for node in G.nodes():
        labels[node] = str(node)

    nx.draw_networkx_labels(G, pos, labels, font_size=16)

    plt.axis('off')
    plt.savefig(file_name + ".png")  # save as png
    plt.show()  # display

def make_simple_graph():
    """
    This functions returns the graph in Q1 of module 13 QUIZ.
    Once you complete the implementation of this function, you can use the main to visualise
    the graph using different layouts
    :return:
    """
    G = nx.Graph()
    G.add_edges_from([("B","D"),("D","E"), ("E", "C"), ("C", "A"), ("D", "A"), ("E", "A")])
    return G


def make_simple_cycle(N):
    """
    This function returns a simple cycle, that is, a graph with N nodes, where node n is connected to node n+1,
    except for the last node (N-1) which is connected to node 0
    Each node should be labelled using a progressive number n, with 0 <= n <= N-1
    :param N:
    :return:
    """
    G = nx.Graph()
    for i in range(0,N-1):
        G.add_edge(i,i+1)
    G.add_edge(N-1,0)

    return G


def make_complete_graph(N):
    """
    This function returns a "complete" graph, that is, a graph with N nodes where each node is connected
    to all other nodes. A complete graph does not have self-loops.
    Each node should be labelled using a progressive number n, with 0 <= n <= N-1
    You can "twist" this function by implementing the following feature:
     - the "weight" of each arc is the product of the lables of the nodes that it connects
    :param N:
    :return:
    """
    G = nx.Graph()
    for i in range(0, N ):
        for j in range(0, N):
            if i != j:
                G.add_edge(i, j)

    return G






if __name__ == '__main__':
    """
    You can use the given function print_graph() to print a graph in a better way
    You should also use the function display_and_save() to display the graphs using different layouts
    """
    G = make_simple_graph()
    print(G.nodes())
    print(G.edges())

    display_and_save(G,"graphG")

    G = make_simple_cycle(5)
    print(G.nodes())
    print(G.edges())

    display_and_save(G, "graphG")

    G = make_complete_graph(5)
    print(G.nodes())
    print(G.edges(data=True))
    display_and_save(G, "graphG")
