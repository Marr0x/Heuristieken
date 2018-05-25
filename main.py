#   main.py
#
#   Heuristics - Case: Fruitfly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   Implements algorithms to find the evolutionary path between
#   fruitfly species.

from code.classes.Fruitfly import Fruitfly
from code import best_first_search
from code import bnb_breakpoints
from code import helpers
import numpy as np


def main():

    # ask user for input: choose genomeset
    while True:
        try:
            genomeset = int(input("Please choose one of the options below: \n"
                                  "(1) D. Melanogaster genome set with 25 genes\n"
                                  "(2) Generate random genome set\n"))
        except ValueError:
            print("Please enter a valid option (number).")
            continue

        if genomeset < 1 or genomeset > 2:
            print("Please enter a valid option (number).")
            continue
        else:
            break

    genome = []

    # make fruitfly with genome of length 25
    if genomeset == 1:
        genome = helpers.load_genome("genome_length25.txt")
        if not genome:
            print("Could not load genome set")
        make_fly(genome)

    # make fruitfly with genome of given length
    else:

        while True:
            try:
                length_genomeset = int(input("\nsize of genome? (5 - 25) \n"))
            except ValueError:
                print("Please enter valid size of genomeset.")
                continue

            if length_genomeset < 5 or length_genomeset > 25:
                print("Please enter valid size of genomeset.")
                continue
            else:
                genome = list(range(1, length_genomeset + 1))
                np.random.shuffle(genome)
                make_fly(genome)
                break


def make_fly(genome):
    """ Makes fruitfly using given genome.

        Args:
            Genome: list of integers.

    """

    fly = Fruitfly(genome, 0)

    # ask user input: choose algorithm
    algorithm = input("\nWhich algorithm would you like to use to "
                      "find the evolutionary path between fruitflies?\n"
                      "(1) Branch and Bound:  breakpoints\n"
                      "(2) Best-first search: breakpoints\n"
                      "(3) Best-first search: distancepoints\n"
                      "(4) Best-first search: mutationpoints\n"
                      "(5) Best-first search: combinationpoints\n")

    # implement algorithms
    if algorithm == "1":
        print("\n")
        bnb_breakpoints.bnb(fly)
    elif algorithm == "2":
        print("\n")
        best_first_search.bfs(fly, Fruitfly.breakpoint_compare)
    elif algorithm == "3":
        print("\n")
        best_first_search.bfs(fly, Fruitfly.distancepoint_compare)
    elif algorithm == "4":
        print("\n")
        best_first_search.bfs(fly, Fruitfly.mutationpoint_compare)
    elif algorithm == "5":
        print("\n")
        best_first_search.bfs(fly, Fruitfly.combinationpoint_compare)
    else:
        print("Please enter valid option")


if __name__ == "__main__":
    main()
