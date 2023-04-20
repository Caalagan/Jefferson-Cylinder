from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("500x700")

def bouton():
    liste.append(label5.cget("text"))
    suite.config(text=liste)

#Creation d`un label a chaque colonne et d`un bouton pour chaque cylindrekkwsdfghbabygirljjjjjjjjjjjj


label = Label(root, text="   1\n   2\n   3\n   4\n   5\n   6")
label.grid(row=0, column=0, sticky="w")

label5 = Button(root, text="1", relief = FLAT, command=bouton)
label5.grid(row=1, column=0, sticky="w")

label2 = Label(root, text="   2\n   3\n   4\n   5\n   6\n   7")
label2.grid(row=0, column=1, sticky="w")

label6 = Button(root, text="2", relief = FLAT, command=bouton)
label6.grid(row=1, column=1, sticky="w")

label3 = Label(root, text="   3\n   4\n   5\n   6\n   7\n   8")
label3.grid(row=0, column=2, sticky="w")

label7 = Button(root, text="3", relief = FLAT, command=bouton)
label7.grid(row=1, column=2, sticky="w")

label4 = Label(root, text="   4\n   5\n   6\n   7\n   8\n   9")
label4.grid(row=0, column=3, sticky="w")

label8 = Button(root, text="4", relief = FLAT, command=bouton)
label8.grid(row=1, column=3, sticky="w")



liste=[]
suite = Label(root, text=liste)
#La suite doit s'afficher en dessous de toutes les colonnes
suite.grid(row=2, column=0, sticky="nsew")


root.mainloop()


Demande = Label(self.root, text="Voulez vous chiffrer la phrase (oui/non) : ")
            Demande.grid(row=3, column=0, sticky="nsew")
            BouttonOui = Button(self.root, text="Oui", relief = FLAT, command=lambda: self.chiffrement_phrase())
            BouttonOui.grid(row=4, column=0, sticky="nsew")
            BouttonNon = Button(self.root, text="Non", relief = FLAT, command=lambda: self.root.destroy())
            BouttonNon.grid(row=4, column=1, sticky="nsew")