class MyQueue():
    """Pythonで学ぶアルゴリズムとデータ構造徹底理解 p.89"""

    def __init__(self):
        """Constructor for MyQueue"""
        self.que = []

    def __str__(self):
        return f"{self.que}"

    def enqueue(self, value):
        self.que.append(value)

    def dequeue(self):
        return self.que.pop(0)


if __name__ == "__main__":
    q = MyQueue()
    q.enqueue("process 1")
    q.enqueue("process 2")
    q.enqueue("process 3")
    q.dequeue()
    print(q)
