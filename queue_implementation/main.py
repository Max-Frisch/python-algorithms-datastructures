class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop(len(self.items)-1)

    def peek(self):
        if len(self.items) != 0:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
