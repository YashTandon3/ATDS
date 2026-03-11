#!/usr/bin/env python3


from atds import *
import time
import matplotlib.pyplot as plt

def test_push(stack_class, n):
    """Times n push operations for a given stack class."""
    s = stack_class()
    start = time.perf_counter()
    for i in range(n):
        s.push(i)
    end = time.perf_counter()
    return end - start

def test_pop(stack_class, n):
    """Times n pop operations for a given stack class."""
    s = stack_class()
    # Pre-fill the stack so we have items to pop
    for i in range(n):
        s.push(i)
    
    start = time.perf_counter()
    for i in range(n):
        s.pop()
    end = time.perf_counter()
    return end - start

def main():
    # Configuration
    SIZES = [10000, 20000, 30000, 40000, 50000]
    
    # Data storage
    results = {
        "Stack_Push": [],
        "ULStack_Push": [],
        "Stack_Pop": [],
        "ULStack_Pop": []
    }

    print(f"{'Size':>10} | {'Stack Push':>12} | {'ULStack Push':>12}")
    print("-" * 45)

    for n in SIZES:
        # Time Pushes
        t_stack_push = test_push(Stack, n)
        t_ulstack_push = test_push(Unordered_List_Stack, n)
        
        # Time Pops
        t_stack_pop = test_pop(Stack, n)
        t_ulstack_pop = test_pop(Unordered_List_Stack, n)
        
        results["Stack_Push"].append(t_stack_push)
        results["ULStack_Push"].append(t_ulstack_push)
        results["Stack_Pop"].append(t_stack_pop)
        results["ULStack_Pop"].append(t_ulstack_pop)

        print(f"{n:>10} | {t_stack_push:>11.4f}s | {t_ulstack_push:>11.4f}s")

    # Plotting the comparison
    plt.figure(figsize=(10, 5))
    
    # Push Comparison
    plt.subplot(1, 2, 1)
    plt.plot(SIZES, results["Stack_Push"], 'bo-', label='List Stack')
    plt.plot(SIZES, results["ULStack_Push"], 'ro-', label='UL Stack')
    plt.title("Push Performance")
    plt.xlabel("Number of Operations")
    plt.ylabel("Time (seconds)")