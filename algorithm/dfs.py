from classes.Stack import Stack
from classes.Fruitfly import Fruitfly
from classes.helpers import load

def rev(genes, x, y):
    """ Reverses a list of genes.

        Two indexes are given: start value and end value. The genome will be
        reverserd from the start to end value.
        If a greater value is given than the length of the genome and error
        message will be given.

        Args:
            self (list of integers): fruitfly genome.
            x (int): Index of list where reversion should start.
            y (int): Index of list where reversion should end.

        Returns:
            Genes (integer list) in new order.
    """

    new_genes = genes[:]

    if x is 0:
        new_genes[:y+1] = new_genes[y::-1]
        return new_genes
    elif y < len(genes):
        new_genes[x:y+1] = new_genes[y:x-1:-1]
        return new_genes
    else:
        print("error1")


def create_rev(genes):
    """ Creates children of genome.

        The children of the genome (list of integers) are created by iterating
        over the genes (single integer).

        Returns:
            A list of n children (list).
    """

    n = len(genes)
    children = []

    # iterates over genes, decreasing every time
    for i in range(n - 1, 0, -1):

        # x is the index of where the reversion starts
        # y is the index of where the reversion ends
        for j in range(0, i):

            x = n - 1 - i
            y = j + (n - i)

            reversed_list = rev(genes, x, y)

            children.append(reversed_list)

    return children


def dfs():
    """ Depth-First Search (dfs): in progress. """

    stack = Stack()
    solution = [1, 2, 3, 4, 5]
    archive = {}

    genome1 = Fruitfly("testgenome.txt")
    genome1 = genome1.get_genes()
    archive[str(genome1)] = "parent"
    stack.push(genome1)
    layer = 0

    while stack:
        child = stack.pop()
        layer += 1
        child_no = 0
       
        next_gen = create_rev(child)

        for child_gen in next_gen:
            if child_gen != solution:
                if not str(child_gen) in archive.keys():
                    stack.push(child_gen)
                    child_no += 1
                    value = "layer:" + str(layer) + "_" + str(child_no)
                    archive[str(child_gen)] = value
            else:
                print("solution found:", child_gen, layer)

    print(stack)
    print(archive)

    upperbound = len(genome1)


if __name__ == "__main__":
    dfs()

