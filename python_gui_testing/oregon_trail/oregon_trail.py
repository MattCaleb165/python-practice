import tkinter as tk

is_running = False  # Global variable to control the game loop

def game_loop(stop_word):
    def handle_quit(event):
        global is_running
        is_running = False

    # Bind the Quit event to handle_quit function
    window.bind("<Destroy>", handle_quit)

    while is_running:
        # Wait for user input
        window.wait_variable(user_input)

        # Get the input value from the shared variable
        input_value = user_input.get()

        # Process user input
        process_input(input_value, stop_word)

def process_input(input_value, stop_word):
    global is_running

    # Implement command processing logic here

    # Example: Handle "quit" command
    if input_value.lower() == stop_word.lower():
        print_to_gui("Goodbye!")
        # End the game loop
        is_running = False
        window.destroy() # Close the Tkinter window

def start_game(stop_word):
    global is_running

    print_to_gui("Welcome to the Text Adventure Game!\n")
    print_to_gui("Type '{}' to exit the game.\n".format(stop_word))

    is_running = True  # Start the game loop
    game_loop(stop_word)

def print_to_gui(message):
    text_output.config(state="normal")
    text_output.insert("end", message + "\n")
    text_output.config(state="disabled")
    text_output.see("end")

# Create the main window
window = tk.Tk()

# Create a Text widget for game output
text_output = tk.Text(window, width=40, height=10)
text_output.pack()

# Create an Entry widget for user input
input_text = tk.Entry(window)
input_text.pack()

# Create a shared variable to store the user input
user_input = tk.StringVar()

def process_enter_key(event):
    # Get the input value
    input_value = input_text.get()

    # Store the input value in the shared variable
    user_input.set(input_value)

    # Clear the input field
    input_text.delete(0, "end")

# Bind the Enter key press event to the function
input_text.bind("<Return>", process_enter_key)

# Create a button to start the game
stop_word = "quit"  # Specify the stop word
start_button = tk.Button(window, text="Start Game", command=lambda: start_game(stop_word))
start_button.pack()

# Redirect stdout to the Text widget
import sys
sys.stdout = text_output

# Start the tkinter event loop
window.mainloop()
