#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly

def dfs(root_genome):
    """ Depth-First Search (dfs): in progress. """

    print("Depth-First search")

    stack = []
    archive = {}

    solution = root_genome.solution()
    archive[str(root_genome)] = "parent"
    stack.append(root_genome)

    while stack:
        genome = stack.pop()

        children = genome.create_children()

        np.random.shuffle(children)

        for child in children:
            if child != solution:
                if not str(child) in archive.keys():
                    stack.append(child)
                    layer = child.get_generation()
                    value = "layer:" + str(layer)
                    archive[str(child.get_genes())] = value
            else:
                layer = child.get_generation()
                path = child.path_solution()
                path_length = child.path_length()
                print("solution found: {}, in layer {}, path: {}, swaps: {}".format(child, layer, path, path_length))

    # print("archive:",archive)
