# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:33:19 2026

@author: mcamp
"""

# Esempio Ereditarieta' in Python

# 1. CLASSE BASE ( Genitore)

class Veicolo:
    def __init__ (self, marca, modello, anno):
        
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.in_moto = False
        
    def accendi_motore (self):
        if not self.in_moto:
            self.in_moto= True
            print(f"Il motore del veicolo {self.marca} é accesso.")
        else: 
            print ("il veicolo é gia accesso")
    def descrivi(self):
        print (f"Veicolo generico : {self.marca} {self.modello} del {self.anno}")
        
        
# 2. Classe derivata 1 (figlia)

class Automobile (Veicolo):
      
    def __init__ (self , marca, modello , anno, numero_porte):
        
        # usiamo la chiamata super per chiamare __init__ della classe genitore (veicolo)
        
        super().__init__(marca, modello,anno)
        
        self.numero_porte = numero_porte
        
    # Sovrascriviamo : specifico per l'automobile
        
    def descrivi (self):
        print (f"Autobile  a {self.numero_porte} porte: {self.marca} {self.modello} {self.anno}")
   
    # Metodo unico solo per l'automobile
    
    def apri_bagagliaio (self):
        print ("il bagagliaio della {self.modello} é aperto")

# 3. Classe derivata 2 (figlia)        
        
class Moto (Veicolo):
      
    def __init__ (self , marca, modello , anno, tipo_manubrio):
        
        # usiamo la chiamata super per chiamare __init__ della classe genitore (veicolo)
        
        super().__init__(marca, modello,anno) 
        
        self.tipo_manubrio = tipo_manubrio # attritbuto unico della moto
        
    def descrivi (self):
        print (f"Moto con manubrio {self.tipo_manubrio}: {self.marca} {self.modello} {self.anno}")
        
        
    # metodo unico per la moto
    
    def impenna(self):
        if self.in_moto:
            print(f"La moto {self.marca} sta impennando!")
            
        else:
            print("Devi prima accendere il mototore per impennare")
            
            
# Testiamo il codice


# creaiamov le istanze

mia_auto= Automobile ("Toyota", "Corolla", 2022,5)
mia_moto = Moto ("Ducati","Monster", 2023, "Sportivo")

print ("--- AUTOMOBILE --")

# un metodo EREDITATO dalla cllase Veicolo

mia_auto.accendi_motore()

# usiamo il metodo RIDEFINITO nella classe Atomobile
mia_auto.descrivi()

# usiamo il metodo specifico della classe Automobile

mia_auto.apri_bagagliaio()

# mia_auto.impenna ()  errore , l'auto no ha questo metodo

print ("--- MOTO --")

mia_moto.accendi_motore() # metodo ereditato
mia_moto.descrivi() # Metodo ridefinito
mia_moto.impenna() # Meto specifico per la classe moto













        
        
        
        
            
            