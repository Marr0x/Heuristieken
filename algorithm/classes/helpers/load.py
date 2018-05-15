#!/usr/bin/env python
#
# Name: Marwa Ahmed, Shan Shan Huang & Mercylyn Wiemer
# Heuristieken: helps loading data


def load_genome(file_name):
	""" loads an array with fruitfly genes from text file. """

	genes = []

	# we still need to do error checking when file does not exist!
	with open('data/' + file_name, 'r') as file:
		genome_file = file.read().split(',')

	for gene in genome_file:
		genes.append(int(gene))

	return genes

# def rev(genes, x, y):
#     """ Reverses a list of genes.

#         Two indexes are given: start value and end value. The genome will be
#         reverserd from the start to end value.
#         If a greater value is given than the length of the genome and error
#         message will be given.

#         Args:
#             self (list of integers): fruitfly genome
#             x (int): Index of list where reversion should start.
#             y (int): Index of list where reversion should end.

#         Returns:
#             Genes (integer list) in new order.
#     """

#     new_genes = genes[:]

#     if x is 0:
#         new_genes[:y+1] = new_genes[y::-1]
#         return new_genes
#     elif y < len(genes):
#         new_genes[x:y+1] = new_genes[y:x-1:-1]
#         return new_genes
#     else:
#         print("error1")