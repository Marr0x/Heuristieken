#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
# from .classes.Stack import Stack

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

        for child in children:
            if child_gen != solution:
                if not str(child) in archive.keys():
                    stack.push(child)
                    layer = child.get_generation
                    value = "layer:" + str(layer)
                    archive[str(child] = value
            else:
                print("solution found:", child, layer)

    print("archive:",archive)
