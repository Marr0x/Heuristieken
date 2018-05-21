#   bfs_breakpoint.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Breadth-first search, pruning with breakpoints.

from .classes.Fruitfly import Fruitfly
from heapq import nsmallest

def bfs(root_genome):
    """ Breadth-First Search (bfs): using breakpoints.
        
        Comment:
            Still in progress! Ik push nu alleen de child met de minste
            breakingpoints in closed_list. Bedoeling is om uiteindelijk
            meerdere children met lage breakpoints erin te pushen.

        Args:
            root: genome sequence of fruitfly provided by user.
            
    """

    solution = root_genome.solution()
    solved = False
    generation = root_genome.generation
    upperbound = len(root_genome) - 1

    print("Breadth-First Search (breakpoint)")
    print("genome fruitfly:", root_genome)

    # initialize open and closed list
    open_list = []
    closed_list = []
    breakpoints_list = []

    # add start node
    open_list.append(root_genome)

    #loop until you find the end
    while not solved and generation < upperbound:

        # get current node: node with least f-value
        minimum_index = open_list.index(min(open_list))
        # min_children = nsmallest(3, open_list)

        # for min_child in min_children:
        #     print(min_children.index(min_child))
        genome = open_list.pop(minimum_index)
        closed_list.append(genome)
        breakpoints_list.append(genome.breakpoints())

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
            open_list.append(child)

    # dit laat zien hoe breakpoints minder worden (Later verwijderen!!)
    print("breakpoint_list:", breakpoints_list)
