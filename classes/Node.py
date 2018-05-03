class Genome(object):
    """ List of integers which respresent genes.

    Attributes:
        genome (list of integers): integers represent de genes and presented in
        the order they are given.
    """

    def __init__(self, genome = []):
        self.genome = genome

    def __repr__(self):
        return "%s" % (self.genome)

class Node(object):
    """ Nodes for a tree consisting of a genome.

    Attributes:
        genome (string): name of the genome
        children (list): next layer of nodes (current node is the parent). The
        nodes in the next layer are the children.
    """

    def __init__(self, genome, children = None):
        self.genome = genome
        self.children = children or []
        # self.parent = parent
        # self.layer = None


    def add_child(self, node):
        """ Link child node to parent nodeself.

        Args:
            node (Node): child of the current node
        """
        self.children.append(node)



    def __str__(self):
        return str(self.genome)

    def get_children(self):
        return self.children


    # def get_rev_children(self):
    #     children = self.children[:]
    #     children.reverse()
    #     return children

    # to print genome but __str__ works too
    # def __repr__(self, level=0):
    #     ret = repr(self.genome)
    #     for child in self.children:
    #         ret += child.__repr__(level + 1)
    #     return ret

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def __str__(self):
        current = top
        while current is not None:
            print(current.value)
            current = current.genome

    def push(self, value):
        self.top = Node(value, self.top)
        self.length += 1

    def top(self):
        return self.top.genome

    def pop(self):
        temp = self.top.genome
        self.length -= 1
        return temp

    def empty(self):
        return self.top == None

    def size(self):
        return self.length

def testStack():
    stack = Stack()
    stack.push(10)
    assert stack.size() == 1
    stack.push(20)
    assert stack.size() == 2
    # assert stack.top() == 20
    assert stack.pop() == 20
    assert stack.size() == 1
    assert stack.pop() == 10
    assert stack.size() == 0
    print("all tests passed")

if __name__ == "__main__":
    genome1 = Genome([5, 4, 3, 2, 1])
    genome2 = Genome([4, 5, 3, 2, 1])
    node1 = Node(genome1)
    node2 = Node(genome2)
    # node3 = Node(3)
    # node4 = Node(4)
    # node5 = Node(5)
    # node6 = Node(6)
    # node7 = Node(7)

    # node1.add_child(node2)
    # node1.add_child(node3)
    # node1.add_child(node4)

    print(node1)
    print(node2)
    # print(node1.children)

    # testStack()
