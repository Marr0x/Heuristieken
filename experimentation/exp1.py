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
import matplotlib.pyplot as plt
import numpy as np
import timeit

start_runtime = timeit.default_timer()
<<<<<<< HEAD


# genome_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
x1 = 1
x2 = 101
genome_list = range(x1, x2, 1)
<<<<<<< HEAD:experimentation/exp1.py

=======
>>>>>>> e1997c28ecaad10f4fff52d7b2e20ca430235d18
=======


# genome_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
x1 = 1
x2 = 101
genome_list = range(x1, x2, 1)

>>>>>>> 1c9351727213c872ec98259527fb9d94d1ec9b24
>>>>>>> ae923546138a0d554ce45589a9a902c0827d09d7:exp1.py
breakpoint_list = []
distancepoint_list = []

for i in range(100):
    genome = list(range(1, 26))
    new_genome = genome[:]
    np.random.shuffle(new_genome)
 
    fly=Fruitfly(new_genome, 0)

    generation_break = best_first_search.bfs(fly)
    generation_dist = best_first_search.bfs(fly, Fruitfly.distancepoint_compare)
    # generation_combi = best_first_search.bfs(fly, Fruitfly.combinationpoint_compare)
    
    breakpoint_list.append(generation_break)
    distancepoint_list.append(generation_dist)
    # combinationpoint_list.append(generation_combi)
<<<<<<< HEAD

<<<<<<< HEAD:experimentation/exp1.py
=======
=======
>>>>>>> 1c9351727213c872ec98259527fb9d94d1ec9b24

<<<<<<< HEAD
plt.plot(genome, breakpoint_list, marker="o", color="blue", label="breakpoints")
plt.plot(genome, distancepoint_list, marker="o", color="red", label="distancepoints")
=======
>>>>>>> ae923546138a0d554ce45589a9a902c0827d09d7:exp1.py
print(genome_list)
print("breakpoint_list", breakpoint_list)
print("distancepoint_list", distancepoint_list)
# print("generation_combi", generation_combi)

end_runtime = timeit.default_timer()

runtime = (end_runtime - start_runtime)
print("runtime: ", runtime)

plt.plot(genome_list, breakpoint_list, marker="o", color="blue", label="breakpoint")
plt.plot(genome_list, distancepoint_list, marker="o", color="red", label="distancepoint")
# plt.plot(genome_list, generation_combi, marker="o", color="green", label="combination")

plt.title('Compare algorithms')
plt.xlabel('100 random genomes of length 25')
plt.ylabel('Number of swaps')
plt.grid(True)
<<<<<<< HEAD:experimentation/exp1.py

=======
<<<<<<< HEAD
>>>>>>> e1997c28ecaad10f4fff52d7b2e20ca430235d18
=======

>>>>>>> 1c9351727213c872ec98259527fb9d94d1ec9b24
>>>>>>> ae923546138a0d554ce45589a9a902c0827d09d7:exp1.py
plt.legend()

plt.show()




