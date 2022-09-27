import tkinter
from tkinter import Button, Label, Tk
root = Tk()
root.title('My Config')
root.geometry("400x400")

def show():
    my_label.config(text='This is new text!!')

global my_label

my_label = Label(root, text='My Config file', font=("Helvetica",15))
my_label.pack(pady=10)

my_button =Button(root,text='Click me', command=show)
my_button.pack(pady=10)






root.mainloop()