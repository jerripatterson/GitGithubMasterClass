from tkinter import *

root = Tk()
root.title("Python Menu for scripts")
root.configure(bd=1, bg="green")
root.geometry("400x400")

# functions

def clicked():
    global my_label2
    input = e.get()
    my_label2 = Label(root, text="Hello " + input)
    my_label2.pack()

def hide():
    my_label2.pack_forget()
    #my_label2.destroy


def show():
    my_label2.pack()


my_label = Label(root, text="Enter your name: ", font=("Helvetica", 20))
my_label.pack()

# Entry widget
e = Entry(root, width=20, font=("Arial", 15))
e.pack(pady=10)

my_button = Button(root, text="Click me!", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="Show", command=show)
show_button.pack(pady=20)

root.mainloop()
