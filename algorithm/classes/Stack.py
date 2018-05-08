from .Fruitfly import Fruitfly

class Stack():
    def __init__(self):
        self.items = []


    def __getattr__(self, name):
        return getattr(self.items, name)


    def __repr__(self):
        return str(self.items)


    # def __str__(self):
        # return  str(self.__class__) + '\n' + '\n'.join((str(item) + ' = ' + str(self.__dict__[item]) for item in sorted(self.__dict__)))

    def __str(self):
        return self.items


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
