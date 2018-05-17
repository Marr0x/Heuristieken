#	Fruitfly.py
#	Heuristics - case: Fruit fly
#	Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#

from .helpers import load

class Fruitfly(object):
    """

    Genome: consists of a list of integers. The Genome is loaded from a txt file.

    The genome is loaded by using the function load_genome from helpers.


    """

    def __init__(self, genes, generation=None, parent=None):
        """ initialize with an array of genes from chosen fruitfly genome. """

        self.genes = genes
        self.generation = generation
        self.parent = parent

    def __eq__(self, other):
        return self.genes == other.genes

    def get_genes(self):
        """ Getter.

        Returns:
            Genes: list of integers.
        """

        return self.genes

    def get_generation(self):
        """ Getter.

        Returns:
            Generation: integer.
        """

        return self.generation

    def get_parent(self):
        """ Getter.

        Returns:
            parent: integer.
        """

        return self.parent

    def print_genes(self):
        """ Prints the genes. """
        print(self.genes)

    def __len__(self):
        """ Overrides len() functions.

        Returns:
            The number of integers (genes) in a genome (list).

        """
        return len(self.genes)

    def __repr__(self):
        """ Overrides __str__() method.

        Returns:
            String representation of genes.

        """
        return str(self.genes)

    def rev(self, x, y):
        """ Reverses a list of genes.

            Two indexes are given: start value and end value. The genome will be
            reverserd from the start to end value.
            If a greater value is given than the length of the genome and error
            message will be given.

            Args:
                self (list of integers): fruitfly genome.
                x (int):  Index of list where reversion should start.
                y (int): Index of list where reversion should end.

            Returns:
                Genes (integer list) in new order.
        """

        new_genes = self.genes[:]

        if x is 0:
            new_genes[:y+1] = new_genes[y::-1]
            return new_genes
        elif y < len(self.genes):
            new_genes[x:y+1] = new_genes[y:x-1:-1]
            return new_genes
        else:
            print("error1")

    def create_children(self):
        """ Creates children of genome.

            The children of the genome (list of integers) are created by iterating
            over the genes (single integer).

            Returns:
                A list of n children (list).
        """

        n = len(self.genes)
        children = []

        # iterates over genes, decreasing every time
        for i in range(n - 1, 0, -1):

            # x is the index of where the reversion starts
            # y is the index of where the reversion ends
            for j in range(0, i):

                x = n - 1 - i
                y = j + (n - i)

                reversed_list = self.rev(x, y)

                child = Fruitfly(reversed_list, self.generation + 1, self)

                children.append(child)

        return children
