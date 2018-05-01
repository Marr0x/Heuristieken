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
        genome_id (string): name of the genome
        children (list): next layer of nodes (current node is the parent). The
        nodes in the next layer are the children.
    """

    def __init__(self, genome_id, children = None):
        self.genome_id = genome_id
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
        return str(self.genome_id)

    def get_children(self):
        return self.children


    # def get_rev_children(self):
    #     children = self.children[:]
    #     children.reverse()
    #     return children

    def __repr__(self, level=0):
        ret = repr(self.genome_id)
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


if __name__ == "__main__":
    genome1 = Genome([5, 4, 3, 2, 1])
    genome2 = Genome([4, 5, 3, 2, 1])
    node1 = Node(genome1)
    node2 = Node(genome2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    # node1.add_child(node2)
    # node1.add_child(node3)
    # node1.add_child(node4)

    print(node1)
    print(node2)
    # print(node1.children)
