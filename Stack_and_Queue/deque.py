# Doule Ended Queue
"""
A deque, short for double-ended queue, is a versatile data structure in Python's collections module that allows for efficient addition and removal of elements from both the left and right ends.

Key methods include:
append(item): Adds an item to the right end.
appendleft(item): Adds an item to the left end.
pop(): Removes and returns the item from the right end.
popleft(): Removes and returns the item from the left end.
extend(iterable): Adds multiple elements to the right end.
extendleft(iterable): Adds multiple elements to the left end (note: the iterable's elements are added in reverse order).
rotate(n): Rotates the deque n steps to the right (or left if n is negative).
clear(): Removes all elements.
"""

from collections import deque

lst = deque([])

lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
print(lst)
lst.appendleft(0)
print(lst)
lst.pop()
print(lst)
lst.popleft()
print(lst)
lst.extend([6, 7, 8, 9, 10])
print(lst)
lst.extendleft([11, 12, 13, 14, 15])
print(lst)
lst.rotate(2)
print(lst)
lst.rotate(-2)
print(lst)
lst.clear()
print(lst)
