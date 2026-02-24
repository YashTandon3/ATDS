#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-02-12"

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if len(self.stack) == 0:
            return self.stack[-1]

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return str(self.queue)


class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)
    
    def remove_front(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)
    
    def remove_rear(self):
        if len(self.deque) > 0:
            return self.deque.pop()
    
    def peek_front(self):
        if len(self.deque) > 0:
            return self.deque[0]

    def peek_rear(self):
        if len(self.deque) >0:
            return self.deque[-1]

    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return len(self.deque) == 0


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def __repr__(self):
        return f"Node[data={self.data}]" + f"next={self.next}"




if __name__ == "__main__":
    pass