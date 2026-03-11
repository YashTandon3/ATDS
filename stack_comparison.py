#!/usr/bin/env python3

from atds import *
import time
import matplotlib.pyplot as plt


def testStackPush(s : Stack, n : int) -> float:
    start = time.time()
    for i in range(s):
        s.push(i)
    end = time.time()
    return end - start


def main():
    START = 100000
    END = 1000000
    STEP = (END - START) // 10
    x = []
    y = []
    for test_size in range(START, END, STEP):
        s = Stack()
        x.append(test_size)
        y.append(testStackPush(s, test_size))
        print(test_size, testStackPush(s, test_size))
        plt.plot(x, y, 'ro')
        plt.title("Run time vs stack size for a list-based stacks")
        plt.xlabel("Stack Size")
        plt.ylabel("Run Time (seconds)")
        plt.show()

if __name__ == "__main__":    
    main()