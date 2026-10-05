# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:23:35 2026

@author: mcamp
"""

# 1.classe base 
class Veicolo:
    def __init__(self, marca,modello):
        self.marca = marca
        self.modello= modello
        
        # metodi generici che verrammo sovrascritti
        
        def muovi(self):
            print(f"IL veicolo{self.marca} si sta muovendo")
            
        def suona_clacson(self):
            # usiammo pass perché volgliamo le sottoclassi definiscano il suono
            pass
        
        
# CLassi derivate 
class Automobile(Veicolo):
   
    def muovi (self):
        print(f"L'automobile {self.marca} {self.modello} viaggia su quattro ruote")
        
        
    def suona_clacson(self):
        print("Beep beep!")
        
        
class Moto(Veicolo):
   
    def muovi (self):
        print(f"La moto {self.marca} {self.modello} viaggia su due ruote")
        
        
    def suona_clacson(self):
        print("Bip bip!")
        
class Camion(Veicolo):
   
    def muovi (self):
        print(f"Il camion {self.marca} {self.modello} trasporta il carico  a destinazion")
        
        
    def suona_clacson(self):
        print("Hook Hook!") 
        
class bicicletta(Veicolo):
                 
    def muovi (self):
         print(f"la bicicletta {self.marca} {self.modello} va nel parco")
                     
    def suona_clacson(self):
         print("Drin Drin!")
        
#  Applicazione de polimorfismo

# funzione generica che accetta qualsiasi veicolo (automobile, Moto,Camion)

def Test_veicolo(mezzo):
     mezzo.suona_clacson()
     mezzo.muovi()
     
# Creaiono le istanze (oggetti)
     
mia_auto = Automobile("Tesla", "Model 3")
mia_moto = Moto("Yamaha", "MT-07")
mio_camion = Camion("Volvo", "FH16")
mia_bici = bicicletta("Bianchi","Da corsa")

# inseriamo tutti gli oggetti in un'unica lista

flotta = [mia_auto,mia_moto,mio_camion,mia_bici]

for veicolo in flotta:
    Test_veicolo(veicolo)
     
     
    
     
    
    
        
        
    
    
        
            