#	main.py
#
#	Heuristics - Case: Fruit fly
#	Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#	Implements algorithms to find the evolutionary path between fruit fly species.

from algorithm.classes.helpers import load
# from algorithm.classes.Stack import Stack
from algorithm.classes.Fruitfly import Fruitfly
import numpy as np
from algorithm import bfs

# from algorithm import dfs

def main ():

    # genome = input("Please enter the filename with a genome \n")

    # genome1 = Fruitfly(genome)
    # genome1.print_genes()

    # genome1.smallest_first_sort()
    # dfs.dfs()
    # genome1.print_genes()

    genome = [5,3,4,2,1]
    fly1 = Fruitfly(genome, 0)


    # print(fly1)

    # print(fly1.create_children())
    bfs.bfs(fly1)


if __name__ == "__main__":
    main()
