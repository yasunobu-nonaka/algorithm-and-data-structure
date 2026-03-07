def selection_sort_2(my_list):
    if len(my_list) == 0:
        print("List is empty.")
        return None

    n = len(my_list)

    for i in range(n):
        current_idx = i
        minimum = my_list[current_idx]

        for j in range(i + 1, n):
            if minimum > my_list[j]:
                current_idx = j
                minimum = my_list[current_idx]

        my_list[i], my_list[current_idx] = my_list[current_idx], my_list[i]

    return my_list


if __name__ == "__main__":
    arr = [2, 4, 5, 3, 1, 7, 6]
    result = selection_sort_2(arr)
    print(result)
