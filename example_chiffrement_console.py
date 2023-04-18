import random

#Déchiffrement de "GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFS" avec le cylindre et la clé fourni

#Chiffrement et déchiffrement d'un une phrase via une cylindre exemple et une clé fixe



class chiffrement:

    def __init__(self, nombre_de_cylindre, phrase, cle):
        self.n = nombre_de_cylindre
        self.phrase = phrase
        self.phrase_chiffré = ""
        self.cle = cle

        #Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
        with open ("example_cylinder.txt", "r") as fichier:
            self.dico = {}
            for i, ligne in enumerate(fichier):
                self.dico[i+1] = ligne

        #Génération d'un d'une clé : permutation des entier entre 1 et n 
        self.cle = [50, 34, 41, 45, 16, 38, 18, 7, 
               26, 25, 10, 30, 2, 9, 4, 20, 36, 
               23, 51, 33, 14, 44, 28, 39, 12, 
               31, 17, 27, 21, 13, 47, 6, 29, 43, 
               46, 42, 3, 8, 24, 1, 37, 49, 35, 11, 
               40, 19, 15, 48, 22, 5, 32]

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




#Exemple : chiffrement et déchiffremnt d'une phrase
phrase = "le grand ours noir danse sur le pont de miami en maillot de bain"
print("Phrase non chiffrée :\n", phrase, "\n")
phrase = phrase.replace(" ", "")
phrase = phrase.upper()
exemple_cle = [50, 34, 41, 45, 16, 38, 18, 7, 
               26, 25, 10, 30, 2, 9, 4, 20, 36, 
               23, 51, 33, 14, 44, 28, 39, 12, 
               31, 17, 27, 21, 13, 47, 6, 29, 43, 
               46, 42, 3, 8, 24, 1, 37, 49, 35, 11, 
               40, 19, 15, 48, 22, 5, 32]
n = len(phrase)
chiffrage = chiffrement(n, phrase, exemple_cle)
chiffrage.chiffrement_phrase()


print("Phrase chifrée : ")
chiffrage.afficher_chiffrement()
phrase_chiffree = chiffrage.return_chiffrement()
dechiffrage = dechiffrement(phrase_chiffree, chiffrage.cle)
dechiffrage._get_dico_()
dechiffrage.dechiffrement_phrase()

print("\n")
print("Phrase déchiffrée : ")
dechiffrage.afficher_dechiffrement()