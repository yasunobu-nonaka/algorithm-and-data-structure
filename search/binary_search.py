def binary_search_bool(arr, target):
    if len(arr) == 0:
        return False

    n = len(arr)
    mid_idx = n // 2
    if target < arr[mid_idx]:
        left_arr = arr[:mid_idx]
        return binary_search_bool(left_arr, target)
    elif arr[mid_idx] < target:
        right_arr = arr[mid_idx + 1:]
        return binary_search_bool(right_arr, target)
    elif arr[mid_idx] == target:
        return True


def binary_search_index(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = list(range(1, 11))
    print(arr)
    result = binary_search_bool(arr, 10)
    print(result)
