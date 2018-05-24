#   exp1.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   Experiment 1 tests 25 genomes of length 25. It compares the solutions
#   found with the best-first search: breakpoints, distancepoints, 
#   and combinationpoints.

from code.classes.Fruitfly import Fruitfly
from code import best_first_search
from experimentation import test_set_100
import numpy as np
import matplotlib.pyplot as plt

genome_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
breakpoint_list = []
distancepoint_list = []
combinationpoint_list = []

for i in range(25):
    genome = list(range(1, 26))
    np.random.shuffle(genome)
    fly=Fruitfly(genome, 0)

    generation_break = best_first_search.bfs(fly)
    generation_dist = best_first_search.bfs(fly, Fruitfly.distancepoint_compare)
    breakpoint_list.append(generation_break)
    distancepoint_list.append(generation_dist)


print(genome_list)
print(breakpoint_list)

plt.plot(genome_list, breakpoint_list, marker="o", color="blue", label="breakpoint")
plt.plot(genome_list, distancepoint_list, marker="o", color="red", label="distancepoint")
plt.legend()

plt.show()

