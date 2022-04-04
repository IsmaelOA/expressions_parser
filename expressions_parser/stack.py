

class Stack:
    '''
        Stack class
    '''
    def __init__(self):
        self.items = list()
        
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    @property
    def size(self):
        return len(self.items)
    
    @property
    def empty(self):
        return self.size == 0

    def peek(self):
        if self.empty:
            raise Exception("Can't pop a value, stack is empty")
        return self.items[0]
    
    def show(self):
        out = ''
        for idx in range(self.size):
            out += str(self.items[idx]) + " \n↓\n" if idx != self.size -1 else str(self.items[idx])
        print(out)

    def __str__(self):
        return 'Stack at {} with {} elements'.format(
            hex(id(self)), self.size
        )

    def __repr__(self):
        return str(self.items)
