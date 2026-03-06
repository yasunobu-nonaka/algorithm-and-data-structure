class MyQueue():
    """
    リングバインダーの実装
    """

    def __init__(self, N):
        self.N = N
        self.que = [None] * N
        self.head = 0
        self.tail = 0
        self.count = 0

    def __str__(self):
        return ("(head:{head}, tail:{tail}), {que}"
                .format(head=self.head, tail=self.tail, que=self.que))

    def enqueue(self, value):
        if self.count == self.N:
            print("Failed to enqueue because que is full.")
            return None

        # キューの最後尾に値を設定
        self.que[self.tail] = value

        # データ件数+1
        self.count += 1

        # キューの最後尾の位置をひとつ後ろにずらす
        self.tail = (self.tail + 1) % self.N

    def dequeue(self):
        # 空のキューであった場合デキュー失敗
        if self.que == [None] * self.N:
            print("Failed to dequeue because que is empty.")
            return None

        value = self.que[self.head]

        # キューのヘッドの値を削除
        self.que[self.head] = None

        # データ件数-1
        self.count -= 1

        # キューのヘッドの位置を一つ後ろにずらす
        self.head = (self.head + 1) % self.N

        return value


if __name__ == "__main__":
    q = MyQueue(4)
    q.enqueue("Process 1")
    q.enqueue("Process 2")
    q.enqueue("Process 3")
    print(q)

    print("Dequeue", q.dequeue())
    print(q)
    print("Dequeue", q.dequeue())
    print(q)

    q.enqueue("Process 4")
    q.enqueue("Process 5")
    print(q)

    print("Dequeue", q.dequeue())
    print("Dequeue", q.dequeue())
    print(q)
