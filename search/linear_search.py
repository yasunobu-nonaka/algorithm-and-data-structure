def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index

    return None


if __name__ == "__main__":
    arr = ["apple", "banana", "kiwi", "grape", "strawberry"]

    result = linear_search(arr, "grape")
    print(result)
