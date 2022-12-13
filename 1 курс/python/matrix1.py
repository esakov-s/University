#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np
import math as mt


def addition(a, b):
    if np.shape(a) != np.shape(b):
        return -1
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = a[i][j] + b[i][j]
    return (a)

def multipl(a, b):
    if len(a[0]) != len(b):
        return -1
    c = [[]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i].append(0)
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
        if i == len(a) - 1:
            break
        c.append([])
    return (c)
def transpos(a):
    return(a.transpose())






