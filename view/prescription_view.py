from tkinter import *
import tkinter.messagebox as msg
from controller.prescription_controller import PrescriptionController
from model.prescription import Prescription
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table


class PrescriptionView:
    def save_click(self):
        status, message = self.controller.save(
            self.date_time.get(),
            self.doctor.get(),
            self.drug.get(),
            self.dosage.get(),
            self.description.get(),
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)

            self.reset_form()

    def edit_click(self):
        status, message = self.controller.edit(
            self.date_time.get(),
            self.doctor.get(),
            self.drug.get(),
            self.dosage.get(),
            self.description.get(),
        )
        if status:
            msg.showinfo("Edited", message)
        else:
            msg.showerror("Error", message)

            self.reset_form()

    def remove_click(self):
        status, message = self.controller.remove(self.id.get())

        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def reset_form(self):
        self.id.set(0)
        self.date_time.set("")
        self.doctor.set("")
        self.drug.set("")
        self.dosage.set("")
        self.description.set("")
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())


    def select_table(self, selected_row):
        global prescription
        if selected_row and len(selected_row) > 5:
            prescription = Prescription(*selected_row)
        self.id.set(prescription.id)
        self.date_time.set(prescription.date_time)
        self.doctor.set(prescription.doctor)
        self.drug.set(prescription.drug)
        self.dosage.set(prescription.dosage)
        self.description.set(prescription.description)

    def __init__(self):
        self.controller = PrescriptionController()

        self.win = Tk()
        self.win.geometry("710x330")
        self.win.title("Prescription View")

        self.id = LabelAndEntry(self.win, "Id", 20, 20, IntVar, 65, state="readonly")
        self.date_time = LabelAndEntry(self.win, "date_time", 20, 60, StringVar, 65)
        self.doctor = LabelAndEntry(self.win, "doctor", 20, 100, StringVar, 65)
        self.drug = LabelAndEntry(self.win, "drug", 20, 140, StringVar, 65)
        self.dosage = LabelAndEntry(self.win, "dosage", 20, 180, StringVar, 65)
        self.description = LabelAndEntry(self.win, "description", 20, 220, StringVar, 65)

        Button(self.win, text="Add Patient", width=8, command=self.save_click).place(x=30, y=280)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=98, y=280)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=280)

        self.table = Table(
            self.win,
            5,
            ["Id", "date_time", "doctor", "drug", "dosage", "description"],
            [60, 100, 100, 100, 100],
            230, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()