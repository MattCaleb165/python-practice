import tkinter as tk
import random

is_running = False  # Global variable to control the game loop

is_running = True  # Flag to indicate if the game is running

def game_loop(stop_word):
    global is_running

    while is_running:
        user_input = process_input()  # Get user input from the GUI

        if user_input.lower() == stop_word.lower():
            stop_game()  # Call the stop_game function to stop the game
        else:
            process_input(user_input)

def stop_game():
    global is_running
    is_running = False
    print_to_gui("Goodbye!")  # Display a farewell message or perform any necessary cleanup tasks


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

    game_action()

    is_running = True  # Start the game loop
    game_loop(stop_word)

player_health = 100  # Initial health value
def game_action():
    global player_health

    outcomes = {
        1: find_treasure_chest,
        2: encounter_friendly_npc,
        3: stumble_upon_hidden_passage,
        4: attack_by_monster,
        5: nothing_interesting_happens
    }

    outcome = random.randint(1, 5)

    if outcome in outcomes:
        action = outcomes[outcome]
        action()

    if player_health <= 0:
        print_to_gui("Game over! Your health has reached zero.")
        stop_game()

def find_treasure_chest():
    global player_health
    print_to_gui("You find a treasure chest!")
    player_health += 10
    if player_health < 0:
        player_health = 0
    print_to_gui("Your health increases by 10. Current health: {}".format(player_health))

def encounter_friendly_npc():
    global player_health
    print_to_gui("You encounter a friendly NPC.")
    # Perform some action that affects the player's health

def stumble_upon_hidden_passage():
    global player_health
    print_to_gui("You stumble upon a hidden passage.")
    # Perform some action that affects the player's health

def attack_by_monster():
    global player_health
    print_to_gui("You are attacked by a monster!")
    player_health -= 20
    if player_health < 0:
        player_health = 0
    print_to_gui("Your health decreases by 20. Current health: {}".format(player_health))

def nothing_interesting_happens():
    print_to_gui("Nothing interesting happens.")

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

print_to_gui("Welcome to the Text Adventure Game!\n")
print_to_gui("Type '{}' to exit the game.\n".format(stop_word))

# Redirect stdout to the Text widget
import sys
sys.stdout = text_output

# Start the tkinter event loop
window.mainloop()
