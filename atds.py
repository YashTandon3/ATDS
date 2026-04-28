#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-02-12"

from turtle import pos


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if len(self.stack) > 0:
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


class UnorderedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def __repr__(self):
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result += "]"
        return result

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count

    def is_empty(self):
        return self.head == None

    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                    current = self.head
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:
                previous = current
                current = current.get_next()

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)

    def index(self, item):
        current = self.head
        position = 0
        while current != None:
            if current.get_data() == item:
                return position
            current = current.get_next()
            position += 1
        return None

    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
            return
        current = self.head
        previous = None
        position = 0
        while current != None and position < pos:
            previous = current
            current = current.get_next()
            position += 1
        new_node.set_next(current)
        previous.set_next(new_node)

    def pop(self, pos=None):
        if self.head == None:
            return None
        if pos == None:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            if previous == None:
                self.head = None
            else:
                previous.set_next(None)
            return current.get_data()
        current = self.head
        previous = None
        position = 0
        while current != None and position < pos:
            previous = current
            current = current.get_next()
            position += 1
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return current.get_data()

class Unordered_List_Stack():
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        self.ul.add(item)

    def pop(self):
        return self.ul.pop()

    def peek(self):
        if not self.ul.is_empty():
            return self.ul.head.get_data()

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()

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

class LinearSearcher:
    def search(self, numbers, target):
        for i, num in enumerate(numbers):
            if num == target:
                return i
        return None
    
class BinarySearcher:
    def search(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return None

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
            f"BinaryTree(key={self.value}, "
            f"left={self.left.value if self.left else None}, "
            f"right={self.right.value if self.right else None})"
        )


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
    print("Testing the UnorderedList class")
    tests_passed = 0
    try:
        ul = UnorderedList()
        tests_passed += 1
        print("Test passed: UnorderedList object created")
    except:
        print("Test failed: couldn't create UnorderedList object")

    try:
        if ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method detected empty list")
        else:
            print("Test failed: .is_empty() method didn't understand that list is empty")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 0:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 0")
        else:
            print("Test failed: .length() didn't identify a length of 0")
    except:
        print("Test failed: .length() method unavailable")
        
    try:
        ul.add(4)
        ul.add(3)
        ul.add(2)
        ul.add(1)
        ul.add(0)
        tests_passed += 1
        print("Test passed: five items added")
    except:
        print("Test failed: couldn't add items")
    
    try:
        if not ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method identified that list is no longer empty")
        else:
            print("Test failed: .is_empty() method thought list was empty, and it isn't")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 5:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 5")
        else:
            print("Test failed: .length() didn't identify a length of 5")
    except:
        print("Test failed: .length() method unusable")
     
    try:
        result = str(ul)         # Try using __repr__
        if result == "UnorderedList[0,1,2,3,4,]":
            tests_passed += 1
            print("Test passed: __repr__ returning correct values:")
            print(result)
        else:
            print("Test failed: __repr__ returned " + result)
            print("Expected: UnorderedList[0,1,2,3,4,]")
        
    except:
        print("Test failed: couldn't reference __repr__ method")
    
    try:
        if not ul.search(5):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 5 isn't on list")
        else:
            print("Test failed: .search() method thought 5 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
        
    try:
        if ul.search(3):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 3 is on list")
        else:
            print("Test failed: .search() method thought 3 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
    
    try:
        ul.remove(0)
        if str(ul) == "UnorderedList[1,2,3,4,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from beginning of list")
        else:
            print("Test failed: .remove() didn't remove item from beginning of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from middle of list")
        else:
            print("Test failed: .remove() didn't remove item from middle of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
        
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(2)
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from end of list")
        else:
            print("Test failed: .remove() didn't remove item from end of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(3)
        if str(ul) == "UnorderedList[0,1,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully didn't remove item from list")
        else:
            print("Test failed: .remove() failed in not removing a non-existent item from list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(0)
        ul.add(1)
        ul.add(0)
        print("Attempting multiple remove")
        print("Before remove: " + str(ul))
        ul.remove(0)
        print("After remove: " + str(ul))
        result = ul.search(0)
        if not result:
            tests_passed += 1
            print("Test passed: .remove() successfully removed multiple items")
        else:
            print("Test failed: .remove() didn't remove multiple items")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.append(3)
        if str(ul) == "UnorderedList[0,1,2,3,]":
            tests_passed += 1
            print("Test passed: .append() successfully appended item to list")
        else:
            print("Test failed: .append() didn't append item to list")
    except:
        print("Test failed: .append() method unavailable or not working?")
    
    try:
        result = ul.index(1)
        if result == 1:
            tests_passed += 1
            print("Test passed: .index() successfully found item on list")
        else:
            print("Test failed: .index() failed to find item on list")
    except:
        print("Test failed: .index() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.insert(0, -1)
        if str(ul) == "UnorderedList[-1,0,1,2,]":
            tests_passed += 1
            print("Test passed: .insert() successfully inserted value at beginning of list")
        else:
            print("Test failed: .insert() didn't correctly insert at beginning of list")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.insert(2,3)
        if str(ul) == "UnorderedList[0,1,3,2,]":
            tests_passed += 1
            print("Test passed: .insert() successfully inserted values in middle of list")
        else:
            print("Test failed: .insert() didn't correctly insert values in middle of list")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop()
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .pop() successfully removed last item from list")
        else:
            print("Test failed: .pop() didn't remove last item from list correctly")
    except:
        print("Test failed: .pop() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(0)
        if str(ul) == "UnorderedList[1,2,]":
            tests_passed += 1
            print("Test passed: .pop(0) successfully removed first item from list")
        else:
            print("Test failed: .pop(0) didn't remove first item from list correctly")
    except:
        print("Test failed: .pop(0) method unavailable? (or __repr__ not working?)")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .pop(1) successfully removed item from middle of list")
        else:
            print("Test failed: .pop(1) didn't remove last item from middle of list correctly")
    except:
        print("Test failed: .pop(1) method unavailable? (or __repr__ not working?)")


        
    print(str(tests_passed) + "/21 tests passed on the UnorderedList class")
    

if __name__ == "__main__":
    main()