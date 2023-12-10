import tkinter as tk

stop_word = "quit"  # Specify the stop word
user_input = None  # Global variable to store user input

is_running = False  # Global variable to control the game loop

def game_loop():
    global is_running
    process_input()

    if is_running:
        window.after(100, game_loop)  # Check for input every 100 milliseconds

def stop_game():
    global is_running
    is_running = False
    print_to_gui("Goodbye!")  # Display a farewell message or perform any necessary cleanup tasks
    window.destroy()  # Close the Tkinter window

def process_input():
    global is_running, user_input

    # Example: Handle "quit" command
    if user_input.get().lower() == stop_word.lower():
        stop_game()
    else:
        # Process other commands
        pass

def start_game():
    global is_running, user_input
    user_input = tk.StringVar()  # Initialize user_input as a StringVar
    is_running = True
    game_loop()

def print_to_gui(message):
    text_output.insert(tk.END, message + "\n")  # Append the message to the Text widget
    text_output.see(tk.END)  # Scroll to the end of the Text widget to show the latest message

# Create the main window
window = tk.Tk()

# Create a Text widget for game output
text_output = tk.Text(window, width=40, height=10)
text_output.pack()

# Create an Entry widget for user input
input_text = tk.Entry(window)  # Remove textvariable=user_input
input_text.pack()

def process_enter_key(event):
    # Store the input value in the user_input variable
    user_input.set(input_text.get())

# Bind the Enter key press event to the function
input_text.bind("<Return>", process_enter_key)

# Create a button to start the game
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

print_to_gui("Welcome to the Text Adventure Game!\n")
print_to_gui("Type '{}' to exit the game.\n".format(stop_word))

# Redirect stdout to the Text widget
import sys
sys.stdout = text_output

# Start the tkinter event loop
window.mainloop()
