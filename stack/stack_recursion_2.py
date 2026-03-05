def test(n):
    if n == 0:
        print("A")
        return

    print("B", n)
    test(n - 1)
    print("C", n)


if __name__ == "__main__":
    test(2)
