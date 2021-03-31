#!/usr/local/bin/python3.9

#initialisation de la site et affichage

liste_animaux = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
print (liste_animaux)

#afficher la liste de manière inversée

liste_animaux.reverse()
print (liste_animaux)

#afficher la liste de manière triée

liste_animaux.sort()
print (liste_animaux)

#ajouter l'élément troll et supprimer les animaux domestiques en créant une liste animaux domestiques

liste_animaux.append("troll")
liste_animaux_domestiques = ["lapin","chat","chien","chiot"]
for i in liste_animaux_domestiques:
    liste_animaux.remove(i)
    print (liste_animaux)

