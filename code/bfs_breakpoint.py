#   bfs_breakpoint.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Best-first search with breakpoints.

from .classes.Fruitfly import Fruitfly
import heapq


def bfs(root_genome):
    """ Best-First Search (bfs): selects fruitflies genomes with least breakpoints.

        Args:
            root: genome sequence of fruitfly provided by user.

    """

    solution = root_genome.solution()
    solved = False

    print("Best-First Search (breakpoints)")
    print("genome fruitfly:", root_genome)

    queue = []
    breakpoints_list = []

    # add start node to queue
    queue.append(root_genome)

    #loop until you find goal node
    while not solved:

        # get current node: node with least breakpoints
        genome = heapq.heappop(queue)

        # found the goal
        if genome == solution:
            solved = True
            solution_child = genome
            print("solution child:", solution_child)
            print("solution found in generation:", solution_child.get_generation())
            print("path to solution:", solution_child.path_solution())

        # generate children
        children = genome.create_children()

        for child in children:
            heapq.heappush(queue, child)
            # print(queue)
            generation = child.get_generation()
