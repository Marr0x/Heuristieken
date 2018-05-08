class Stack():
    def __init__(self):
        self.items = []


    def __getattr__(self, name):
        return getattr(self.items, name)


    def __str__(self):
        return str(self.items)


    def __len__(self):
        return len(self.items)


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()


    def isEmpty(self):
        return self.items == []


    def peek(self):
        return self.items[len(self.items)-1]
