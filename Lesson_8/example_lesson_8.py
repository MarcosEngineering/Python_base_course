# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 06:38:44 2026

@author: mcamp
"""

class Automobile:
    
    # il metodo costruttore per inizialzzare i dati dell'auto (attributi)
    
    def __init__ (self,marca,modello,anno):
        
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.in_moto = False # Impostazione predefinita iniziale
        
    # un metodo che fa compiere un azione all'auto
    
    def accendi (self):
        
        if not self.in_moto:
            self.in_moto = True
            print (f"il motore della {self.marca} {self.modello} é accesso")
                   
        else:
            print("L'auto é gia accesa")
            
    # metodo descrizione dell'oggetto
    
    def mostra_dettagli(self):
        
        print (f"Questa é una {self.marca} {self.modello} costruita nel {self.anno}")
        
        
# creazione oggetti (istanze) della classe automobile

auto1= Automobile("Fiat", "Panda", 2018)
auto2= Automobile("Tesla", "Model 3", 2023)

# accedere agli attributi usando la sintassi del punto

print(auto1.marca)
print(auto2.anno)


# richiamare i metodi

auto2.mostra_dettagli()

auto1.accendi()
auto1.accendi()

            
            
            