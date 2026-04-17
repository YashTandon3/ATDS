#!/usr/bin/env python3
__author__ = "Yash Tandon"
__date__ = "2026-04-14"

from atds import *


def build_parse_tree(tokens: list) -> BinaryTree:
    bt = BinaryTree(None)
    st = Stack()
    current = bt
    st.push(current)
    for token in tokens:
        if token == '(':
            current.insert_left(None)
            st.push(current)
            current = current.get_left_child()
        elif token in ('+', '-', '*', '/'):  
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


def evaluate(parse_tree: BinaryTree):
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        op = operators[parse_tree.get_root_val()]
        return op(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_val()


def main():
    fpe = "( 2 * 13 )"
    tokens = fpe.split(" ")
    bt = build_parse_tree(tokens)
    print(evaluate(bt))

if __name__ == "__main__":
    main()