# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:26:31 2019

@author: BSDU
"""

import numpy as np

N = int(input("enter the values of n for NXN matrix:"))
mg = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
    mg[i,j]=n
    n += 1
    newi, newj = (i-1) % N, (j+1)% N
    if mg[newi, newj]:
        i += 1
    else:
        i,j = newi,newj
print(mg)