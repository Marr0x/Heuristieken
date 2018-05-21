#	Fruitfly.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   The class Fruitfly contains all the methods needed for the algorithms.


class Fruitfly(object):
    """
    Genome: consists of a list of integers.
    The genome is loaded by using the function load_genome.
    """

    def __init__(self, genes, generation=None, parent=None):
        """ Initialize with an array of genes from chosen fruitfly genome. """

        self.genes = genes
        self.generation = generation
        self.parent = parent

    def __eq__(self, other):
        """ Compares whether gene sequences are the same. """

        return self.genes == other.genes

    def get_genes(self):
        """ Getter.

        Returns:
            Genes: list of integers.
        """

        return self.genes

    def solution(self):
        """ Sorts genome for a solution genome.

        Returns:
            Solution genome.

        """

        solution = Fruitfly(sorted(self.genes))

        return solution


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

    def path_solution(self):
        """ Returns the path of the solution.
        """
        path = [self]

        ancestor = self.parent

        while ancestor is not None:
            path.append(ancestor)
            ancestor = ancestor.get_parent()

        return path

    def path_length(self):
        """ Returns the length of the path solution.

            Returns:
                length of path solution (integer).

        """

        return (len(self.path_solution()) - 1)

    def distancepoints(self):
        """ Calculates the distance of the genome index and the solution index.

            Returns:
                distancepoints.
        """

        distancepoints = 0

        for gene in self.genes:
            solution_index = gene - 1
            gene_index = self.genes.index(gene)

            if gene_index != solution_index:
                distancepoints += abs(solution_index - gene_index)

        return distancepoints

    def breakpoints(self):
        """ Calculates breakpoints of genome. Breakpoint occurs between
            two non-consecutive numbers.

            Returns:
                breakpoints.
        """

        breakpoints = 0

        for gene in range(len(self.genes) - 1):
            if abs(self.genes[gene] - self.genes[gene + 1]) > 1:
                breakpoints += 1

        return breakpoints

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
            print("error: start or end index invalid")

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
