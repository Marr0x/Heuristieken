#   astar.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   

from .classes.Fruitfly import Fruitfly
import heapq

def astar(root_genome):

    node_goal = root_genome.solution()
    open_list = []
    closed_list = []

    open_list.append(root_genome)

    while open_list:

        node_current = heapq.heappop(open_list)

        if node_current == node_goal:
            print("solution found:", node_current)
            break;

        node_successor = node_current.create_children()

        if node_successor in open_list:
            if node_successor.generation <= node_succes 







