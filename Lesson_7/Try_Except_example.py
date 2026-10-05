# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:46:42 2026

@author: mcamp


try:
    # codice che potrebbe generrare un errore
    eta = int(input("Quanti hanni hai?"))
    print(f"Hai {eta} anni!")
except ValueError:
    # queso e' eseguito in caso di errore
    print("Errore: devi inserire un numero intero, non del test!")
    

while True:
    
    try:
        peso = float(input ("inserisci il tupeso in kg (es.78.5):"))
        break # se arriviamo a questo punto, non ci sono erriri
    except ValueError:
        print("Input non valido!Usare valori numerici. Riprova!")
        
print (f"Ottimo, peso registrato: {peso} kg")


try: 
    numero = int(input("INserisci un numero:"))
    
except ValueError:
    print("Non é un numerp valido")
    
else: 
    print ("esatto! hai inserito un numero corretto")
    
finally:
    print("Programma terminato") # questo e' stapato in ogni caso!
    


try:
    numeratore =int(input("Inserisci il numeratore della divisione:"))
    denominatore = int(input("Inserisci il denominatore della diivisione:"))
    risultato=numeratore/denominatore
    print (f"il risulato della diivisione é : {risultato}")
except ValueError:
    print ("Errore: Hai inserito del testo o dei simboli invece di un numero intero!")
except ZeroDivisionError:
    print ("Erroe: Impossibile dividere per zero. scegli un altro denominatore!")
except Exception as e: 
    # cattura qualsiasi altro errore non considerato in precedenza
    print (f"Si e' verificato un errore imprevisto {e}") 
    
    

try:
    numeratore =int(input("Inserisci il numeratore della divisione:"))
    denominatore = int(input("Inserisci il denominatore della diivisione:"))
    risultato=numeratore/denominatore
    print (f"il risulato della diivisione é : {risultato}")
except (ValueError,ZeroDivisionError):
    print ("Si e' verificato un errore! bisogna inserire numeri validi") 
    


import math

# Inserire coefficenti dell'equazione ax^2+bx+c=0

while True:
    try:
        print("\n --- risolutore di equazione sendo grado ----")
        a = float (input("Inserisci il coefficente a: "))
        b = float (input("Inserisci il coefficente b: "))
        c = float (input("Inserisci il coefficente c: "))
        
        if  a==0 :
            print( "a = 0 , l'equazione di primo grado")
            x= -c/b
            print (f"x=: {x}")
        else:
            delta = (b**2) - (4*a*c)
            print(f"Delta calcolato: {delta}")
            if  delta>0:
        
                x1=(-b + math.sqrt(delta))/(2*a)
                x2=(-b - math.sqrt(delta))/(2*a)
                print(f"Due soluzioni reali e distinte: x1={x1} x2={x2}")
            elif delta==0:
        
                x=-b/(2*a)
                print (f"Due soluzioni uguali e coincidenti: x={x}")
        
            else: 
                print ("Il delta e' negativo. nessuna soluzione nel campo dei numeri reali")
                
                # se il codice arriva a questa riga senza , interrompe il ciclo con il break
            break
    except ValueError:
            print("Errore: Devi inserire dei numeri , non mettere o simboli! Riprova")
            
    except ZeroDivisionError:
            print ("Errore: a e b non possono esser entrambi zero")
            
"""

import math

def ottieni_coefficienti():
    print("Inserimento Dati")
    while True:
        try:
            print("\n --- risolutore di equazione sendo grado ----")
            a = float (input("Inserisci il coefficente a: "))
            b = float (input("Inserisci il coefficente b: "))
            c = float (input("Inserisci il coefficente c: "))
            return a,b,c # listruzione return esce dal ciclo while
        except ValueError:
            print("Errore: devi inserirre dei numeri. Riprova")
            
def calcola_soluzioni(a,b,c):
    if  a==0 :
        print( "a = 0 , l'equazione di primo grado")
        x= -c/b
        print (f"x=: {x}")
    else:
        delta = (b**2) - (4*a*c)
        print(f"Delta calcolato: {delta}")
        if  delta>0:
    
            x1=(-b + math.sqrt(delta))/(2*a)
            x2=(-b - math.sqrt(delta))/(2*a)
            print(f"Due soluzioni reali e distinte: x1={x1} x2={x2}")
        elif delta==0:
    
            x=-b/(2*a)
            print (f"Due soluzioni uguali e coincidenti: x={x}")
    
        else: 
            print ("Il delta e' negativo. nessuna soluzione nel campo dei numeri reali")
 
# fase di input  - Richiamo funzione           
 
coeff_a, coeff_b,coeff_c= ottieni_coefficienti() 

# fase di calcolo
calcola_soluzioni(coeff_a,coeff_b,coeff_c)





    
    
