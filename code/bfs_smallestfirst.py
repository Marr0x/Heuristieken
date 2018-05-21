#   bfs_breakpoint.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Breadth-first search, pruning with breakpoints.

from .classes.Fruitfly import Fruitfly

def bfs(root_genome):
    """ Breadth-First Search (bfs): selects smallest

        Args:
            root: genome sequence of fruitfly provided by user.
            
    """

    solution = root_genome.solution()
    solved = False
    generation = root_genome.generation
    upperbound = len(root_genome) - 1

    print("Breadth-First Search (smallest first)")
    print("genome fruitfly:", root_genome)

    queue = []
    breakpoints_list = []

    # add start node to queue
    queue.append(root_genome)

    #loop until you find goal node
    while not solved and generation < upperbound:

        # get current node: node with smallest value
        minimum_index = queue.index(min(queue))
        genome = queue.pop(minimum_index)

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
            queue.append(child)
            generation = child.get_generation()
