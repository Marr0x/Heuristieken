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
import matplotlib.pyplot as plt
import numpy as np
import timeit

start_runtime = timeit.default_timer()


# genome_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
x1 = 1
x2 = 101
genome_list = range(x1, x2, 1)

breakpoint_list = []
distancepoint_list = []
combinationpoint_list = []

for i in range(100):
    genome = list(range(1, 26))
    new_genome = genome[:]
    np.random.shuffle(new_genome)
 
    fly=Fruitfly(new_genome, 0)

    # generation_break = best_first_search.bfs(fly)
    # generation_dist = best_first_search.bfs(fly, Fruitfly.distancepoint_compare)
    generation_combi = best_first_search.bfs(fly, Fruitfly.combinationpoint_compare)
    
    # breakpoint_list.append(generation_break)
    # distancepoint_list.append(generation_dist)
    combinationpoint_list.append(generation_combi)

print(genome_list)
# print("breakpoint_list", breakpoint_list)
# print("distancepoint_list", distancepoint_list)
print("generation_combi", generation_combi)

end_runtime = timeit.default_timer()

runtime = (end_runtime - start_runtime)
print("runtime: ", runtime)

# plt.plot(genome_list, breakpoint_list, marker="o", color="blue", label="breakpoint")
# plt.plot(genome_list, distancepoint_list, marker="o", color="red", label="distancepoint")
plt.plot(genome_list, generation_combi, marker="o", color="green", label="combination")

plt.title('Compare algorithms')
plt.xlabel('100 random genomes of length 25')
plt.ylabel('Number of swaps')
plt.grid(True)

plt.legend()

plt.show()




