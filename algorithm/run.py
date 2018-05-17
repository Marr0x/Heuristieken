from classes.Fruitfly import Fruitfly
import numpy as np
import bfs

genome = [5,3,4,2,1]
fly1 = Fruitfly(genome, 0)


# print(fly1)

# print(fly1.create_children())
bfs.bfs(fly1)
