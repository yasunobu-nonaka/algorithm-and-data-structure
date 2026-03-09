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


def quick_sort_with_comments(arr):
    if len(arr) <= 1:
        print(f"stop sorting {arr}")
        return arr

    print(f"start soring {arr}...")

    pivot = arr[-1]

    smaller = []
    larger = []

    print("target", pivot)

    for i in arr[:-1]:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)

    print("smaller: ", smaller)
    print("larger: ", larger)

    print("sort smaller")
    smaller = quick_sort_with_comments(smaller)
    print("--------------------------")
    print("sort larger")
    larger = quick_sort_with_comments(larger)

    sorted_arr = smaller + [pivot] + larger

    print("sorted_arr: ", sorted_arr)

    return sorted_arr


if __name__ == "__main__":
    import random

    arr = list(range(1, 11))
    random.shuffle(arr)

    print("Original: ", arr)

    result = quick_sort_with_comments(arr)
    print("Sorted: ", result)
