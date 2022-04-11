from tkinter import *
window = Tk()

window.geometry("550x400+10+20")
window.title("Midterms in OOP")

lbl = Label(window, text = "Enter your fullname:", fg = "red", font = ("Arial", 10))
lbl.place(x = 20, y = 60)

input_fn = Entry(window, text = "Fullname", bd = 5, width = 35)
input_fn.place(x = 250, y = 60)

btn = Button(window, text = "Click to display your Fullname", fg = "red")
btn.place(x = 20, y = 100)

disp_fn = Entry(window, text = "Fullname", bd = 5, width = 35)
disp_fn.place(x = 250, y = 100)

window.mainloop()