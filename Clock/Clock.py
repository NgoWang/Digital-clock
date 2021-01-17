from time import strftime
from tkinter import Label, Tk

#======= Configuring window =========
window = Tk()
window.title("Current Time")
window.geometry("420x150")
window.configure(bg="white")

clock_label = Label(window, bg="white", fg="black", font = ("Times", 30), relief='flat')
clock_label.place(x = 20, y = 20)

def update_label():
    Ohio_time = strftime('%a %H: %M: %S %p')
    clock_label.configure(text = Ohio_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()