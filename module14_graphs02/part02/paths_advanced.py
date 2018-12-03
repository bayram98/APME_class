

import networkx as nx
from datetime import datetime, date, time

# import some functions to show graphs from last week
from module13_graphs01.part01_basics.graphs_basics import print_graph, display_and_save

def graph_with_gmaps_travel_info(routemap):
    """
    This function takes as input a "routemap", i.e., a a list of tuples (origin, destination) (see exercises of
    last week) and returns a graph in which:
    - nodes are the destinations in the routemap
    - an edge is drawn if two destinations are connected, i.e., if a tuple exists in routemap connecting them
    - each edge is labelled with information about the duration of travelling between two connected nodes using a car
    ("driving") and a bicycle ("bicycling"). This information must be captured in real time using the Google Maps API.

    Assume the routemap can only contain cities in the USA as destinations

    TWIST: How much longer does is take on average to cycle as compared to driving among the destinations in routemap?
    """



if __name__ == '__main__':
    # use this simple routemap to test!
    rm_simple = [('Austin',"San Antonio"), ("San Antonio", "Houston"), ("Houston", "Austin"), ("Houston", "Dallas")]

    G = graph_with_gmaps_travel_info(rm_simple)
    print_graph(G)

    routemap = [('St. Louis', 'Miami'), ('St. Louis', 'San Diego'), ('St. Louis', 'Chicago'), ('San Diego', 'Chicago'),
                ('San Diego', 'San Francisco'), ('San Diego', 'Minneapolis'), ('San Diego', 'Boston'),
                ('San Diego', 'Portland'), ('San Diego', 'Seattle'), ('Tulsa', 'New York'), ('Tulsa', 'Dallas'),
                ('Phoenix', 'Cleveland'), ('Phoenix', 'Denver'), ('Phoenix', 'Dallas'), ('Chicago', 'New York'),
                ('Chicago', 'Los Angeles'), ('Miami', 'New York'), ('Miami', 'Philadelphia'), ('Miami', 'Denver'),
                ('Boston', 'Atlanta'), ('Dallas', 'Cleveland'), ('Dallas', 'Albuquerque'), ('Philadelphia', 'Atlanta'),
                ('Denver', 'Minneapolis'), ('Denver', 'Cleveland'), ('Albuquerque', 'Atlanta'),
                ('Minneapolis', 'Portland'), ('Los Angeles', 'Seattle'), ('San Francisco', 'Portland'),
                ('San Francisco', 'Seattle'), ('San Francisco', 'Cleveland'), ('Seattle', 'Portland')]

