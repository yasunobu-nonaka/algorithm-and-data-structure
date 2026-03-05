class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None

        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.data


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    print("peek", s.peek())
    s.push(20)
    print("peek", s.peek())
    s.push(30)
    print("peek", s.peek())

    print(s.pop())
    print(s.pop())
    print(s.pop())
