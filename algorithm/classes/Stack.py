class Stack:
    def __init__(self):
            # self.top = None
            # self.length = 0
            self.items = []

    def push(self, item):
        # self.top = Node(value, self.top)
        # self.length += 1
        self.items.append(item)


    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
