from classes.Fruitfly import Fruitfly
import numpy as np
import bfs

# genome = [5,3,4,2,1]
# genome = list(range(1,6))
# genome = [24, 25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# genome = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
genome = [2, 1, 3, 4, 5, 6, 7, 8]
np.random.shuffle(genome)
fly1 = Fruitfly(genome, 0)


print('genome {}'.format(fly1))

# print(fly1.create_children())
bfs.bfs(fly1)
