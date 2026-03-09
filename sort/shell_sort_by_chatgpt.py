def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr


if __name__ == "__main__":
    arr = [2, 4, 5, 3, 1, 7, 6]
    result = shell_sort(arr)
    print(result)
