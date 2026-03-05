class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f'Stack({self.data})'

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print("pop", s.pop())
    print("peek", s.peek())
    print("size", s.size())
