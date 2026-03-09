def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    import random

    arr = list(range(1, 31))
    random.shuffle(arr)
    print("Original: ", arr)
    print("Sorted: ", bubble_sort(arr))
