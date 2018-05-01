class Node():
    def __init__(self, genes, parent=None):
        self.genes = genes
        self.children = []
        self.parent = parent
        # self.layer = None


    def add_node(self, node):
        self.children.append(node)


    def __str__(self):
        return str(self.genes)


    def __repr__(self, level=0):
        ret = repr(self.genes)
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.add_node(node2)
    node1.add_node(node3)
    node1.add_node(node4)

    print(node1.children)
