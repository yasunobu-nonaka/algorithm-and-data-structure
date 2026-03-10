from string import ascii_letters


def my_hash_func(text):
    hash_num = 0
    for c in text:
        hash_num += ascii_letters.index(c)
    return hash_num


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
        self.data[hash_key] = Node(key, value)

    def get(self, key):
        hash_key = my_hash_func(key) % self.size
        return self.data[hash_key]

    def delete(self, key):
        hash_key = my_hash_func(key) % self.size
        self.data[hash_key] = None


if __name__ == "__main__":
    htable = MyHashTable()
    htable.set("one", 100)
    htable.set("two", 200)
    htable.set("three", 300)
    htable.set("four", 400)
    print("four", htable.get("four"))
    htable.delete("four")
    print("four", htable.get("four"))
    print(htable)
