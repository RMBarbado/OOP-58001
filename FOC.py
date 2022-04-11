from tkinter import *
window = Tk()

window.geometry("400x130+10+20")
window.title("Father of Computer")

label = Label(window, text = "Charles Babbage", font = ("Verdana", 20), fg = "black", bg = "cyan")
label.place(x = 85, y = 45)
window.mainloop()
