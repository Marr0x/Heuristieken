# main.py
# 
# Heuristics - Case: fruit flies
# Authors: Marwa Ahmed, Shan Shan Huang & Mercylyn wiemer
# 
# Implements algorithms to find the evolutionary path between fruit fly species.

from code import helpers

class Fruitfly:

	def __init__(self, genome_file):
		""" initialize with an array of genes from chosen fruitfly genome. """

		self.genes = helpers.load_genome(genome_file)

	def print_genes(self):
		print(self.genes)

	def bubble_sort(self):
		""" This program sorts a list of genes using bubblesort. """

		n = len(self.genes)
		count = 0

		for i in range (n):
			for j in range (n - 1):
				if self.genes[j] > self.genes[j + 1]:
					self.genes[j], self.genes[j + 1] = self.genes[j + 1], self.genes[j]
					count += 1
		print("count: {}" .format(count))

	def smallest_first_sort(self):
		""" This program sorts a list of genes by making inversions so that the
			smallest number constantly get sorted first. Upperbound: n - 1 """

		n = len(self.genes)
		count = 0

		for i in range(n - 1):

			minimum = min(self.genes[i:])
			minimum_index = self.genes[i:].index(minimum)

			j = i + minimum_index

			if minimum is not self.genes[i]:
				self.genes[i:j + 1] = reversed(self.genes[i: j + 1])
				count += 1

		print("count: {}" .format(count))

def main ():

	genome = input("Please enter the filename with a genome \n")

	genome1 = Fruitfly(genome)
	genome1.print_genes()

	genome1.smallest_first_sort()
	genome1.print_genes()

if __name__ == "__main__":
	main()