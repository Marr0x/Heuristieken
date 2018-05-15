#   Stack.py
#   Heuristics - case:  Fruit fly
#   Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   This program implements a stack for fruitfly genomes.


class Stack():
    """ Works with the last-in, first-out principle to add fruitfly genomes.

    Attributes:
        items (list): Stack containing genome sequences.

    """

    def __init__(self):
        """ Initializes the stack (list). """

        self.items = []

    # def __getattr__(self, name):
    #     return getattr(self.items, name)

    # def __repr__(self):
    #     return str(self.items)

    # def __str(self):
    #     return self.items

    def __len__(self):
        """ Overrides len() functions

        Returns:
            The length of the stack.

        """
        return len(self.items)

    def push(self, item):
        """ Appends item (genome sequence) to stack. """
        self.items.append(item)

    def pop(self):
        """ Pops item (genome sequence) from stack.

        Returns:
            Item (list of integers): genome sequence.

        """
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]