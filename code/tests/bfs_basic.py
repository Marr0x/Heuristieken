#   bfs_basic.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Basic breadth-first search algorithm.

from .classes.Fruitflytest import Fruitflytest
import timeit


def bfs(root_genome):
    """ Breadth-First Search (bfs): the foundation.

        Args:
            root: genome sequence of fruitfly provided by user.

    """

    start_runtime = timeit.default_timer()

    solution = root_genome.solution()
    solved = False
    generation = 0
    upperbound = len(root_genome) - 1

    queue = [root_genome]

    # create children from root genome until a solution found
    while not solved and generation < upperbound:

        genome = queue.pop(0)

        if genome == solution:
            solved = True
            solution_child = genome

        children = genome.create_children()

        for child in children:
                queue.append(child)

    print("\nBreadth-First Search")
    print("Genome fruitfly:", root_genome)
    print("Solution found in generation:", solution_child.get_generation())

    path = solution_child.path_solution()
    print("Path to solution: ")
    for inversion in range(len(path)):
                print("Inversion: {:2d}".format(inversion), path[inversion])

    end_runtime = timeit.default_timer()
    runtime = (end_runtime - start_runtime)
    print("Runtime: ", runtime)

    return solution_child.get_generation()