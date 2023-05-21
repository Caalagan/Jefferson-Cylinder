import random
from tkinter import *

class Menu:
    def __init__(self) -> None:
        #Création de la fenetre de menu
        self.root = Tk()
        self.root.geometry("400x400")
        BouttonChiffrement = Button(self.root, text="Chiffrement", command=self.chiffrement)
        BouttonChiffrement.pack()
        BouttonDechiffrement = Button(self.root, text="Déchiffrement", command=self.dechiffrement)
        BouttonDechiffrement.pack()

    def chiffrement(self):
        for elements in self.root.winfo_children():
            elements.destroy()
        Text = Label(self.root, text="Le nombre de cylindre doit être supérieur à 0 !")
        Text.pack()
        self.__number = IntVar()
        NbCylinders = Entry(self.root, textvariable=self.__number)
        NbCylinders.focus_set()
        NbCylinders.pack()
        button = Button(self.root, text="Afficher le Cylindre", command=self.LancerLeChiffrement)
        button.pack()
        

    def LancerLeChiffrement(self):
        if self.__number.get()>0:
            self.root.destroy()
            phrase = chiffrement(self.__number.get())
            phrase.root.mainloop()

    def dechiffrement(self):
        self.root.destroy()
        phrase = dechiffrement()
        phrase.root.mainloop()

class chiffrement:
    def __init__(self, nombre_de_cylindre):
        self.nbCylindre = nombre_de_cylindre
        self.phraseClair = ""
        self.phraseChiffre = "" 
        self.cle = []
        #Ecriture dans un fichier txt de n ligne (pas besoin de clear ça le fait tout seul)
        with open ("cylindre.txt", "w+") as fichier:
            for i in range (self.nbCylindre):
                fichier.write(self.tirage())

        self._get_dico_()


        #Création de la fenetre
        self.root = Tk()
        self.root.title("Jefferson's Cylinder")
        self.root.geometry("400x800")
        self.affichage_cylindre()
        self.creer_boutton_cle()

 


    def affichage_cylindre(self):
        #Creation d`un label pour afficher chaque cylindre sur une colonne
        for i in range(self.nbCylindre):
            ligne=""
            VarCylindre = "label"+str(i)
            VarTexte = self.dico[i+1]
            for caractere in VarTexte:
                ligne += ("   " + caractere + "\n")
            VarCylindre = Label(self.root, text=ligne)
            VarCylindre.grid(row=0, column=i, sticky="w")

    #ajouter un boutton pour chaque cylindre
    def creer_boutton_cle(self):
        for i in range (self.nbCylindre):
            VarBoutton = Button(self.root, text=i+1, relief = FLAT, command=lambda i=i: self.boutton(i))
            VarBoutton.grid(row=1, column=i, sticky="w")
            self.AffichageCle = Label(self.root, text=self.cle)
            self.AffichageCle.grid(row=2, column=0, columnspan=100)
  

    #ajouter deux fleches pour chaque cylindre 
    def creer_fleches(self):
        for i in range (self.nbCylindre):
            VarFlecheHaut = Button(self.root, text="\u25b2\n", relief = FLAT, command=lambda i=i: self.fleche_haut(i))
            VarFlecheHaut.grid(row=1, column=i, sticky="w")
            
        for i in range (self.nbCylindre):
            VarFlecheBas = Button(self.root, text="\n\u25bc", relief = FLAT, command=lambda i=i: self.fleche_bas(i))
            VarFlecheBas.grid(row=2, column=i, sticky="w")


    #Fonction pour rotate le cylindre vers le haut3
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
        if len(self.cle) == self.nbCylindre:
            self._get_dico_()
            self.reload_affichage()
            self.creer_fleches()

    def phrase_clair(self):
        self.phraseClair=""
        for y in range(len(self.dico)):
            self.phraseClair+=self.dico[y+1][0]

    def phrase_chiffre(self):
        self.phraseChiffre=""
        for y in range(len(self.dico)):
            self.phraseChiffre+=self.dico[y+1][14]

    def reload_affichage(self):
        for elements in self.root.winfo_children():
            elements.destroy()

        #Affichage des cylindres dans l'ordre de la cle
                                                                                                    #self.modification_cylindre()
        self.affichage_cylindre()
        self.phrase_clair()
        self.phrase_chiffre()
        

        # Affichage de CLEAR et CIPHER

        self.clear_label = Label(self.root, text="\u2190  CLEAR")
        self.clear_label.grid(row=0,column=self.nbCylindre+1,sticky="nwe")
        self.cipher_label = Label(self.root, text="\u2190 CHIFFRE")
        self.cipher_label.grid(row=0,column=self.nbCylindre+1,sticky="we")
    
        

        # Affichage de la phrase en clair
        self.clear_result_label = Label(self.root, text="Texte clair: " + self.phraseClair)
        self.clear_result_label.grid(row=2, column=self.nbCylindre+1, sticky="w")

        # Affichage du résultat chiffré
        self.cipher_result_label = Label(self.root, text="Texte chiffré: " + self.phraseChiffre)
        self.cipher_result_label.grid(row=3, column=self.nbCylindre+1, sticky="w")

        # Affichage la clé
        self.key_result_label = Label(self.root, text="Clé: " + str(self.cle))
        self.key_result_label.grid(row=4, column=self.nbCylindre+1, sticky="w")
    
        
        # Affichage du nombre de ligne a sauter pour avoir la phrase en clair
        self.skip_result_label = Label(self.root, text="Nombre de lignes à sauter: 15")
        self.skip_result_label.grid(row=5, column=self.nbCylindre+1, sticky="w")

        style_Quitter = {
            'bg': '#f44336',     # Background color
            'fg': 'white',       # Text color
            'font': ('Arial', 12, 'bold'),  # Font style
            'relief': 'raised',  # Button border style
            'borderwidth': 2,    # Border width
            'width': 10,         # Button width
            'height': 1,         # Button height
                        }
         # Affichage du bouton pour Menu
        self.boutonMenu = Button(self.root, text="Menu", command=self.LancerMenu, **style_Quitter)
        self.boutonMenu.grid(row=6, column=self.nbCylindre+1, sticky="w")

    def LancerMenu(self):
        self.root.destroy()
        BackMenu = Menu()
        BackMenu.root.mainloop()

    
    def modification_cylindre(self):
        #on modifie le fichier cylindre.txt pour qu'il corresponde à la rotation en cours
        with open ("cylindre.txt", "w+") as fichier:
            for i in self.cle:
                fichier.write(self.dico[i])

    def _get_dico_(self):
        #Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
        if 1 in self.cle :
            with open ("cylindre.txt", "r") as fichier:
                self.dico = {}
                for i, ligne in enumerate(fichier):
                    self.dico[self.cle[i]] = ligne
        else : 
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
    
    
#Déchiffrement
class dechiffrement:
    def __init__(self):
        
        self.phraseClair = ""
        self.phraseChiffre = "" 
        self.cle = []

        self._get_dico_()
        print(len(self.dico))
        self.nbCylindre = len(self.dico)


        #Création de la fenetre
        self.root = Tk()
        self.root.title("Jefferson's Cylinder")
        self.root.geometry("400x800")
        self.affichage_cylindre()
        self.creer_boutton_cle()


    def affichage_cylindre(self):
        #Creation d`un label pour afficher chaque cylindre sur une colonne
        for i in range(self.nbCylindre):
            ligne=""
            VarCylindre = "label"+str(i)
            VarTexte = self.dico[i+1]
            for caractere in VarTexte:
                ligne += ("   " + caractere + "\n")
            VarCylindre = Label(self.root, text=ligne)
            VarCylindre.grid(row=0, column=i, sticky="w")

    #ajouter un boutton pour chaque cylindre
    def creer_boutton_cle(self):
        for i in range (self.nbCylindre):
            VarBoutton = Button(self.root, text=i+1, relief = FLAT, command=lambda i=i: self.boutton(i))
            VarBoutton.grid(row=1, column=i, sticky="w")
            self.AffichageCle = Label(self.root, text=self.cle)
            self.AffichageCle.grid(row=2, column=0, columnspan=100)
  

    #ajouter deux fleches pour chaque cylindre 
    def creer_fleches(self):
        for i in range (self.nbCylindre):
            VarFlecheHaut = Button(self.root, text="\u25b2\n", relief = FLAT, command=lambda i=i: self.fleche_haut(i))
            VarFlecheHaut.grid(row=1, column=i, sticky="w")
            
        for i in range (self.nbCylindre):
            VarFlecheBas = Button(self.root, text="\n\u25bc", relief = FLAT, command=lambda i=i: self.fleche_bas(i))
            VarFlecheBas.grid(row=2, column=i, sticky="w")


    #Fonction pour rotate le cylindre vers le haut3
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
        if len(self.cle) == self.nbCylindre:
            self._get_dico_()
            self.reload_affichage()
            self.creer_fleches()

    def phrase_clair(self):
        self.phraseClair=""
        for y in range(len(self.dico)):
            self.phraseClair+=self.dico[y+1][0]

    def phrase_chiffre(self):
        self.phraseChiffre=""
        for y in range(len(self.dico)):
            self.phraseChiffre+=self.dico[y+1][14]

    def reload_affichage(self):
        for elements in self.root.winfo_children():
            elements.destroy()

        #Affichage des cylindres dans l'ordre de la cle
        self.modification_cylindre()
        self.affichage_cylindre()
        self.phrase_clair()
        self.phrase_chiffre()
        

        # Affichage de CLEAR et CIPHER

        self.clear_label = Label(self.root, text="\u2190  CLEAR")
        self.clear_label.grid(row=0,column=self.nbCylindre+1,sticky="nwe")
        self.cipher_label = Label(self.root, text="\u2190 CHIFFRE")
        self.cipher_label.grid(row=0,column=self.nbCylindre+1,sticky="we")
    
        

        # Affichage de la phrase en clair
        self.clear_result_label = Label(self.root, text="Texte clair: " + self.phraseClair)
        self.clear_result_label.grid(row=2, column=self.nbCylindre+1, sticky="w")

        # Affichage du résultat chiffré
        self.cipher_result_label = Label(self.root, text="Texte chiffré: " + self.phraseChiffre)
        self.cipher_result_label.grid(row=3, column=self.nbCylindre+1, sticky="w")

        # Affichage la clé
        self.key_result_label = Label(self.root, text="Clé: " + str(self.cle))
        self.key_result_label.grid(row=4, column=self.nbCylindre+1, sticky="w")
    
        
        # Affichage du nombre de ligne a sauter pour avoir la phrase en clair
        self.skip_result_label = Label(self.root, text="Nombre de lignes à remonter : 15")
        self.skip_result_label.grid(row=5, column=self.nbCylindre+1, sticky="w")

        style_Quitter = {
            'bg': '#f44336',     # Background color
            'fg': 'white',       # Text color
            'font': ('Arial', 12, 'bold'),  # Font style
            'relief': 'raised',  # Button border style
            'borderwidth': 2,    # Border width
            'width': 10,         # Button width
            'height': 1,         # Button height
                        }
        # Affichage du bouton pour Menu
        self.boutonMenu = Button(self.root, text="Menu", command=self.LancerMenu, **style_Quitter)
        self.boutonMenu.grid(row=6, column=self.nbCylindre+1, sticky="w")

    def LancerMenu(self):
        self.root.destroy()
        BackMenu = Menu()
        BackMenu.root.mainloop()

      

    
    def modification_cylindre(self):
        #on modifie le fichier cylindre.txt pour qu'il corresponde à la rotation en cours
        with open ("cylindre.txt", "w+") as fichier:
            for i in self.cle:
                fichier.write(self.dico[i])

    def _get_dico_(self):
        #Lecture du fichier : création d'un dictionnaire avec en clé le numéro de la ligne et en valeur la chaine de caractère
        if 1 in self.cle :
            with open ("cylindre.txt", "r") as fichier:
                self.dico = {}
                for i, ligne in enumerate(fichier):
                    self.dico[self.cle[i]] = ligne
        else : 
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
    


menu = Menu()
menu.root.mainloop()


