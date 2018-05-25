#   exp3.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#  Compares the breadth first search, depth first search algorithms with the
#  algorithms with heuristics: best first search and branch and bound beam search.

from code.classes.Fruitfly import Fruitfly
from code.classes.Fruitflytest import Fruitflytest
from code import bfs_basic
from code import dfs_basic
from code import best_first_search
from code import bnb_breakpoints
import matplotlib
import numpy as np

genome_8 = [1,2,3,4,5,6,7,8]
new_genome = genome_8[:]
np.random.shuffle(new_genome)


fly1=Fruitfly(new_genome, 0)
fly2=Fruitflytest(new_genome, 0)
generation_bfs_break = best_first_search.bfs(fly1)
generation_bfs_basic = bfs_basic.bfs(fly2)
generation_dfs_basic = dfs_basic.dfs(fly2)

print("breadth first", generation_bfs_break)
print("gen bfs basic", generation_bfs_basic)