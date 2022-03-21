from tkinter import *
import math

def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, f"Összeg: {str(c)}")

def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b
    mezo3.delete(0, END)
    mezo3.insert(0, f"Az eredmény: {str(c)}")

def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b
    mezo3.delete(0, END)
    mezo3.insert(0, f"A szorzat értéke: {str(c)}")

def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a / b
    mezo3.delete(0, END)
    mezo3.insert(0, f"Az eredmény: {str(c)}")

def hatvanyozas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a ** b
    mezo3.delete(0, END)
    mezo3.insert(0, f"Eredmény : {str(c)}")
    

def gyokvonas():
    a = int(mezo1.get())
    c = math.sqrt(a)
    mezo3.delete(0, END)
    mezo3.insert(0, f"Eredmény : {str(c)}")
    if a>=0:
        mezo3.insert(0, "Negatív számból nem tudok nágyzetgyököt vonni")

foablak = Tk()
foablak.title("Számológép")
icon = PhotoImage(file="szamologep.png")
foablak.iconphoto(True, icon)
cimke=Label(foablak, text="Üdvözlet! Ez a lap itt számológépként funkcionál", fg="red")
cimke.grid(row=0, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=0)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=3)
mezo3=Entry(foablak)
mezo3.grid(row=2, column=1)
gomb4=Button(foablak, text="Összead", command=osszeg)
gomb4.grid(row=4, column=1)
gomb5=Button(foablak, text="Kivonás", command=kivonas)
gomb5.grid(row=5, column=1)
gomb6=Button(foablak, text="Szorzás", command=szorzas)
gomb6.grid(row=6, column=1)
gomb7=Button(foablak, text="Osztás", command=osztas)
gomb7.grid(row=7, column=1)
gomb8=Button(foablak, text="Hatványozás", command=hatvanyozas)
gomb8.grid(row=8, column=1)
gomb9=Button(foablak, text="Gyökvonás", command=gyokvonas)
gomb9.grid(row=9, column=1)
gomb3=Button(foablak, text="Kilépés", command=foablak.destroy)
gomb3.grid(row=10, column=3)

can1= Canvas(foablak, width=300, height=300, bg="white")
photo = PhotoImage(file ="8008135+calculator.gif")
item=can1.create_image(80, 80, image= photo)
can1.grid(row=11, column=1)
foablak.mainloop()



