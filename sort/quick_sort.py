def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = []
    larger = []

    for i in arr[:-1]:
        if i < pivot:
            smaller.append(i)
        else:
            larger.append(i)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


if __name__ == "__main__":
    import random

    arr = list(range(1, 11))
    random.shuffle(arr)

    print("Original: ", arr)

    result = quick_sort(arr)
    print("Sorted: ", result)
