class Stack:
    

    def __init__(self):
        self.items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)
        
    def __bool__(self):
       return bool(self.items) != 0

    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        return f"Stack({self.items})"