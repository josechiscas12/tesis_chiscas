#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:09:19 2020

@author: thisjose
"""
from time import time
AA = [1, 2, 3.1, 4, 5, -6.2, 7, 8, -9.1, 10.3, 11, 12.3] #Contienes los valores no nulos de la matriz
JA = [1, 4, 1, 2, 4, 1, 3, 4, 5, 3, 4, 5] # indicies de las columnas de AA
IA = [1, 3, 6, 10, 12,13]
X = [1, 2, 3, 4, 5]
SALIDA = []
CONTADOR = 0;


tiempo_inicial = time() 
for i in list(range(len(IA)-1)):
    acum = 0
    k1 = IA[i]
    k2 = IA[i+1]-1
    k3 = list(range(k1-1,k2))
    for j in k3:
        acum = acum + X[JA[j]-1]*AA[j]
        CONTADOR = CONTADOR + 1
    SALIDA.append(acum)
    
tiempo_final = time()     

tiempo_ejecucion = tiempo_final - tiempo_inicial
    

print("SALIDA: ", SALIDA)
print("Tiempo de ejecucuion:  ", tiempo_ejecucion)
print("Multiplicaciones:  ", CONTADOR)
print("Finalizado")
        
    
