#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Tests for algorithms!

from code.classes.Fruitfly import Fruitfly
from code import dfs_breakpoints
import numpy as np

genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
# genome = [1, 2, 3, 4, 5]
# genome = [3, 5, 2, 1, 4]
# genome = [2, 1, 4, 5, 3]
# genome = [3, 5, 4, 2, 1]
# genome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# genome = [7, 2, 14, 8, 3, 1, 10, 9, 13, 11, 6, 15, 4, 5, 12]
# genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

# np.random.shuffle(genome)
fly = Fruitfly(genome, 0)

print('genome:{}'.format(fly))

# print('mutationpoints: {}'.format(mutationpoints))

# print(fly1.create_children())
# dfs_breakpoints.dfs_upperbound(fly, Fruitfly.breakpoint_compare)
dfs_breakpoints.dfs_upperbound(fly)
