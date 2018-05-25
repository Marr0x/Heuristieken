#   best_first_search.py
#
#   Heuristics - Case: Fruitfly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   Uses best-first search to find the path of inversions that changed
#   the genome of one fruitfly species to the other one. To select "the best"
#   fruitflychild it uses breakpoints, distancepoints, mutationpoints or
#   a combination of breakpoints + distancepoints.

from .classes.Fruitfly import Fruitfly
import heapq
import timeit


def bfs(root_genome, points_function=None):
    """ Best-First Search (bfs): Searches for series of mutations that changed
        the genome of one fruitfly species to the other one.

        Args:
            root_genome: the start genome sequence of a fruitfly.
            points_function: selects "best" fruitfly child based on
                breakpoints, distance points, mutationpoints or a combination of
                breakpoints + distancepoints. Default is set on breakpoints.

    """

    start_runtime = timeit.default_timer()

    if not points_function:
        points_function = Fruitfly.breakpoint_compare

    if points_function == Fruitfly.breakpoint_compare:
        print("Best-First Search: Breakpoints")
    elif points_function == Fruitfly.distancepoint_compare:
        print("Best-First Search: Distancepoints")
    elif points_function == Fruitfly.mutationpoint_compare:
        print("Best-First Search: Mutationpoints")
    else:
        print("Best-First Search: Combinationpoints")

    print("Genome fruitfly:", root_genome)

    solution = root_genome.solution()
    solved = False

    queue = []
    queue.append(root_genome)

    while not solved:

        # get current node with least points
        genome = heapq.heappop(queue)

        # show path to solution, when solution found
        if genome == solution:
            solved = True
            print("Solution found in generation: ",
                  genome.get_generation())

            path = genome.path_solution()
            print("Path to solution: ")

            for inversion in range(len(path)):
                print("Inversion: {:2d}".format(inversion), path[inversion])

        # generate children and place in heap based on pointsfunction
        else:
            children = genome.create_children(points_function)
            for child in children:
                heapq.heappush(queue, child)

    end_runtime = timeit.default_timer()
    runtime = (end_runtime - start_runtime)
    print("Runtime: ", runtime)
