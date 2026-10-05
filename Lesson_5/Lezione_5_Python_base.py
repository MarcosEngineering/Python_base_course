# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 06:45:35 2026

@author: mcamp
"""

"""
# creare ulna lista

frutta = ["mela", "banana", "ciliegia"]

# accedere agli elementi della lista ( si inizia a contare da 0) 

print (frutta[1])

# modifica di un elemento

frutta[1]= "kiwi"

print (frutta[1])

#aggiungere un elmento alla lista

frutta.append("arancia")


print (frutta[3])

#rimuovere un elementi

frutta.remove("mela")

print (frutta[0])



#crere una tupla

coordinate = (45.0, 0.0)

print (coordinate[0])

coordinate[0]=15.0



import math

def calcola_distanza(punto_a, punto_b):
    
    somma_quadrati = sum((a-b)**2 for a,b, in zip (punto_a,punto_b))
    
    return math.sqrt(somma_quadrati)


def calcolo_punto_medio(punto_a,punto_b):
    
    return tuple((a+b)/2 for a,b in zip (punto_a,punto_b))
    
    

# inseriamo i dati di partenza

p1= (3.0,4.0,5.0)
p2 = (7.0,1.0,5.0)

distanza = calcola_distanza(p1,p2)

punto_medio = calcolo_punto_medio(p1,p2)


print(f"Cooordinata Punto 1: {p1}")

print(f"Cooordinata Punto 2: {p2}")

print (f"Distanza tra i punti : {distanza}")

print (f"Coordinate del punto medio : {punto_medio}")


# voliti iniziali nellla lista ( in trentesimi)

voti = [24,27,18,30,22]

print (f"Voti iniziali: {voti}")

voti.append(29)
voti.append (25)

print (f"Voti iniziali: {voti}")

voti[2]=20

print (f"Voti iniziali: {voti}")

# calcoli sulla lista

numero_studenti = len(voti)
somma_totale= sum(voti)
media = somma_totale/numero_studenti
voto_massimo= max(voti)
voto_minimo= min (voti)



print (f"Voti aggiornati: {voti}")
print(f"Numero di compiti validati: {numero_studenti}" )
print(f"Media voti della classe: {media:.2f}")
print(f"Voto piu' alto: {voto_massimo}")
print(f"Voto piu' basso: {voto_minimo}")

"""

# Create un set con dei duplicati intenzionalmente

colori= {"rosso", "blu", "verde", "rosso","giallo","blu"}

print(colori)

colori.add("viola")
colori.remove("verde")

print(colori)








