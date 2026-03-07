def insertion_sort(my_list):
    if len(my_list) == 0:
        print("List is empty.")
        return None

    # ソート済みリスト
    sorted = []

    # リストの最初の要素のみを入れて初期化
    sorted.append(my_list[0])

    for i in range(1, len(my_list)):
        # リストから値を取り出す
        takenout = my_list[i]

        # ソート済みリストの値を左から比べる
        j = 0
        item = sorted[j]
        while takenout > item:
            j += 1
            item = sorted[j]

        sorted.insert(j, takenout)

    return sorted


if __name__ == "__main__":
    arr = [10, 2, 4, 1, 5, 7]
    result = insertion_sort(arr)
    print(result)
