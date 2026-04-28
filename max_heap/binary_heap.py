#!/usr/bin/env python3
"""
binary_heap.py
This demonstration uses a list to build and maintain a minHeap tree.
@author Yash Tandon
@version 2017-04-24
"""

class BinaryHeap():
    """The BinaryHeap class implements the Binary Heap Abstract 
    Data Type as a list of values, where the index p of a parent
    can be calculated from the index c of a child as c // 2.
    """
    def __init__(self):
        self.heap_list = [0]  # not used. Here just to make parent-
                             # child calculations work nicely.
        # Note that current size of heap = len(self.heapList) - 1

    def insert(self,value):
        """Inserts a value into the heap by:
        a. adding it to the end of the list, and then
        b. "percolating" it up to an appropriate position
        """
        self.heap_list.append(value)
        self.percolate_up(len(self.heap_list) - 1)


    def percolate_up(self, i):
        """Beginning at i, check to see if parent above is greater than
        value at i. If so, percolate i upwards to parent's position.
        """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def del_min(self):
        """This is a bit trickier. It's easy to return the minimum item,
        the first item on the list, but how do we readjust the heap then?
        """
        if self.is_empty():
            raise IndexError("del_min() called on empty heap")
        min_val = self.heap_list[1]
        if self.size() == 1:
            self.heap_list.pop()
        else:
            self.heap_list[1] = self.heap_list.pop()
            self.percolate_down(1)
        return min_val

    def percolate_down(self,i):
        """Moves the item at i down to a correct level in the heap. To
        work correctly, needs to identify the minimum child for parent i.
        """
        while (i * 2) <= len(self.heap_list) - 1:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if (i * 2 + 1) > len(self.heap_list) - 1:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def find_min(self):
        """Returns the minimum item in the heap, without removing it.
        """
        return self.heap_list[1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_keys):
        """Returns a new heap based on a pre-existing list of key values."""
        self.heap_list = [0] + list_of_keys[:]
        i = len(self.heap_list) // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)

def main():
    print("Demonstrating minHeap binary tree")
    bh = BinaryHeap()
    bh.insert(5)
    print(bh)
    '''
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(1)
    bh.insert(50)
    bh.insert(15)
    print(bh)
    print(bh.find_min())
    print(bh.del_min())
    print(bh)
    '''

if __name__ == "__main__":
    main()