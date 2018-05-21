#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
import numpy as np

def dfs_random(root_genome):
    """ Depth-First Search (dfs) Random.

        Args:
            root: genome sequence of fruitfly provided by user.
    """

    print("Depth-First search")

    stack = []
    archive = {}
    current_layer

    solution = root_genome.solution()
    archive[str(root_genome)] = "parent"
    stack.append(root_genome)

    while current_layer < upperbound:
        genome = stack.pop()
        # print("archive: {}".format(archive))
        children = genome.create_children()

        # print("children: {}".format(children))
        np.random.shuffle(children)

        ## TODO bijhouden welke laag. Eerste oplossing gevonden?
        for child in children:
            if child != solution:
                if not str(child) in archive.keys():
                    stack.append(child)
                    current_layer = child.get_generation()
                    value = "layer:" + str(current_layer)
                    archive[str(child.get_genes())] = value

            else:
                solution_layer = child.get_generation()
                path = child.path_solution()
                path_length = child.path_length()
                print("solution found: {}, in layer {}, path: {}, swaps: {}".format(child, solution_layer, path, path_length))

    # print("archive:",archive)
