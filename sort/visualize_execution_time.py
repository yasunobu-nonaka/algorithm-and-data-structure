from insertion_sort import insertion_sort

import random
import time
import matplotlib.pyplot as plt


def visualize_insertion_sort_execution_time():
    lengths = [100, 200, 400, 800, 1600, 3200]
    times = []

    for n in lengths:
        start = time.perf_counter()

        arr = list(range(1, n))
        random.shuffle(arr)

        insertion_sort(arr)
        end = time.perf_counter()

        times.append(end - start)

    plt.plot(lengths, times, ".")
    plt.xlabel("n")
    plt.ylabel("time")

    plt.show()


if __name__ == "__main__":
    visualize_insertion_sort_execution_time()
