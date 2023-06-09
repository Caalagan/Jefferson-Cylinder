import random

class chiffrement:

    def __init__(self, nombre_de_cylindre, phrase):
        self.n = nombre_de_cylindre
        self.phrase = phrase
        self.phrase_chiffré = ""

        #Génération des cylindres
        #Ecriture dans un fichier txt de n ligne (pas besoin de clear ça le fait tout seul)
        with open ("cylindre.txt", "w+") as fichier:
            for i in range (n):
                fichier.write(self.tirage())

        #Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
        with open ("cylindre.txt", "r") as fichier:
            self.dico = {}
            for i, ligne in enumerate(fichier):
                self.dico[i+1] = ligne

        #Génération d'un d'une clé : permutation des entier entre 1 et n 
        for i in range (n):
            self.cle = random.sample(range(1, n+1), n)

    def tirage(self):
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

    #chiffrement d'une lettre (lettre située à la position +6 de la chaine de caractère)
    def chiffrement_lettre(self, lettre, cle):
        cylindre = self.dico[cle]
        position = cylindre.find(lettre)
        position += 6
        if position > 25:
            position -= 26
        return cylindre[position]

    #chiffrement d'une phrase
    def chiffrement_phrase(self):
        for i in range(len(self.phrase)):
            self.phrase_chiffré += self.chiffrement_lettre(self.phrase[i], self.cle[i])

    def afficher_chiffrement(self):
        print(self.phrase_chiffré)

    def return_chiffrement(self):
        return self.phrase_chiffré

phrase = input("Votre phrase : ")
phrase = phrase.replace(" ", "")
phrase = phrase.upper()
n = len(phrase)
chiffrage = chiffrement(n, phrase)
print(chiffrage.dico)
print(chiffrage.cle)
chiffrage.chiffrement_phrase()
chiffrage.afficher_chiffrement()
phrase_chiffree = chiffrage.return_chiffrement()

#Déchiffrement
class dechiffrement:
    def __init__(self, phrase_chiffré, cle):
        self.phrase_chiffré = phrase_chiffré
        self.cle = cle
        self.phrase_dechiffree = ""

    def _get_dico_(self):
        #Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
        with open ("cylindre.txt", "r") as fichier:
            self.dico = {}
            for i, ligne in enumerate(fichier):
                self.dico[i+1] = ligne


    def dechiffrement_lettre(self, lettre, cle):
        cylindre = self.dico[cle]
        position = cylindre.find(lettre)
        position -= 6
        if position < 0:
            position += 26
        return cylindre[position]

    def dechiffrement_phrase(self):
        for i in range(len(self.phrase_chiffré)):
            self.phrase_dechiffree += self.dechiffrement_lettre(self.phrase_chiffré[i], self.cle[i])

    def afficher_dechiffrement(self):
        print(self.phrase_dechiffree)

    def return_dechiffrement(self):
        return self.phrase_dechiffree
    

dechiffrage = dechiffrement(phrase_chiffree, chiffrage.cle)
dechiffrage._get_dico_()
dechiffrage.dechiffrement_phrase()
dechiffrage.afficher_dechiffrement()
phrase_dechiffree = dechiffrage.return_dechiffrement()
print(phrase_dechiffree)