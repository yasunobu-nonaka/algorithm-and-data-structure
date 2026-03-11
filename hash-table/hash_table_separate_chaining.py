from utils import my_hash_func


class Node():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return f'{self.value} - {self.next}'
        else:
            return f'{self.value}'


class MyHashTable():
    def __init__(self):
        self.size = 100
        self.data = [None] * self.size

    def __str__(self):
        result = ""
        for index, item in enumerate(self.data):
            if item:
                result += f"{index}:{item}\n"
        return result

    def set(self, key, value):
        hash_key = my_hash_func(key) % self.size
        node = self.data[hash_key]

        if node is None:
            self.data[hash_key] = Node(key, value)
            return

        while node:
            if node.key == key:
                node.value = value
                return
            if node.next is None:
                break

            node = node.next

        node.next = Node(key, value)

    def get(self, key):
        hash_key = my_hash_func(key) % self.size
        node = self.data[hash_key]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def delete(self, key):
        hash_key = my_hash_func(key) % self.size
        node = self.data[hash_key]
        prev = None

        while node:
            if node.key == key:
                if prev is None:
                    self.data[hash_key] = node.next
                else:
                    prev.next = node.next

                return node.value

            prev = node
            node = node.next

        return None


if __name__ == "__main__":
    htable = MyHashTable()
    htable.set("abc", "vone")
    htable.set("bca", "vtwo")
    htable.set("cab", "vthree")
    print(htable.get("abc"))
    print(htable.get("bca"))
    print(htable.get("cab"))
    print("Delete", htable.delete("bca"))
    print("\n")
    print(htable)
