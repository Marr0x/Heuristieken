#   bfs_basic.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Basic breadth-first search algorithm.

from .classes.Fruitfly import Fruitfly


def bfs(root_genome):
    """ Breadth-First Search (bfs): the foundation.

        Args:
            root: genome sequence of fruitfly provided by user.

    """

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

    print("Breadth-First Search (basic)")
    print("genome fruitfly:", root_genome)
    print("solution child:", solution_child)
    print("solution found in generation:", solution_child.get_generation())
    print("path to solution:", solution_child.path_solution())