#!/usr/bin/env python3
"""
selection_sort.py
Creates a list of random values and sorts them using the 
Selection Sort algorithm.
"""

import time
import random

def generate_random_numbers(length, range_of_values):
    """Generates a list of "length" integers randomly
    selected from the range 0 (inclusive) to 
    range_of_values (exclusive) and returns it to 
    the caller.
    """
    # write code here


def sort(nums):
    """Takes the list "nums" and sorts it using the
    Selection Sort algorithm.
    """
    # write code here


    
def display(a_list):
    """Prints out the list "a_list" on the screen. To
    be used for debugging, or displaying the initial
    and final state of the list.
    """
    # write code here



def main():
    NUM_OF_VALUES = 10
    nums = generate_random_numbers(NUM_OF_VALUES, 1000)
    display(nums)
    start = time.time()
    sort(nums)
    stop = time.time()
    display(nums)
    print("Sorted {0:10d} values, execution time: {1:10.5f} seconds".format(NUM_OF_VALUES, stop - start))

if __name__ == "__main__":
    main()