def bubble_sort(my_list):
    n = len(my_list)
    is_continue = True

    while is_continue:
        replace_time = 0
        for i in range(n - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                replace_time += 1

        if replace_time > 0:
            is_continue = True
        else:
            is_continue = False

    return my_list


if __name__ == "__main__":
    # arr = [7, 4, 1, 2, 5, 3, 6]

    import random

    arr = list(range(1, 11))
    random.shuffle(arr)

    result = bubble_sort(arr)
    print("result: ", result)
