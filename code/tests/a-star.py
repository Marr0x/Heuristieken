
from .classes.Fruitfly import Fruitfly

class Astar(object):

	def __init__(self, genes, archive, ):
		self.value = value
		self.point = point
		self.parent = None
		self.H = 0
		self.G = 0

	def move_cost(self, other):
		return 0 if self.value == '.' else 1


def aStar(start, goal, grid)
	
	openset = set()
	closedset = set()

	current = start

	openset.add(current)

	while openset:
		current = min(openset, )

		if current == goal:
			path = []

			while current.parent:
				path.append(current)
				current = current.parent
			path.append(current)
			return path[::-1]
			