#!/usr/bin/env python3
__author__ = "Yash Tandon"
__date__ = "2026-04-14"
import token

from atds import *


def build_parse_tree(tokens : list) -> BinaryTree:
    bt = BinaryTree(None)
    st = Stack()
    current = bt
    st.push(current)
    for token in tokens:
        if token == '(':
            current.insert_left(None)
            st.push(current)
            current = current.get_left_child()
        elif token in ('+-/*'):
            current.set_root_val(token)
            current.insert_right(None)
            st.push(current)
            current = current.get_right_child()
        elif token == ')':
            current = st.pop()
        else:
            current.set_root_val(int(token))
            current = st.pop()
    return bt
       
    


def main():
    fpe = "( 2 * 13 )"
    tokens = fpe.split(" ")
    bt = build_parse_tree(tokens)
    print(bt)

if __name__ == "__main__":
    main()