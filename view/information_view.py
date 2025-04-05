from tkinter import *
from controller.information_controller import InformationController
import tkinter.messagebox as msg
from validation.validator import information_validator
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table
from model.information import PatientInformation



class InformationView:
    def save_click(self):
        status, message = self.controller.save(
            self.person.get(),
            self.visit_date_time.get(),
            self.hospital.get(),
            self.prescription.get(),
            self.extra_data.get(),
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)

            self.reset_form()

    def edit_click(self):
        status, message = self.controller.edit(
            self.id.get(),
            self.person.get(),
            self.visit_date_time.get(),
            self.hospital.get(),
            self.prescription.get(),
            self.extra_data.get(),
        )
        if status:
            msg.showinfo("Saved", message)
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
        self.person.set("")
        self.visit_date_time.set("")
        self.hospital.set("")
        self.prescription.set("")
        self.extra_data.set("")
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())

    def select_table(self, selected_row):
        print(selected_row)  # بررسی محتوا برای دیباگ
        try:
            information = PatientInformation(*selected_row[:6])  # پاس دادن 6 آیتم اول
        except TypeError as e:
            print(f"Error: {e}")  # مدیریت خطا در صورت اختلاف آرگومان‌ها

        self.id.set(information.id)
        self.person.set(information.person)
        self.hospital.set(information.hospital)
        self.visit_date_time.set(information.visit_date_time)
        self.prescription.set(information.prescription)
        self.extra_data.set(information.extra_data)

    def __init__(self):
        self.controller = InformationController()

        self.win = Tk()
        self.win.geometry("830x330")
        self.win.title("Information_view")

        self.id = LabelAndEntry(self.win, "Id", 20, 20, IntVar, 90, state="readonly")
        self.person = LabelAndEntry(self.win, "Person", 20, 60, StringVar, 90)
        self.hospital = LabelAndEntry(self.win, "Visit_Date_Time", 20, 100, StringVar, 90)
        self.visit_date_time = LabelAndEntry(self.win, "Hospital", 20, 140, StringVar, 90)
        self.prescription = LabelAndEntry(self.win, "Prescription", 20, 180, StringVar, 90)
        self.extra_data = LabelAndEntry(self.win, "Extra_Data", 20, 220, StringVar, 90)

        Button(self.win, text="search", width=7, command=self.save_click).place(x=20, y=280)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=85, y=280)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=150, y=280)

        self.table = Table(
            self.win,
            6,
            ["Id", "Person", "Visit_Date_Time", "Hospital", "Prescription","Extra_Data"],
            [60, 100, 100, 100, 100, 100],
            260, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()







