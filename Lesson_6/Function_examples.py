# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 08:43:11 2026

@author: mcamp


def saluta():
    
    print("Ciaio! Benvenuto nella lezione di Python!")
    
    
# chiamata funzione

saluta()


def presentazione(nome, eta=18):
    
    print(f"Mi chiamo {nome} e' ho {eta} anni")
    
# chiamata funzione con parametri

presentazione("Giulio", 30)

presentazione("Giulia", 45)


presentazione("Francesco", 60)





def calcola_area_rettangolo (base, altezza):
    
    area = base *altezza
    return area

def calcola_perimetro_rettangolo (base, altezza):
    
    perimetro = 2*(base + altezza)
    return perimetro

# chiamata funzione con parametri e la restituzione del risulato della funzione

risultato_a = calcola_area_rettangolo (5, 4)

print (f"L'area calcolata è: {risultato_a}")


risultato_p = calcola_perimetro_rettangolo (5, 4)

print (f"IL perimetro calcolato è: {risultato_p}")



def somma_numeri(*args):
    
    totale = sum(args)
    
    return totale

# chiamata funzione con un numero indefinito di parametri


somma = somma_numeri( 1,2,3,4,5)
print (f"La somma é {somma}")

somma_1 = somma_numeri(6,7)
print (f"La somma é {somma_1}")

"""

profilo_utente = {
    
    "nome": "Anna",
    "ruolo": "Admin",
    "Livello": 5,
    "eta'":25
     
    }

def mostra_profilo (**kwargs):
    for chiave, valore in kwargs.items():
        
        print(f"{chiave}: {valore}")
        

# chiamata funzione con un dizionario

mostra_profilo(**profilo_utente)

    