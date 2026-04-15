#!/usr/bin/env python3
__author__ = "Yash Tandon"
__date__ = "2026-04-14"

class BinaryTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def get_root_val(self):
        return self.value

    def set_root_val(self, new_val):
        self.value = new_val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def insert_left(self, new_left_child):
        new_node = BinaryTree(new_left_child)  
        if self.left is not None:
            new_node.left = self.left           
        self.left = new_node

    def insert_right(self, new_right_child):
        new_node = BinaryTree(new_right_child)  
        if self.right is not None:
            new_node.right = self.right         
        self.right = new_node

    def __str__(self):
        return (
            f"BinaryTree[key={self.value},"
            f"left_child={self.left},"
            f"right_child={self.right}]"
        )
