import tkinter
from tkinter import *
from PIL import ImageTk, Image

from view.person_view import PersonView
from view.information_view import InformationView


class MainView:
    def person_view(self):
        ui = PersonView()

    def information_view(self):
        ui = InformationView()

    def __init__(self):
        win = Tk()
        win.title("Main view")
        win.geometry("250x250")
        img = Image.open("C:/Users/MSI/Desktop/patient_system/view/main back.jpeg")
        img = img.resize((300, 250))
        img = ImageTk.PhotoImage(img)
        Label_pic = Label(image=img)
        Label_pic.place(x=2, y=2)

        Button(win, text="Persons", width=15, height=2, command=self.person_view).place(x=50, y=30)
        Button(win, text="Informations", width=15, height=2, command=self.information_view).place(x=50, y=90)
        Button(win, text="Prescriptions", width=15, height=2, command=self.information_view).place(x=50, y=150)

        win.mainloop()
