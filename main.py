import random


#Fonction de tirage d'une chaine aléatoire constituée de chacune des 26 lettres de l'alphabet

def tirage():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tirage = ""
    temp = ""
    for i in range(0, 26):
        temp = random.choice(alphabet)
        while temp in tirage:
            temp = random.choice(alphabet)
        tirage += temp
    tirage += "\n"
    return tirage


#Demande à l'utilisateur de rentrer le nombre de ligne qu'il veut dans son fichier
n = int(input("Combien de ligne voulez vous dans votre fichier ?"))
#ajouter la valeure absolue + prendre en compte les erreur de type lettre au lieu de chiffre

#Ecriture dans un fichier txt de n ligne (pas besoin de clear ça le fait tout seul)
with open ("test.txt", "w+") as fichier:
    for i in range (n):
        fichier.write(tirage())

#Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
with open ("test.txt", "r") as fichier:
    dico = {}
    for i, ligne in enumerate(fichier):
        dico[i+1] = ligne

#Affichage du dictionnaire
print(dico)

#Génération d'un d'une clé : permutation des entier entre 1 et n 
for i in range (n):
    cle = random.sample(range(1, n+1), n)

#affichage clé
print(cle)

#chiffrement d'une lettre (lettre située à la position +6 de la chaine de caractère)
#cle = dico[l] l en fonction de la place de la lettre dans la phrase
def chiffrement(lettre, cle):
    cylindre = dico[cle]
    position = cylindre.find(lettre)
    position += 6
    if position > 25:
        position -= 26
    return cylindre[position]

#test de la fonction chiffrement
print(chiffrement("A",cle[0]))

#chiffrement d'une phrase
def chiffrement_phrase(phrase):
    for i in range(len(phrase)):
        phrase[i] = chiffrement(phrase[i], cle[i-1])
        print(phrase)
    return phrase

chiffrement_phrase("BONJOUR")