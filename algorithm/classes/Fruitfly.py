from .helpers import load

class Fruitfly(object):

    def __init__(self, genome_file):
        """ initialize with an array of genes from chosen fruitfly genome. """

        self.genes = load.load_genome(genome_file)

    def print_genes(self):
        print(self.genes)

    def __len__(self):
        return len(self.genes)

    def __str__(self):
    	return str(self.genes)

    # def