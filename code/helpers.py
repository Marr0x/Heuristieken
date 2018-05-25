#   helpers.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Contains functions that support the algorithms.

def load_genome(file_name):
    """ loads an array with fruitfly genes from text file.

        Args: name of textfile (e.g. "genome_length25.txt")
        Returns: genome from the file

    """

    genes = []

    # we still need to do error checking when file does not exist!
    with open('data/' + file_name, 'r') as file:
        genome_file = file.read().split(',')

    for gene in genome_file:
        genes.append(int(gene))

    return genes