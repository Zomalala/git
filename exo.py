#!/usr/local/bin/python3.9

#-*-coding:UTF-8-*-

#exo1 : convertir la température de celsius à fahrenheit

c = float(input("Donner une température en celsius:"))

f=float((c*9/5)+32)
print("La température en fahrenheit est",f)

#exo2 : Concaténation de dictionnaires

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

dic4 = {}
for d in (dic1,dic2,dic3):
    dic4.update(d)
    print(dic4)

#exo3 : afficher l'heure et la date du jour

import datetime

date = datetime.datetime.now()
print("La date et l'heure actuelles sont:")
print(date.strftime("%Y-%m-%d %H:%M:%S"))

#exo4 : afficher la 1ère et la dernière couleur de la liste

color_list=["Red","Green","White","Black"]
print("La première couleur est:",color_list[0])
print("La dernière couleur est:",color_list[3])

#exo5 : afficher le nom de l'OS et les informations sur la plateforme

import os
import platform

print("Le nom de OS est :",os.name)
print("Les informations sur la plateforme sont :",platform)

#exo6 : afficher la taille d'un fichier 

fichier = str(input("Entrer le chemin complet d'un fichier:"))
taille = os.path.getsize(fichier)
print("La taille de votre fichier est:",taille)

#exo7 : écrire une liste dans un fichier

liste=["Pommes","Poires","Scoubidou","Bananes","Papaye","Mangue"]
fichier = open("liste.txt","w")
fichier.write(liste)
fichier.close()


