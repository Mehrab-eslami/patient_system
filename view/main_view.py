from tkinter import *

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

        Button(win, text="Persons", width=10, command=self.person_view).place(x=20, y=20)
        Button(win, text="Informations", width=10, command=self.information_view).place(x=20, y=80)

        win.mainloop()
