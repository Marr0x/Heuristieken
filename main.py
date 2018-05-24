#	main.py
#
#	Heuristics - Case: Fruit fly
#	Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#	Implements algorithms to find the evolutionary path between 
#   fruit fly species.

from code.classes.Fruitfly import Fruitfly
from code import best_first_search
from data import load_data
import numpy as np

genomeset = input("\nPlease choose one of the options below: \n\
(1) Use default genome set with 25 genes\n\
(2) Generate own random genome set\n")

genome = []

if genomeset == "1":
    # load fruitfly genome of length 25
    genome = load_data.load_genome("genome1.txt")

elif genomeset == "2":
    # get shuffled fruitfly genome of given length
    length_genomeset = int(input("\nsize of genomeset? (1 - 25) \n"))
    if length_genomeset < 1 or length_genomeset > 25:
        print("Please enter valid size of genomeset.")
    else:
        genome = list(range(1, length_genomeset + 1))
        np.random.shuffle(genome)

else:
    print("Please enter valid option")

fly = Fruitfly(genome, 0)

algorithm = input("\nWhich algorithm would you like to use to \
find the evolutionary path between fruitflies?\n \
(1) best-first search: breakpoints\n \
(2) best-first search: distancepoints\n \
(3) best-first search: combinationpoints\n")

# implement algorithms
if algorithm == "1":
    print("\n")
    best_first_search.bfs(fly, Fruitfly.breakpoint_compare)
elif algorithm == "2":
    print("\n")
    best_first_search.bfs(fly, Fruitfly.distancepoint_compare)
elif algorithm == "3":
    print("\n")
    best_first_search.bfs(fly, Fruitfly.combinationpoint_compare)
else:
    print("Please enter valid option")
