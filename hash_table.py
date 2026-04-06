#!/usr/bin/env python3
__author__ = "Yash Tandon"
__date__ = "2026-03-18"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def __repr__(self):
        return str(self.slots) + "\n" + str(self.data)

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        i = self.hash_function(key)
        while self.slots[i] is not None and self.slots[i] != key:
            i = (i + 1) % self.size
        self.slots[i] = key
        self.data[i] = value

    def get(self, key):
        i = self.hash_function(key)
        start = i
        while self.slots[i] is not None:
            if self.slots[i] == key:
                return self.data[i]
            i = (i + 1) % self.size
            if i == start:
                break
        return None


def main():
    h = HashTable(7)
    h.put(8, "Adam")
    h.put(15, "Bob")
    print(h)
    print(h.get(8))
    print(h.get(99))
    h.put(22, "Cathy")
    h.put(1, "Dan")
    print(h.get(22))
    print(h.get(1))
    h.put(8, "Alex")
    print(h.get(8))
    print(h)


if __name__ == "__main__":
    main()