#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Tests for algorithms!

from code.classes.Fruitfly import Fruitfly
# from code import dfs_basic
# from code import dfs_random
from code import dfs_upperbound
import numpy as np

genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
# genome = [5, 4, 3, 2, 1]
# genome = [2, 1, 4, 5, 3]
# genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

np.random.shuffle(genome)
fly1 = Fruitfly(genome, 0)

print('genome:{}'.format(fly1))

# print('mutationpoints: {}'.format(mutationpoints))

# print(fly1.create_children())
dfs_upperbound.dfs_upperbound(fly1)
