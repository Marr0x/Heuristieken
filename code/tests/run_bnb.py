#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Tests for algorithms!

from code.classes.Fruitfly import Fruitfly
from code import bnb_breakpoints
import numpy as np

genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
# genome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# np.random.shuffle(genome)
fly = Fruitfly(genome, 0)

print('genome:{}'.format(fly))

# print('mutationpoints: {}'.format(mutationpoints))

# print(fly1.create_children())
# dfs_breakpoints.dfs_upperbound(fly, Fruitfly.breakpoint_compare)
bnb_breakpoints.bnb(fly)
