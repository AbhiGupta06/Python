# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:32:45 2019

@author: BSDU
"""
from collections import deque

queue = deque(["Ravi", "Tejas", "Aditya", "Jony"])
print(queue)

queue.append("Deep")
print(queue)

queue.append("Jony")
print(queue)

print(queue.popleft())
print(queue)

