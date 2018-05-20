#   bfs_breakpoint.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Breadth-first search, pruning with breakpoints.

from .classes.Fruitfly import Fruitfly

def bfs(root_genome):
    """ Breadth-First Search (bfs): using breakpoints.

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

        children = genome.create_children()
        for child in children:
            if child == solution:
                solved = True
                solution_child = child
            else:
                queue.append(child)

    print("Breadth-First Search (breakpoint)")
    print("genome fruitfly:", root_genome)
    print("solution child:", solution_child)
    print("solution found in generation:", solution_child.get_generation())
    print("path to solution:", solution_child.path_solution())