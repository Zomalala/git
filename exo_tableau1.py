#!/usr/local/bin/python3.9

#-*-coding:UTF-8-*-

import random
tableau_jeu=[]

#initialisation d'une liste de 10 éléments

for i in range (0,10):
    tableau_jeu.append(random.randint(1,10))

#recherche séquentielle dans la liste non triée

trouver = False
nombre=int(input("Choisir un nombre: "))
for elt in tableau_jeu:
    if elt == nombre:
        trouver = True
        break
if trouver:
    print("Gagné")
else:
    print("Perdu")
