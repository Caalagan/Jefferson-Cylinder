import tkinter

root = tkinter.Tk()
root.title("Hello World")
root.geometry("500x700")
label = tkinter.Label(root, text="1\n2\n3\n4\n5\n6")
label.grid(row=0, column=0, sticky="w")

label5 = tkinter.Label(root, text="1")
label5.grid(row=1, column=0, sticky="w")

label2 = tkinter.Label(root, text="2\n3\n4\n5\n6\n7")
label2.grid(row=0, column=1, sticky="w")

label6 = tkinter.Label(root, text="2")
label6.grid(row=1, column=1, sticky="w")

label3 = tkinter.Label(root, text="3\n4\n5\n6\n7\n8")
label3.grid(row=0, column=2, sticky="w")

label7 = tkinter.Label(root, text="3")
label7.grid(row=1, column=2, sticky="w")

label4 = tkinter.Label(root, text="4\n5\n6\n7\n8\n9")
label4.grid(row=0, column=3, sticky="w")

label8 = tkinter.Label(root, text="4")
label8.grid(row=1, column=3, sticky="w")

root.mainloop()