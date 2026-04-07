#!/usr/bin/env python3
__author__ = "Yash Tandon"
__date__ = "2026-04-06"

from atds import Stack
import random

tasks = [ ['read work emails',10],
          ['respond to emails', 10],
          ['attend meeting', 15],
          ['coffee break', 15],
          ['talk to boss', 10],
          ['read work emails',10],
          ['respond to emails', 10],
          ['conference call', 15],
          ['conversation with colleague', 15],
          ['coffee break', 15],
          ['meet with student', 15] ]

WORKDAY_MINUTES = 180

s = Stack()
clock = 0
task_num = 0
current_task = None

while clock < WORKDAY_MINUTES:

    print("Current time is", clock, "and current task is", current_task)
    print("Items on stack are:", s)

    if task_num < len(tasks) and random.randrange(10) == 0:
        print("New task coming in...!")
        new_task = tasks[task_num][:]
        task_num += 1

        if current_task is None:
            current_task = new_task
        else:
            s.push(current_task)
            current_task = new_task

    if current_task is not None:
        current_task[1] -= 1

        if current_task[1] == 0:
            print("Done with task:", current_task[0])
            current_task = None

            if not s.is_empty():
                current_task = s.pop()

    input("[Enter] to continue...")
    print("------------")

    clock += 1