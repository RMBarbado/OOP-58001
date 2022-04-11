from tkinter import *
from tkinter import ttk
window = Tk()

def Displayname():
    txtfld['text'] = 'Fullname'

window.geometry("500x250+10+20")
window.title("Midterm in OOP")

label = Label(window, text = "Enter your fullname:", fg = "red")
label.place(x=20, y=60)

button = Button(window, text = "Click to display your Fullname", fg = "red", command = Displayname)
button.place (x=20, y=100)

txtfld = Entry(window, textvariable = 'Fullname', bd = 5)
txtfld.place(x=250, y=60)

txtfld = Entry(window, text = 'name', bd = 5)
txtfld.place(x=250, y=100)

window.mainloop()