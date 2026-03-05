def countdown(n):
    print("enter:", n)

    if n == 0:
        return

    countdown(n - 1)

    print("exit:", n)


if __name__ == "__main__":
    countdown(3)
