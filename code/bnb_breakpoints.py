#   bnb_breakpoints.py
#
#   Heuristics - Case: Fruitfly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   Implements the Branch and Bound (dfs) algorithm that prunes using
#   breakpoints to find the evolutionary path between fruit fly species.

from .classes.Fruitfly import Fruitfly
import heapq
import timeit


def bnb(root_genome):
    """ Branch and Bound: depth first search that prunes using breakpoints.

    This algorithm searches for the best path to the solution genome
    (integers ordered from low to high). The path consists of inversions of
    blocks of genes. From the root genome every possible inversion is generated:
    the children. The best two children, based on breakpoints, are selected and
    added to the stack. Then the children are compared to the solution.
    When in a generation the solution is found, the upperbound is updated.
    So the algorithm will discard the children after this generation.

        Args:
            root_genome: genome sequence of fruitfly provided by user.

    """

    start_runtime = timeit.default_timer()

    print("Branch and Bound: depth-first search using breakpoints.\n")
    print("Genome fruitfly:", root_genome)

    stack = []
    stack.append(root_genome)

    # upperbound based upon sorting smallest integer first to correct position
    upperbound = len(root_genome) - 1

    n_best_children = 2
    solution = root_genome.solution()

    # create children and search for solution
    while stack:

        genome = stack.pop()
        genome_generation = genome.get_generation()

        if genome_generation < upperbound:
            children = genome.create_children(Fruitfly.breakpoint_compare)

            # select 2 children with the lowest number of breakpoints
            smallest_children = heapq.nsmallest(n_best_children, children)

            # checks for solution and updates upperbound
            for child in smallest_children:
                if child.get_generation() < upperbound:
                    if child != solution:
                        stack.append(child)
                    else:
                        upperbound = child.get_generation()
                        path = child.path_solution()
                        print("Solution found in generation: {}, but still"
                              " searching for a better solution..."
                              .format(upperbound))

    print("\nBest solution found in generation: ", upperbound)
    print("Path to solution: ")

    # prints path to solution
    for inversion in range(len(path)):
        print("Inversion: {:2d} {}".format(inversion, path[inversion]))
    print("")

    end_runtime = timeit.default_timer()
    runtime = (end_runtime - start_runtime)
    print("Runtime: ", runtime)
