#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Tests for algorithms!

from code.classes.Fruitfly import Fruitfly
# from code import dfs_basic
from code import dfs_random
import numpy as np

genome = [1, 2, 3, 4, 5]
# genome = [5, 4, 3, 2, 1]
np.random.shuffle(genome)
fly1 = Fruitfly(genome, 0)

print('genome:{}'.format(fly1))

# print('mutationpoints: {}'.format(mutationpoints))

# print(fly1.create_children())
dfs_random.dfs_random(fly1)