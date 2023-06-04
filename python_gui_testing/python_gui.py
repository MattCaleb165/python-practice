import tkinter as tk

def button_clicked(option):
    print(f"You selected: {option}")

window = tk.Tk()

greeting = tk.Label(window, text="Welcome to the Game", fg="white", bg="black")
greeting.grid(row=0, column=0, padx=10, pady=10)

button_options = ["Start", "Character Select", "Settings"]
max_length = max(len(option) for option in button_options)

for i, button_text in enumerate(button_options):
    button_width = max(15, max_length + 5)  # Calculate dynamic button width based on longest option
    button = tk.Button(window, text=button_text, width=button_width, command=lambda opt=button_text: button_clicked(opt))
    button.grid(row=i, column=1, padx=10, pady=5, sticky="w")


window.mainloop()