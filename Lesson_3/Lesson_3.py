# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 06:51:30 2026

@author: mcamp


numero=0

while numero < 20:

    numero+= 1

    if numero==3:
        continue # salta il blocco successivo e non stapera il 3
        
    print(f"numero={numero}")
    
    if numero == 7:
        
        print("il valore di numero e' uguale a 7")
        break # esce dal ciclo

"""

# definizione funzione calcolo MCD

def calcolo_mcd(a,b):
    
    a= abs(a)
    b= abs(b)
    
    while b!=0:
        
        resto = a % b
        print (f"Operazione {a} / {b} allora  resto ={resto}")
        
        a = b
        b  = resto
    return a
    
# testare la funzione
num1=1071
num2=462

risultato = calcolo_mcd(num1, num2)
print(f"il massimo comune divisore e' {risultato} ")