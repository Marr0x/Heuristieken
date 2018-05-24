#  dfs_upperbound.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
import numpy as np

def dfs_upperbound(root_genome):
    """ Depth-First Search (dfs) Random.
    This algorithm takes a
        Args:
            root: genome sequence of fruitfly provided by user.
    """

    print("Depth-First search")

    stack = []
    archive = {}
    current_layer = root_genome.get_generation()
    upperbound = len(root_genome) - 1

    solution = root_genome.solution()
    archive[str(root_genome)] = "parent"
    stack.append(root_genome)

    while stack:
        genome = stack.pop()
        genome_generation = genome.get_generation()

        if genome_generation < upperbound:
            children = genome.create_children()

            np.random.shuffle(children)

            for child in children:
                if child != solution:
                    if not str(child) in archive.keys():
                        stack.append(child)
                        # current_layer = child.get_generation()
                        value = "layer:" + str(current_layer)
                        archive[str(child.get_genes())] = value

                else:
                    upperbound = child.get_generation()
                    path = child.path_solution()
                    path_length = child.path_length()
                    print("solution found: {}, in layer {}, path: {}, swaps: {}".format(child, upperbound, path, path_length))
