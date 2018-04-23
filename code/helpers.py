import os

def gene_set1():

	genes = []

	# change current dir to parent directory to access data folder
	os.chdir(os.path.dirname(os.getcwd()))

	# open file with D. melanogaster genome
	with open('data/genome.txt', 'r') as file:
		gene_list = file.read().split(',')

	# store every gene in genes
	for gene in gene_list:
		genes.append(int(gene))

	return genes

def gene_set2():

	genes = []

	# change current dir to parent directory to access data folder
	os.chdir(os.path.dirname(os.getcwd()))

	# open file with D. melanogaster genome
	with open('data/genome2.txt', 'r') as file:
		gene_list = file.read().split(',')

	# store every gene in genes
	for gene in gene_list:
		genes.append(int(gene))

	return genes