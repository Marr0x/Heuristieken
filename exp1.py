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

breakpoint_list = []
distancepoint_list = []

for i in range(25):
    genome = list(range(1, 26))
    new_genome = genome[:]
    np.random.shuffle(new_genome)
 
    fly=Fruitfly(new_genome, 0)

    generation_break = best_first_search.bfs(fly)
    generation_dist = best_first_search.bfs(fly, Fruitfly.distancepoint_compare)
    breakpoint_list.append(generation_break)
    distancepoint_list.append(generation_dist)


plt.plot(genome, breakpoint_list, marker="o", color="blue", label="breakpoints")
plt.plot(genome, distancepoint_list, marker="o", color="red", label="distancepoints")
plt.legend()

plt.show()

