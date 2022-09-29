from tkinter import *

root = Tk()
root.title("Python Menu for scripts")
root.configure(bd=1, bg="blue")
root.geometry("400x400")

# functions


def clicked():
    global my_label2
    input = e.get()
    my_label2 = Label(root, text="Hello " + input)
    my_label2.grid(row=1, column=1)


def hide():
    # my_label2.pack_forget()
    # my_label2.destroy
    my_frame.grid_forget()


def show():
    # my_label2.pack()
    my_frame.grid(row=10, column=0, columnspan=2, padx=20, pady=20)


def fake_command():
    my_label = Label(root, text="You clicked a menu item.",
                     bg="blue", fg="yellow").grid(row=2, column=1)


my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=fake_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit())

# Create another sub-menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=fake_command)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Paste", command=fake_command)

my_label = Label(root, text="Enter your name: ",
                 font=("Helvetica", 20), bg="blue", fg="Yellow")
my_label.grid(row=1, columnspan=2, padx=10, pady=10)

# Entry widget
e = Entry(root, width=20, font=("Arial", 15))
e.grid(row=2, column=0, columnspan=2)

#my_button = Button(root, text="Click me!", command=clicked)
# my_button.pack(pady=20)

hide_button = Button(root, text="Hide", command=hide)
hide_button.grid(row=3, column=1)

show_button = Button(root, text="Show", command=show)
show_button.grid(row=3, column=2)

my_frame = Frame(root, width=150, height=100, bd=1,
                 bg="darkblue", relief="sunken")
my_frame.grid(row=10, column=0, columnspan=2, padx=20, pady=20)

frame_label = Label(my_frame, text="Hello World", font =("Helvetica", 20),bg="darkblue", fg="yellow")
frame_label.pack(padx=20,pady=20)


root.mainloop()
