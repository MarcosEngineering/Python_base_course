# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:00:59 2026

@author: mcamp
"""

from abc import ABC, abstractmethod

# 1. CLASSE astratta (il nostro "contratto")

class Veicolo(ABC):
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    # Questo è un metodo astratto - usiamo pass.
    # È fondamentale che sia a livello di classe, non dentro __init__
    @abstractmethod
    def avvia_motore(self):
        pass

    # Questo è un metodo "normale" (concreto), ereditato così com'è.
    def descrivi(self):
        # Corretto: aggiunto uno spazio tra marca e modello per leggibilità
        print(f"Questo è un veicolo {self.marca} {self.modello}.")

# 2. CLASSI figlie (devono rispettare il nostro "contratto")

class Automobile(Veicolo):
    def avvia_motore(self):
        # Corretto il refuso 'acecnsione' in 'accensione'
        print ("Giro la chiave di accensione e l'automobile è avviata!")

class Moto(Veicolo):
    def avvia_motore(self):
        print ("Premo lo starter elettrico e la moto è avviata!")

# --- TESTIAMO L'ASTRAZIONE ---

# Creiamo istanze delle classi concrete che hanno implementato i metodi astratti
mia_auto = Automobile("Fiat", "Cinquecento")
mia_moto = Moto("Ducati", "Monster")

# Usiamo un metodo concreto ereditato dalla classe astratta
mia_auto.descrivi()

# Usiamo il metodo che ogni classe ha dovuto implementare a modo suo
mia_auto.avvia_motore()
mia_moto.avvia_motore()

# TENTATIVO ERRATO:
# Non possiamo creare un "Veicolo" generico. Se de-commenti la riga qui sotto, 
# Python restituirà un TypeError (Can't instantiate abstract class).
veicolo_misterioso = Veicolo("MarcaIgnota", "ModelloX")