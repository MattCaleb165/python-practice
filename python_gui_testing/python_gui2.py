import tkinter as tk

def clear_entry(event):
    entry.delete(0, tk.END)

def print_entry(event):
    name = entry.get()
    print("Hello, " + name)
    clear_entry(event)

def button_clicked(event):
    print_entry(event)

window = tk.Tk()
window.geometry("300x200")

label = tk.Label(text="Name")
entry = tk.Entry()
submit_button = tk.Button(text="Submit", command=lambda opt="Submit": button_clicked(opt))

label.pack()
entry.pack()
submit_button.pack()

name = entry.get()
entry.bind("<Return>", print_entry)
entry.bind

window.mainloop()