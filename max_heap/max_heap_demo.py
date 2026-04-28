#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-04-23"

from person import Person
from max_heap import BinaryHeap

def main():
    print("Welcome to the BinaryHeap of the Stars!")
    print("Where you can get in line, but you may *never*")
    print("get to the top of the heap.")
    print()

    vip_list = [
        Person("Patty", 10),
        Person("Dexter", 17),
        Person("Zetlian", 12),
        Person("Schmoke", 23),
        Person("Carrie", 100),
    ]

    heap = BinaryHeap()
    heap.build_heap(vip_list)
    print(heap)

    print("Adding a star")
    heap.insert(Person("Tsai", 30))
    print(heap)

    print(f"Most Important VIP (findMax()): {heap.find_max()}")
    print(f"Admitting VIP (delMax()): {heap.del_max()}")
    print(f"Remaining queue: {heap}")

    print("Admitting remaining VIPs in order:")
    while not heap.is_empty():
        print(heap.del_max())

    print(f"VIPs remaining: {heap.size()}")

main()