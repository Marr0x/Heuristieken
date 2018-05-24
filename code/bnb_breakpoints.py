#   bnb_breakpoints.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793)&
#            Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
import numpy as np
import heapq
import timeit

def bnb(root_genome):
    """ Branch and Bound: breakpoints

    This algorithm searches for the best path to the solution genome
    (integers ordered from low to high). The path consists of swaps between
    genes of the genome.
    From the root genome every possible swap is generated: children. Then the
    children are compard with the solution. When in this generation the solution
    exist the upperbound is updated.

        Args:
            root: genome sequence of fruitfly provided by user.
    """
    start_runtime = timeit.default_timer()

    print("Branch and Bound: breakpoints")

    stack = []
    stack.append(root_genome)

    current_layer = root_genome.get_generation()

    # upperbound found in smallest first algorithm
    upperbound = len(root_genome) - 1

    solution = root_genome.solution()

    while stack:
        genome = stack.pop()
        genome_generation = genome.get_generation()

        if genome_generation < upperbound:
            children = genome.create_children(Fruitfly.breakpoint_compare)

            # select 2 children with the smallest breakpoints
            smallest_children = heapq.nsmallest(4, children)

            # Check generation of child and check if the child is the solution
            for child in smallest_children:
                if child.get_generation() < upperbound:
                    if child != solution:
                        stack.append(child)
                    else:
                        upperbound = child.get_generation()
                        path = child.path_solution()
                        path_length = child.path_length()
                        print("Solution found in generation: {}, but still"
                        " searching for a better solution".format(upperbound))

    print("\nBest solution found in generation: ", upperbound)
    print("Path to solution: ")
    for swap in range(len(path)):
        print("swap: {:2d}".format(swap), path[swap])
    print("")

    end_runtime = timeit.default_timer()

    runtime = (end_runtime - start_runtime)
    print("runtime: ", runtime)
