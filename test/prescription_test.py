from tkinter import *
from PIL import ImageTk, Image
root = Tk()
#img = PhotoImage(master=root , file="C:/Users/MSI/Desktop/patient_system/view/back.jpg")
img = Image.open("C:/Users/MSI/Desktop/patient_system/view/main back.jpeg")
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)


Label_pic = Label(root, image=img)
Label_pic.place(x=2,y=1)



mainloop()
