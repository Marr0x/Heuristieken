#!/usr/bin/env python
# Name: Marwa Ahmed, Shan Shan Huang & Mercylyn Wiemer
# Heuristieken: first solution

def bubble_sort(genes):
	""" This program sorts a list of genes using bubblesort. """
	
	n = len(genes)
	count = 0

	for i in range (n):
		for j in range (n - 1):
			if genes[j] > genes[j + 1]:
				genes[j], genes[j + 1] = genes[j + 1], genes[j]
				count += 1

	print ("count: {}".format(count))

if __name__ == "__main__":

	genes_melanogaster = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
							14, 15, 16, 17, 21, 3, 4, 9]

	print("unsorted: {}".format(genes_melanogaster))
	bubble_sort(genes_melanogaster)
	print("sorted: {}".format(genes_melanogaster))	
