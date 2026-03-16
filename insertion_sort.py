#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-03-13"


def sort(arr):
    for start in range(1, len(arr)):
        j = start
        
        while j > 0 and arr[j] < arr[j - 1]:
            swap = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = swap
            j -= 1


def main():
    arr = [3, 7, 6, 2, 17, 4, 6]

    print("Before sorting:")
    print(arr)

    sort(arr)

    print("After sorting:")
    print(arr)


if __name__ == "__main__":
    main()