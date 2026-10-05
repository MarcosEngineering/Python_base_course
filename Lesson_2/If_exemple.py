# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
"""
anni=20

if anni< 18:
    
    print("Minorenne")
else:
    
    print("maggiorenne")
    


colore ="Rosso"  

if colore =="Rosso":
    print ("Stop")
    print ("Fermati")
elif colore =="Giallo":
    print ("Rallenta")
elif colore=="Verde":
    print("Avanti")
else:
    print("colore non valido! Semaforo guasto!")
    


anno= 2028

if (anno % 4==0  and anno %100 !=0) or (anno %400==0):
    
    print (f"l'anno {anno} e' bisestile ")
    
else:
    
    print (f"l'anno {anno}  non e' bisestile ")
    
    


lista_invitati = ["Pippo", "Paperino", "Paperone"]
invitato= "Topolino"


if invitato not in lista_invitati:
    print(f"{invitato} non e' stato invitato")
else:
   print(f"{invitato} e' stato invitato") 
   
"""


import math

# coefficenti dellequazione ax^2+bx+c=0

a= 1
b= 2.0
c= -4.0

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
        print ("Ildelta e' negativo. nessuna soluzione nel campo dei numeri reali")
        
    
    


    
    

