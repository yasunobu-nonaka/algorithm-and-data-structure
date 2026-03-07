def selection_sort(my_list):
    if len(my_list) == 0:
        print("List is empty.")
        return None

    sorted_list = []

    while len(my_list) > 0:
        minimum = min(my_list)
        my_list.remove(minimum)
        sorted_list.append(minimum)

    return sorted_list


if __name__ == "__main__":
    arr = [2, 4, 5, 3, 1, 7, 6]

    result = selection_sort(arr)
    print(result)
