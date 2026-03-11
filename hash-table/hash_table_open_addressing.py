from utils import my_hash_func


class Node():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return "{key}:{value}".format(key=self.key, value=self.value)


class MyHashTable:
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
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None or node.key == "-":
                self.data[hash_key] = Node(key, value)
                print(f"Set Node({key}, {value})")
                return
            hash_key += 1
        print("No empty space found")

    def get(self, key):
        hash_key = my_hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None:
                print("No data found")
                return
            elif node.key == key:
                return node.value
            hash_key += 1

        return self.data[hash_key]

    def delete(self, key):
        hash_key = my_hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None:
                print("Failed to delete because target not found")
                return
            elif node.key == key:
                self.data[hash_key] = Node("-", None)
                print(f'key "{key}" has been  deleted successfully.')
                return
            hash_key += 1


if __name__ == "__main__":
    htable = MyHashTable()
    htable.set("one", 100)
    htable.set("two", 200)
    htable.set("three", 300)
    htable.set("four", 400)
    htable.set("five", 500)
    print("\n")

    print("get two => ", htable.get("two"))
    print("get four => ", htable.get("four"))
    htable.delete("four")
    print("get four => ", htable.get("four"))
    print("get five => ", htable.get("five"))
    print("\n")
    print("Print Hash Table")
    print(htable)
