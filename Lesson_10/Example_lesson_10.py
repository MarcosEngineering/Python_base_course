# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:14:44 2026

@author: mcamp
"""

# 1. Classe base (genitore)

class Veicolo:
    
    def __init__(self, marca, modello):
        self.marca= marca
        self.modello = modello
        
    # metodi generici che verranno sovrascitti (override)
    def muovi(self):
        print(f"il veicolo {self.marca} si sta muovendo")
        
    def suona_clacson (self):
        # usiamo pass perché vogliamo che le classi figlie definascano il suono
        pass
    
# 2. Classi derivate (figlie)

class Automobile(Veicolo):
    
    def muovi(self):
        print (f"L'automobile {self.marca} {self.modello} si muove su quattro ruote")
        
    def suona_clacson (self):
        print("Beep Beep!")
        
class Moto(Veicolo):
    
    def muovi(self):
        print (f"La moto {self.marca} {self.modello} si muove su due ruote e sfreccia nel traffico")
        
    def suona_clacson (self):
        print("Biip Bip!")
        
        
class Camion(Veicolo):
    
    def muovi(self):
        print (f"Il camion {self.marca} {self.modello}trasporta il carico a destinazione")
        
    def suona_clacson (self):
        print("Hoonk!!")
        
class Bici(Veicolo):
    
    def muovi(self):
        print (f"La bici {self.marca} {self.modello} viaggia sul percorso ciclabile")
        
    def suona_clacson (self):
        print("Driin Driin!!")
        
# poliformismo in azione

def test_veicolo (mezzo):
    mezzo.suona_clacson()
    mezzo.muovi()
    
    
# creiamo le istanze (oggetti)

mia_auto = Automobile ("Tesla", "Model 3")
mia_moto = Moto ("Yamaha", "MT-07")
mio_camion = Camion ("Volvo", "FH16")
mia_bici = Bici("Bianchi", "Aria")

# mettiamo tutti gli oggetti creati  in una lista
flotta = [mia_auto,mia_moto, mio_camion, mia_bici]

# cicliamo sulla lista la stessa funzione

for veicolo in flotta:
    test_veicolo(veicolo)



    
    
        

        
        