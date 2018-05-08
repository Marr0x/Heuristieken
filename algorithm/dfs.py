from classes.Stack import Stack
from classes.Fruitfly import Fruitfly

def rev(genes, x, y):

    """ reverses a list of genes
        genes = the list of integers
        x  = index of list where reversion should start
        y = index of list where reversion should end
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

def add_children_stack(children, stack):
    for child in children:
        stack.append(child)
    return stack

def dfs():

    stack = Stack()

    # genes = [5, 4, 3, 2, 1]
    genome1 = Fruitfly(genome1)

    print(genome1)

    upperbound = (len(genes) - 1)

    # stopcriterium functie

    layer1 = create_rev(genes)

    # for child in layer1:
    #     stack.append(child)
    add_children_stack(layer1, stack)

    print(stack)

    layer2_child1 = create_rev(stack[0])

    add_children_stack(layer2_child1, stack)

    print(stack)

if __name__ == "__main__":
    dfs()
