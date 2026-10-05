# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:10:46 2026

@author: mcamp
"""

class Automobile:
    def __init__ (self, marca,modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno= anno
        
        # attributo PRIVATO (Incapsulamento). ininia  con __
        self.__chilometraggio =0
        
    #1: GETTER : Metodo per permetter all'esterno di Leggere il dato in modo sicuro
    def leggi_chilometraggio(self):
        print(f"L'auto ha perocrso {self.__chilometraggio} km")
        return self.__chilometraggio
    
    #2: SETTER: un metodo controllato  per modificare il dato
    def guida(self, chilometri):
        # aggiungiamo una logica di controllo: i km non possono esser negativi
        if chilometri>= 0:
            self.__chilometraggio+= chilometri
            print (f"Hai guidato per {chilometri} km.")
        else:
            print("Errore: Non si puo percorrere una distanza negativa!")
            
# Creiamo l'oggetto

mia_auto = Automobile("Fiat", "Panda",2010)

# uso corretto dell'incapsulamento

mia_auto.leggi_chilometraggio()

# 

mia_auto.guida(50)

mia_auto.leggi_chilometraggio()
mia_auto.guida(-20)

mia_auto.guida(100)
mia_auto.leggi_chilometraggio()

# tentattivo di forzare il valore del chilometraggio dall'esterno
mia_auto.__chilometraggio=10


mia_auto.leggi_chilometraggio() # chack : tentativo ignorato.


        
    