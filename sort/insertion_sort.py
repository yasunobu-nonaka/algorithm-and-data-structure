def insertion_sort(my_list):
    if len(my_list) == 0:
        print("List is empty.")
        return None

    # ソート済みリスト
    sorted_list = []

    # リストの最初の要素のみを入れて初期化
    sorted_list.append(my_list[0])

    for i in range(1, len(my_list)):
        # リストから値を取り出す
        takenout = my_list[i]

        # ソート済みリストの値を左から比べる
        j = 0
        while j < len(sorted_list) and takenout > sorted_list[j]:
            j += 1

        sorted_list.insert(j, takenout)

    return sorted_list


if __name__ == "__main__":
    import random

    arr = list(range(1, 31))
    random.shuffle(arr)

    print("Original", arr)
    result = insertion_sort(arr)
    print("Result", result)
