#!/usr/local/bin/python3.9

#roulette de casino : le joueur mise une somme sur un numéro compris entre 0 et 49

cagnotte = int(1000)
print("Vous vous installez à la table de roulette avec ", cagnotte , "$")

from random import randrange
from math import ceil

#boucle while pour miser un numéro

reponse = str("o")
while reponse == "o":

    numero = int(input("Choisir un nombre entre 0 et 49: "))
    mise = float(input("Choisir le montant de votre mise: "))

    if mise > cagnotte:
        print("Vous ne pouvez pas miser autant, vous n'avez que ",cagnotte , "$!")
    elif cagnotte == 0:
        print("Vous ne pouvez malheureusement plus jouer!")

    else:
        tirage = randrange(50)
        print("La roulette tourne... elle s'arrête sur le numero ", tirage)

#1er cas : le numéro misé correspond au tirage


    if numero == tirage:
        gain = ceil(mise * 3)
        print("Félicitations! Vous avez gagné ", gain, "$!")
        cagnotte = (ceil(cagnotte+gain))
        print("Votre cagnotte est maintenant de: ", cagnotte , "$!")
        reponse = str(input("Voulez-vous continuer? o/n : "))

#2ème cas : le numéro misé est de la même couleur que le tirage

    elif numero%2 == tirage%2:
        gain = ceil(mise * 1.5)
        print("Félicitations! Vous avez gagné ", gain, "$!")
        cagnotte = (ceil(cagnotte+gain))
        print("Votre cagnotte est maintenant de: ", cagnotte ,"$!")
        reponse = str(input("Voulez-vous continuer? o/n : "))

#3ème cas : le joueur perd sa mise

    else:
        print("Désolé, pas pour cette fois. Vous perdez votre mise.")
        cagnotte = (ceil(cagnotte-mise))
        print("Votre cagnotte est maintenant de: ", cagnotte , "$!")
        reponse = str(input("Voulez-vous continuer? o/n : "))

