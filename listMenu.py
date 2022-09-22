from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("400x400")

# functions


def clicked():
    input = e.get()
    my_label2 = Label(root, text="Hello " + input)
    my_label2.pack()


my_label = Label(root, text="Enter your name: ", font=("Helvetica", 20))
my_label.pack()

my_button = Button(root, text="Click me!", command=clicked)
my_button.pack(pady=20)

# Entry widget
e = Entry(root, width=20, font=("Arial", 15))
e.pack(pady=10)


root.mainloop()
