import random
from tkinter import *
class chiffrement:
    def __init__(self, nombre_de_cylindre, phrase):
        self.n = nombre_de_cylindre
        self.phrase = phrase
        self.phrase_chiffré = ""
        self.cle = []

        #Ecriture dans un fichier txt de n ligne (pas besoin de clear ça le fait tout seul)
        with open ("cylindre.txt", "w+") as fichier:
            for i in range (n):
                fichier.write(self.tirage())

        self._get_dico_()


        #Création de la fenetre
        self.root = Tk()
        self.root.title("Jefferson's Cylinder")
        self.root.geometry("500x700")
        self.affichage_cylindre()
        self.creer_boutton_cle()

 


    def affichage_cylindre(self):
        #Creation d`un label a chaque colonne
        for i in range (n):
            ligne=""
            VarCylindre = "label"+str(i)
            VarTexte = self.dico[i+1]
            for caractere in VarTexte:
                ligne += ("   " + caractere + "\n")
            VarCylindre = Label(self.root, text=ligne)
            VarCylindre.grid(row=0, column=i, sticky="w")


    #ajouter un boutton pour chaque cylindre
    def creer_boutton_cle(self):
        for i in range (n):
            VarBoutton = Button(self.root, text=i+1, relief = FLAT, command=lambda i=i: self.boutton(i))
            VarBoutton.grid(row=1, column=i, sticky="w")
            self.AffichageCle = Label(self.root, text=self.cle)
            self.AffichageCle.grid(row=2, column=0, columnspan=100)
  

        #ajouter deux fleches pour chaque cylindre 
    def creer_fleches(self):
        for i in range (n):
            VarFlecheHaut = Button(self.root, text="^\n|", relief = FLAT, command=lambda i=i: self.fleche_haut(i))
            VarFlecheHaut.grid(row=1, column=i, sticky="w")

        for i in range (n):
            VarFlecheBas = Button(self.root, text="|\nv", relief = FLAT, command=lambda i=i: self.fleche_bas(i))
            VarFlecheBas.grid(row=2, column=i, sticky="w")

    #Fonction pour rotate le cylindre vers le haut
    def fleche_haut(self, num):

        temp=self.dico[num+1]
        lettre=""
        for i in range (25):
            lettre+=temp[i+1]
        lettre+=temp[0]
        lettre+="\n"
        self.dico[num+1]=lettre
        self.reload_affichage()
        self.creer_fleches()

    #Fonction pour rotate le cylindre vers le bas
    def fleche_bas(self, num):

        temp=self.dico[num+1]
        lettre=temp[25]
        for i in range (25):
            lettre+=temp[i]
        lettre+="\n"
        self.dico[num+1]=lettre
        self.reload_affichage()
        self.creer_fleches()

    #Fonction pour ajouter ou supprimer un numéro de cylindre de la clé
    def boutton(self, num):
        PeutAjouter = True
        for i in range(len(self.cle)):
            if self.cle[i] == num+1:
                self.cle.pop(i)
                PeutAjouter = False
                break
        if PeutAjouter == True:
            self.cle.append(num+1)
        self.AffichageCle.config(text=self.cle)

        #Si la clé est complète on reload l'affichage et on ajoute les fleches
        if len(self.cle) == n:
            self.reload_affichage()
            self.creer_fleches()

   
    def reload_affichage(self):
        for elements in self.root.winfo_children():
            elements.destroy()
        #Affichage des cylindres dans l'ordre de la cle
        self.modification_cylindre()
        self.affichage_cylindre()
        # Affichage de CLEAR et CIPHER
        self.clear_label = Label(self.root, text="CLEAR")
        self.clear_label.grid(row=0,  column=n+1,padx = 1, pady=5)
        self.cipher_label = Label(self.root, text="CIPHER ")
        self.cipher_label.grid(row=0, column=n+1, sticky="s",  padx= 1, pady=5)
    

        # Affichage du résultat chiffré
        self.cipher_result_label = Label(self.root, text="Texte chiffré: " + self.phrase_chiffré)
        self.cipher_result_label.grid(row=2, column=self.n+1, sticky="w")

        # Affichage du résultat déchiffré
        self.clear_result_label = Label(self.root, text="Texte clair: " + self.phrase)
        self.clear_result_label.grid(row=3, column=self.n+1, sticky="w")

        # Affichage du bouton pour quitter
        self.quit_button = Button(self.root, text="Quitter", command=self.root.destroy)
        self.quit_button.grid(row=4, column=self.n+1, sticky="w")

        # Affichage la clé et le nombre de ligne a sauter pour avoir la phrase en clair
        self.key_result_label = Label(self.root, text="Clé: " + str(self.cle))
        self.key_result_label.grid(row=5, column=self.n+1, sticky="w")
    

        # Affichage du nombre de ligne a sauter
        self.lines_result_label = Label(self.root, text="Lignes à sauter: " + str(self.phrase_chiffré.count("\n")))
        self.lines_result_label.grid(row=6, column=self.n+1, sticky="w")





    
    def modification_cylindre(self):
        #on modifie le fichier cylindre.txt pour qu'il corresponde à la clé
        with open ("cylindre.txt", "w+") as fichier:
            for i in range (n):
                fichier.write(self.dico[self.cle[i]])
        #recupération du nouveau dico
        self._get_dico_()

    def _get_dico_(self):
        #Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
        with open ("cylindre.txt", "r") as fichier:
            self.dico = {}
            for i, ligne in enumerate(fichier):
                self.dico[i+1] = ligne

    #Génération d'un tirage aléatoire de 26 lettres
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
    
phrase = input("Votre phrase : ")
phrase = phrase.replace(" ", "")
phrase = phrase.upper()
n = len(phrase)
chiffrage = chiffrement(n, phrase)
#print(chiffrage.dico)
#print(chiffrage.cle)
chiffrage.root.mainloop()
#chiffrage.chiffrement_phrase()
#chiffrage.afficher_chiffrement()
#phrase_chiffree = chiffrage.return_chiffrement()
#dechiffrage = dechiffrement(phrase_chiffree, chiffrage.cle)
#dechiffrage._get_dico_()
#dechiffrage.dechiffrement_phrase()
#dechiffrage.afficher_dechiffrement()
#phrase_dechiffree = dechiffrage.return_dechiffrement()

