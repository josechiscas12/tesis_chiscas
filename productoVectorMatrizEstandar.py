#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:19:24 2020

@author: thisjose
"""

from time import time

A = [[1, 0, 0, 2, 0],[3.1, 4, 0, 5, 0],[-6.2, 0, 7, 8, -9.1],[0, 0, 10.3, 11, 0],[0, 0, 0, 0, 12.3]]
X = [1,2,3,4,5]
SALIDA = []

CONTADOR = 0;


tiempo_inicial = time() 
for i in A:
    acum = 0
    for j in list(range(len(i))):
        acum = acum + i[j]*X[j]
        CONTADOR = CONTADOR + 1
    SALIDA.append(acum)
tiempo_final = time()     

tiempo_ejecucion = tiempo_final - tiempo_inicial


print("SALIDA: ", SALIDA)
print("Tiempo de ejecucuion:  ", tiempo_ejecucion)
print("Multiplicaciones:  ", CONTADOR)
print("Endl")
