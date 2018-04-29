#!/usr/bin/env python
# Name: Marwa Ahmed, Shan Shan Huang & Mercylyn Wiemer
# Heuristieken: upperbound of n-1

def smallest_first_sort(genes):
	""" This program sorts a list of genes by making inversions so that the
	smallest number constantly get sorted first. """

	n = len(genes)
	count = 0

	for i in range(n - 1):

		minimum = min(genes[i:])
		minimum_index = genes[i:].index(minimum)

		j = i + minimum_index

		if minimum is not genes[i]:
			genes[i:j + 1] = reversed(genes[i: j + 1])
			count += 1

	print ("count: {}".format(count))

if __name__ == "__main__":

	genes_melanogaster = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
								14, 15, 16, 17, 21, 3, 4, 9]

	print("unsorted: {}".format(genes_melanogaster))
	smallest_first_sort(genes_melanogaster)
	print("sorted: {}".format(genes_melanogaster))	

