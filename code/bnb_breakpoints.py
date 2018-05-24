#   dfs_breakpoint.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
import numpy as np
# import itertools
import heapq
import copy

def dfs_upperbound(root_genome):
    """ Depth-First Search (dfs) Random.

    This algorithm searches for the best path to the solution genome
    (integers ordered from low to high). The path consists of swaps between
    genes of the genome.
    From the root genome every possible swap is generated: children. Then the children
    are being compard with the solution. When in this generation the solution exist the
    upperbound is updated.

        Args:
            root: genome sequence of fruitfly provided by user.
    """

    print("Branch and bound with breakpoints")

    stack = []
    # archive = {}
    current_layer = root_genome.get_generation()
    upperbound = len(root_genome) - 1

    solution = root_genome.solution()
    # archive[str(root_genome)] = "parent"
    stack.append(root_genome)

    # solved = False

    while stack:
        genome = stack.pop()
        genome_generation = genome.get_generation()

        # print("New Genome")
        if genome_generation < upperbound:
            children = genome.create_children(Fruitfly.breakpoint_compare)

            smallest_children = heapq.nsmallest(2, children)
            # best = copy.copy(children[0])
            # second_best = copy.copy(children[1])
            #
            # for a, b in itertools.combinations(children, 2):
            #     if a < b and a < best:
            #         best = copy.copy(a)
            # print("best child: ", best)
            # for child in children:
            #     if child < best:
            #         best = copy.copy(child)
            #     elif best < child < second_best:
            #         second_best = child

            # print(smallest_children)

            for child in smallest_children:
                if child.get_generation() < upperbound:
                    if child != solution:
                        # if not str(child) in archive.keys():
                        # print("breakpoints: ", child.breakpoint)
                        stack.append(child)
                            # current_layer = child.get_generation()
                            # value = "layer:" + str(current_layer)
                            # archive[str(child.get_genes())] = value
                    else:
                        # solved = True
                        upperbound = child.get_generation()
                        path = child.path_solution()
                        path_length = child.path_length()
                        print("solution found: {}, in layer {}, path: {}, swaps: {}".format(child, upperbound, path, path_length))
