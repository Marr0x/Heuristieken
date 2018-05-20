#   run1.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Tests for algorithms!

from code.classes.Fruitfly import Fruitfly
from code import bfs_breakpoint
import numpy as np

genome = [1, 2, 3, 4, 5]
np.random.shuffle(genome)
fly = Fruitfly(genome, 0)

print(fly)
print("breakpoints:", fly.breakpoints())

bfs_breakpoint.bfs(fly)