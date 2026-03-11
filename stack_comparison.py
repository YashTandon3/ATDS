#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-03-1"

from atds import *
import time
import matplotlib.pyplot as plt

""""
For this project, I had to measue the time it took to push
and pop items from the stack and unorderled list classes.
In each stack, I tested sizes from 100,000 to 1,000,000
while recording the time it took to push and pull items 
onto and off the stack. After graphing and visualzing the 
data, I found that the list stack was much faster than 
the unordered list stack. This difference is most likely due
to they ways that the 2 stacks use their memory. Lists are more
straightforward, appending elements more effiently, while the 
unordered list has to take extra steps to keep node connection.
Finally, both stacks are able to handle large numbers, but certain
operations are more efficient on the list stack.

"""""

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