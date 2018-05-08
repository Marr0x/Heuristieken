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