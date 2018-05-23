#   best_first_search.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   Uses best-first search to find the series of mutations that changed
#   the genome of one fruitfly species to the other one. To select "the best"
#   fruitflychild it uses breakpoints, distancepoints or a combination of both.

from .classes.Fruitfly import Fruitfly
import heapq


def bfs(root_genome, compare_function=None):
    """ Best-First Search (bfs): Searches for series of mutations that changed
        the genome of one fruitfly species to the other one.

        Args:
            root_genome: The start genome sequence of a fruitfly.
            compare_function: Selects "best" fruitfly child based on
                              breakpoints, distance points, or a combination of
                              both. Default is set on breakpoints.

    """

    if not compare_function:
        compare_function = Fruitfly.breakpoint_compare

    if compare_function == Fruitfly.breakpoint_compare:
        print("Best-First Search: Breakpoints")
    elif compare_function == Fruitfly.distancepoint_compare:
        print("Best-First Search: Distancepoints")
    else:
        print("Best-First Search: Combinationpoints")

    print("genome fruitfly:", root_genome)

    solution = root_genome.solution()
    solved = False

    queue = []
    queue.append(root_genome)

    while not solved:

        # get current node with least mutationpoints
        genome = heapq.heappop(queue)

        # show path to solution, when solution found
        if genome == solution:
            solved = True
            solution_child = genome

            print("Solution found in generation: ",
                  solution_child.get_generation())

            path = solution_child.path_solution()
            print("Path to solution: ")
            for swap in range(len(path)):
                print("swap: {:2d}".format(swap), path[swap])
            print("\n")

        # generate children and place in heap based on mutationpoints
        else:
            children = genome.create_children(compare_function)
            for child in children:
                heapq.heappush(queue, child)
