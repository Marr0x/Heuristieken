#   Fruitflytest.py
#
#   Heuristics - Case: Fruitfly
#   Authors: Mercylyn Wiemer (10749306),
#            Shan Shan Huang (10768793),
#            Marwa Ahmed (10747141)
#
#   The Fruitfly class contains all the attributes and methods needed to find
#   the evolutionary path between fruitfly species.


class Fruitflytest(object):
    """ Contains attributes and methods needed to find the evolutionary path
        between fruitfly species.

    """

    def __init__(self, genes, generation=0, parent=None):
        """ Initializes a fruitfly.

            Args:
                genes: list of integers that represent a fruitfly genome.
                generation: integer that shows in which generation fruitfly
                    child is made.
                parent: fruitfly that is a parent of a fruitfly child.
                points_function: compares points given to a fruitfly
                    genome. Consist of mutationpoints, breakpoints,
                    distancepoints, and a combination of break + distancepoints.
                    Default is set on breakpoints when no points function is given.
                mutationpoint: integer that represents the length of an inversion.

        """

        self.genes = genes
        self.generation = generation
        self.parent = parent

        # if not points_function:
        #     self.points_function = self.breakpoint_compare
        # else:
        #     self.points_function = points_function

        # self.mutationpoint = mutationpoint
        # self.breakpoint = self.breakpoints()
        # self.distancepoint = self.distancepoints()

    def breakpoints(self):
        """ Calculates the sum of the breakpoints in a genome. A breakpoint
            is defined as a point where there are two non-consecutive numbers.

            Returns:
                The total breakpoints of a genome: integer.

        """

        breakpoints = 0
        genome_list = self.genes

        for gene in range(len(genome_list) - 1):
            if abs(genome_list[gene] - genome_list[gene + 1]) > 1:
                breakpoints += 1

        return breakpoints

    def distancepoints(self):
        """ Calculates the sum of the distances between a gene in a fruitfly
            genome and the same gene in the solution genome.

            Returns:
                The total distancepoints of a genome: integer.

        """

        distancepoints = 0

        for idx, gene in enumerate(self.genes):
            solution_index = gene - 1

            if idx != solution_index:
                distancepoints += abs(solution_index - idx)

        return distancepoints

    def __lt__(self, other):
        """ Overrides less-than comparison to compare points.

            Returns:
                A points function that compares either breakpoints, distance-
                points, mutationpoints or a combination of breakpoints + distancepoints.

        """

        return self.points_function(self, other)

    def breakpoint_compare(self, other):
        """ Compares amount of breakpoints between fruitflies.

            Returns:
                A boolean value.

        """

        return self.breakpoint < other.breakpoint

    def distancepoint_compare(self, other):
        """ Compares amount of distancepoints between fruitflies.

            Returns:
                A boolean value.

        """

        return self.distancepoint < other.distancepoint

    def mutationpoint_compare(self, other):
        """ Compares amount of mutationpoints between fruitflies.

            Returns:
                A boolean value.

        """

        return self.mutationpoint < other.mutationpoint

    def combinationpoint_compare(self, other):
        """ Compares amount of breakpoints plus distancepoints between fruitflies.

            Returns:
                A boolean value.
        """
        alpha = 0.01
        return (self.breakpoint + round(self.distancepoint * alpha)) < (other.breakpoint + round(other.distancepoint * alpha))

    def get_genes(self):
        """ Gets fruitfly genes.

        Returns:
            Genes: list of integers.

        """

        return self.genes

    def get_generation(self):
        """ Gets generation of fruitfly child.

        Returns:
            Generation: integer.

        """

        return self.generation

    def get_parent(self):
        """ Gets parent of fruitfly child.

        Returns:
            Parent: fruitfly.

        """

        return self.parent

    def get_mutationpoints(self):
        """ Getter for the mutationpoints.

        Returns:
            mutationpoints (integer)

        """

        return self.mutationpoint

    def __eq__(self, other):
        """ Overrides equality operator to compare genes of fruitfly.

            Returns:
                True if fruitfly genes are the same, False otherwise.

        """

        return self.genes == other.genes

    def __len__(self):
        """ Overrides len() functions.

        Returns:
            The number of genes (integers) in a genome (list).

        """

        return len(self.genes)

    def __repr__(self):
        """ Overrides __repr__ method.

        Returns:
            String representation of genes.

        """
        return str(self.genes)

    def rev(self, x, y):
        """ Reverses a list of genes.

            Two indexes are given: start value and end value. The genome will
            be reverserd from the start to end value.

            Args:
                x (int): index of list where reversion should start.
                y (int): index of list where reversion should end.

            Returns:
                Genes in new order: list of integers.

        """

        new_genes = self.genes[:]

        if x is 0:
            new_genes[:y+1] = new_genes[y::-1]
            return new_genes
        else:
            new_genes[x:y+1] = new_genes[y:x-1:-1]
            return new_genes

    def create_children(self):
        """ Creates children of genome.

            The children of the genome are created by iterating over the parent
            fruitfly, making all possible inversions.

            Args:
                compare_function: chooses a pointsfunction to compare fruitflies.

            Returns:
                children: list of fruitfly children.

        """

        n = len(self.genes)
        children = []

        for i in range(n - 1, 0, -1):

            for j in range(0, i):

                start_rev = n - 1 - i
                end_rev = j + (n - i)

                reversed_list = self.rev(start_rev, end_rev)

                # formula mutationpoints based upon the evolution whereas large inversions are less likely
                child = Fruitflytest(reversed_list, self.generation + 1, self)

                children.append(child)

        return children

    def solution(self):
        """ Sorts fruitfly genes.

        Returns:
            solution genome: sorted list of integers.

        """

        solution = Fruitflytest(sorted(self.genes))

        return solution

    def path_solution(self):
        """ Shows the path of inversions from a fruitfly genome
            to the solution.

        Returns:
            The path of the solution: list of fruitflies.

        """

        path = [self]
        ancestor = self.parent

        while ancestor:
            path.insert(0, ancestor)
            ancestor = ancestor.get_parent()

        return path

    def path_length(self):
        """ Gets the length of the path solution.

            Returns:
                Length of path solution: integer.

        """

        return (len(self.path_solution()) - 1)
