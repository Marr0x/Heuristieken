#   beamsearch.py
#
#   Heuristics - Case: Fruitfly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)

from .classes.Fruitfly import Fruitfly
import numpy as np
import heapq
import timeit


def beamsearch(root_genome,  points_function=None, beam):
    """ Beam search.

    Heuristic search algorithm: Optimized Best-first search.
    From every layer only the best/promising n (beam) children are selected and
    added to the queue. Depending on the chosen beam: the best solution could
    be returned. The algorithms stops searching when a solution is found.

        Args:
            root_genome: genome sequence of fruitfly provided by user.
            points_function: selects "best" fruitfly child based on
                breakpoints, distance points, mutationpoints or a combination of
                breakpoints + distancepoints. Default is set on breakpoints.
            beam (integer): number of best partial solutions as candidats.

        Returns:
            Numbers of inversions (generations) needed to go from the
            root_genome to the solution genome.

    """
    start_runtime = timeit.default_timer()

    if not points_function:
        points_function = Fruitfly.breakpoint_compare

    if points_function == Fruitfly.breakpoint_compare:
        print("Beam Search: Breakpoints")
    elif points_function == Fruitfly.distancepoint_compare:
        print("Beam Search: Distancepoints")
    elif points_function == Fruitfly.mutationpoint_compare:
        print("Beam Search: Mutationpoints")
    else:
        print("Beam Search: Combinationpoints")

    print("root genome:", root_genome)

    solved = False
    solution = root_genome.solution()

    queue = []
    priority_queue = []
    queue.append(root_genome)

    while not solved:

        if queue:

            # get current node with least points
            genome = queue.pop(0)

            # show path to solution, when solution found
            if genome == solution:
                solved = True
                print("Solution found in generation: ",
                      genome.get_generation())

                path = genome.path_solution()
                print("Path to solution: ")

                for inversion in range(len(path)):
                    print("Inversion: {:2d}".format(inversion), path[inversion])

            else:
                children = genome.create_children(points_function)

                for child in children:
                    heapq.heappush(priority_queue, child)

        else:
            for child in range(beam):
                best = heapq.heappop(priority_queue)
                queue.append(best)

            priority_queue[:] = []

    end_runtime = timeit.default_timer()
    runtime = (end_runtime - start_runtime)
    print("Runtime: ", runtime)

    return genome.get_generation()
