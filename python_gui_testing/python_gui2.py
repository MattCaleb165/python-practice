import tkinter as tk

error_label = None  # Global variable for the error label

def print_entry():
    global error_label  # Access the global error_label variable
    name = entry.get().strip()  # Get the entered name and remove leading/trailing spaces
    if not name:  # Check if name is empty
        if error_label is None:
            error_label = tk.Label(text="Please enter a name", fg="red")
            error_label.pack()
        return

    # Clear the screen and display the greeting and buttons
    if error_label is not None:
        error_label.pack_forget()
        error_label = None
    
    entry.delete(0, tk.END)
    label.pack_forget()
    entry.pack_forget()
    submit_button.pack_forget()
    greeting = tk.Label(text="Hello, " + name)
    greeting.pack(pady=10)  # Add vertical spacing (10 pixels)
    quick_match_button.pack(pady=3)
    season_mode_button.pack(pady=3)
    create_character_button.pack(pady=3)
    settings_button.pack(pady=3)

window = tk.Tk()
window.geometry("300x200")

label = tk.Label(text="Name")
label.pack()

entry = tk.Entry()
entry.pack()

greeting = tk.Label(text="")

submit_button = tk.Button(text="Submit", command=print_entry)
submit_button.pack()

entry.bind("<Return>", lambda event: print_entry())

def removeButtons():
    greeting.pack_forget()
    quick_match_button.pack_forget()
    season_mode_button.pack_forget()
    create_character_button.pack_forget()
    settings_button.pack_forget()

def quick_match():
    # Clear the screen
    removeButtons()

def season_mode():
    removeButtons()

def create_character():
    removeButtons()

def settings():
    removeButtons()

quick_match_button = tk.Button(text="Quick Match", command=quick_match)
season_mode_button = tk.Button(text="Season Mode", command=season_mode)
create_character_button = tk.Button(text="Create a Character", command=create_character)
settings_button = tk.Button(text="Settings", command=settings)






window.mainloop()

