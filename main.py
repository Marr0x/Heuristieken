# fruitfly.py
# 
# Heuristieken - Case: fruitflies
# Authors: Marwa Ahmed, Shan Shan Huang & Mercylyn wiemer
# 
# Datastructure of the fruitfly case

import os
import helpers

class Fruitfly:

	def __init__(self, geneset):
		self.genes = []

		self.geneset = geneset

		if self.geneset is 1:
			self.genes = helpers.gene_set1()

		elif self.geneset is 2:
			self.genes = helpers.gene_set2()

	def print_genes(self):
		print(self.genes)

	def bubble_sort(self):
		n = len(self.genes)
		count = 0

		for i in range (n):
			for j in range (n - 1):
				if self.genes[j] > self.genes[j + 1]:
					self.genes[j], self.genes[j + 1] = self.genes[j + 1], self.genes[j]
					count += 1
		print(count)

	def pancake_sort(self):
		n = len(self.genes)
		count = 0

		for i in range(n - 1):

			minimum = min(self.genes[i:])
			minimum_index = self.genes[i:].index(minimum)

			j = i + minimum_index

			if minimum is not self.genes[i]:
				self.genes[i:j + 1] = reversed(self.genes[i: j + 1])
				count += 1

		print (count)

def main ():

	genes = Fruitfly(1)
	genes.print_genes()
	genes.pancake_sort()
	genes.print_genes()

if __name__ == "__main__":
	main()