#	main.py
#
#	Heuristics - Case: Fruit fly
#	Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#	Implements algorithms to find the evolutionary path between fruit fly species.

from code.classes.Fruitfly import Fruitfly
from code import bfs_basic
from code import dfs_basic
from data import load_data
import numpy as np

# load fruitfly genome of length 25
genome25 = load_data.load_genome("genome1.txt")

# insert a genome of fruitfly and shuffle
genome = [1, 2, 3, 4, 5]
np.random.shuffle(genome)
fly = Fruitfly(genome, 0)

# implement algorithms
bfs_basic.bfs(fly)
print("\n")
dfs_basic.dfs(fly)