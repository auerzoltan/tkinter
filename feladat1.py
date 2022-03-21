from tkinter import *

foablak = Tk()
foablak.title("Feladat")

def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, f"{str(c)}")

cimke1=Label(foablak, text="Első mező:")
cimke1.grid(row=1, column=0)
cimke2=Label(foablak, text="Második mező:")
cimke2.grid(row=2, column=0)
cimke3=Label(foablak, text="Harmadik:")
cimke3.grid(row=3, column=0)

mezo1=Entry(foablak)
mezo1.grid(row=1, column=1, columnspan=1)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=1, columnspan=1)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=1, columnspan=1)

can1= Canvas(foablak, width=160, height=160, bg="white")
photo = PhotoImage(file ="villanykorte.png")
item=can1.create_image(80, 80, image= photo)
can1.grid(row=2, column=2, columnspan=3)

foablak.mainloop()