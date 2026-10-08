# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 06:51:30 2026

@author: mcamp
"""

import math

# 1. Definiamo il valore del raggio (m)
testo_raggio = input("Inserisci il valore del raggio:")
raggio=float(testo_raggio)

# 2. calcoliamo il perimetro e l'area del cerchio

perimetro= 2*math.pi*raggio
area = math.pi*(raggio**2)

# 3. Stampiamo i risultati del cancolo nella console
print("--- calcolare valori del cerchio  ---")
print(f"Raggio: {raggio}")
print(f"Perimetro: {perimetro:.2f}")
print (f"Area:{area:.2f}")