#   main.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Tests for algorithms!

from code.classes.Fruitfly import Fruitfly
from code import bfs_basic
import numpy as np

genome = [1, 2, 3, 4, 5]
np.random.shuffle(genome)
fly1 = Fruitfly(genome, 0)

mutationpoints = fly1.mutationpoints()

print('genome:{}'.format(fly1))

print('mutationpoints: {}'.format(mutationpoints))

# print(fly1.create_children())
bfs_basic.bfs(fly1)
