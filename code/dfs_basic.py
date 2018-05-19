#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
from .classes.Stack import Stack

def dfs(root_genome):
    """ Depth-First Search (dfs): in progress. """

    print("Depth-First search")

    stack = Stack()
    archive = {}

    genome = root_genome
    solution = genome.solution()
    archive[str(genome)] = "parent"
    stack.push(genome)
    layer = 0

    while stack:
        child = stack.pop()
        layer += 1
        child_no = 0

        next_gen = genome.create_children()

        for child_gen in next_gen:
            if child_gen != solution:
                if not str(child_gen) in archive.keys():
                    stack.push(child_gen)
                    child_no += 1
                    value = "layer:" + str(layer) + "_" + str(child_no)
                    archive[str(child_gen)] = value
            else:
                print("solution found:", child_gen, layer)

    print("archive:",archive)
