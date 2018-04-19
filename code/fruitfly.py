# fruitfly.py
# 
# Heuristieken - Case: fruitflies
# Authors: Marwa Ahmed, Shan Shan Huang & Mercylyn wiemer
# 
# Datastructure of the fruitfly case

import os

class Fruitfly:

	def __init__(self):
		self.genes = []

	def get_genes(self):

		# change current dir to parent directory to access data folder
		os.chdir(os.path.dirname(os.getcwd()))

		# open file with D. melanogaster genome
		with open('data/genome.txt', 'r') as file:
			gene_list = file.read().split(',')

		# store every gene in genes
		for gene in gene_list:
			self.genes.append(int(gene))

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

def main ():

	set1 = Fruitfly()
	set1.get_genes()
	set1.print_genes()
	set1.bubble_sort()
	set1.print_genes()


if __name__ == "__main__":
	main()