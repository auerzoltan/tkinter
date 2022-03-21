from tkinter import *
ablak1 = Tk()
gyoker = "H:\\\IKT\\tkinter\\"
ablak1.geometry("450x450")
ablak1.title("IKT Tkinter")
icon = PhotoImage(file="szamologep.png")
ablak1.iconphoto(True, icon)
ablak1.config(background="black")
elsokep= PhotoImage(file=gyoker+"alma.png", width="100", height="100")

def klikk():
    print("Klikkeltem.")

cimke = Label(ablak1, 
            text="Üdvözlet!", 
            fg="#553388",
            bg="yellow",
            font=("Arial", 45, "bold"),
            bd=10,
            relief=RAISED,
            padx=25,
            pady=30,
            image=elsokep,
            compound="center").pack()

gomb= Button(ablak1,
            text="Kattints!",
            fg="blue",
            font=("Comic Sans", 20, "bold"),
            bg="yellow",
            relief=SUNKEN,
            bd=10,
            command=klikk,
            padx=12,
            pady=5,
            image=elsokep,
            compound="bottom",
            activebackground="blue",
            activeforeground="yellow",
            state=ACTIVE).pack()


ablak1.mainloop()