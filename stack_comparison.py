#!/usr/bin/env python3

from atds import *
import time
import matplotlib.pyplot as plt


def testStackPush(s, n):
    start = time.time()
    for i in range(n):
        s.push(i)
    end = time.time()
    return end - start


def main():
    START = 100000
    END = 1000000
    STEP = (END - START) // 10

    x = []
    y_list = []
    y_ul = []

    for test_size in range(START, END, STEP):

        s1 = Stack()
        s2 = Unordered_List_Stack()

        t1 = testStackPush(s1, test_size)
        t2 = testStackPush(s2, test_size)

        x.append(test_size)
        y_list.append(t1)
        y_ul.append(t2)

        print(test_size, t1, t2)

    plt.plot(x, y_list, 'ro', label="List Stack")
    plt.plot(x, y_ul, 'bo', label="UnorderedList Stack")

    plt.title("Run Time vs Stack Size")
    plt.xlabel("Stack Size")
    plt.ylabel("Run Time (seconds)")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()