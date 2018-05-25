#   helpers.py
#
#   Heuristics - Case: Fruitfly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   Contains a function that loads a file with a genome sequence.

def load_genome(file_name):
    """ Loads an array with fruitfly genes from text file.

        Args: name of textfile (e.g. "genome_length25.txt").

        Returns: genome from the file.

    """

    genes = []

    with open('data/' + file_name, 'r') as file:
        genome_file = file.read().split(',')

    for gene in genome_file:
        genes.append(int(gene))

    return genes