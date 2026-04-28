#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-04-23"

from person import Person 

class BinaryHeap():
    def __init__(self):
        self.heap_list = [0]

    def insert(self, person):
        self.heap_list.append(person)
        self.percolate_up(len(self.heap_list) - 1)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i].get_vip_value() > self.heap_list[i // 2].get_vip_value():
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def del_max(self):
        if self.is_empty():
            return None
        max_val = self.heap_list[1]
        if self.size() == 1:
            self.heap_list.pop()
        else:
            self.heap_list[1] = self.heap_list.pop()
            self.percolate_down(1)
        return max_val

    def percolate_down(self, i):
        while (i * 2) <= len(self.heap_list) - 1:
            mc = self.max_child(i)
            if self.heap_list[i].get_vip_value() < self.heap_list[mc].get_vip_value():
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def max_child(self, i):
        if (i * 2 + 1) > len(self.heap_list) - 1:
            return i * 2
        else:
            if self.heap_list[i * 2].get_vip_value() > self.heap_list[i * 2 + 1].get_vip_value():
                return i * 2
            else:
                return i * 2 + 1

    def find_max(self):
        return self.heap_list[1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_persons):
        self.heap_list = [0] + list_of_persons[:]
        i = len(self.heap_list) // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def __str__(self):
        return "BinaryHeap[ " + " , ".join(str(p) for p in self.heap_list[1:]) + " ]"