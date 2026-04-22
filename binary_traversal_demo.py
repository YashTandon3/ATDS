#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-04-21"

from atds import *

def isLeaf(t):
    return t.get_left_child() is None and t.get_right_child() is None

def preOrder(t, l:list):
    root = t.get_root_val()
    l.append(root)
    if t.get_left_child():
        preOrder(t.get_left_child(), l)
    if t.get_right_child():
        preOrder(t.get_right_child(), l)
    return l


def inOrder(t, l:list):
    if t.get_left_child():
        inOrder(t.get_left_child(), l)
    root = t.get_root_val()
    l.append(root)
    if t.get_right_child():
        inOrder(t.get_right_child(), l)
    return l

def postOrder(t, l:list):
    if t.get_left_child():
        postOrder(t.get_left_child(), l)
    if t.get_right_child():
        postOrder(t.get_right_child(), l)
    l.append(t.get_root_val())
    return l

def main():
    t = BinaryTree("a")
    t.insert_left("b")
    t.insert_right("c")
    t.get_left_child().insert_left("d")
    t.get_left_child().insert_right("e")
    t.get_right_child().insert_left("f")
    t.get_right_child().insert_right("g")

    print("Pre-order: ", preOrder(t, []))
    print("In-order: ", inOrder(t, []))
    print("Post-order: ", postOrder(t, []))

if __name__ == "__main__":
    main()