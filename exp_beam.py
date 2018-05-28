#   exp4.py
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
from code import beamsearch
import matplotlib.pyplot as plt
import numpy as np
import timeit

start_runtime = timeit.default_timer()

inversions = []
beam_list = [1, 3, 5, 10, 20, 50, 80, 100]

genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

fly=Fruitfly(genome, 0)

for beam_size in beam_list:
    inversion = beamsearch.beamsearch(fly, beam_size)
    inversions.append(inversion)


print(inversions)

end_runtime = timeit.default_timer()

runtime = (end_runtime - start_runtime)
print("runtime: ", runtime)

plt.plot(beam_list, inversions, marker = "o", color="blue")

plt.title('Compare beam size')
plt.xlabel('Beam size')
plt.ylabel('Number of inversions')
plt.grid(True)

plt.legend()

plt.show()
