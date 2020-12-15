#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:18:12 2020

@author: thisjose
"""

A = [[1, 0, 0, 2, 0],[3.1, 4, 0, 5, 0],[-6.2, 0, 7, 8, -9.1],[0, 0, 10.3, 11, 0],[0, 0, 0, 0, 12.3]]
AA = []
JA = []
IA = []

m = 1
for i in A:
    n = 1
    for j in i:
        if(j != 0):
            IA.append(m)
            break
    for j in i:
        if(j != 0):
            JA.append(n)
            AA.append(j)
            m = m +1 
        n = n + 1
    
        
print(AA)
print(JA)
print(IA)