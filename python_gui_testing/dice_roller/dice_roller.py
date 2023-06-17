import tkinter as tk
from dice_options import roll_dice
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create the main window
window = tk.Tk()
window.title("Dice Roller")

# Load dice images from URLs
dice_urls = [
    "https://opengameart.org/sites/default/files/side_1_pip.png",
    "https://opengameart.org/sites/default/files/side_2_pips.png",
    "https://opengameart.org/sites/default/files/side_3_pips.png",
    "https://opengameart.org/sites/default/files/side_4_pips.png",
    "https://opengameart.org/sites/default/files/side_5_pips.png",
    "https://opengameart.org/sites/default/files/side_6_pips.png"
]

dice_images = []
for url in dice_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        resized_image = image.resize((50, 50))  # Resize the image to width 100, maintaining aspect ratio
        dice_images.append(ImageTk.PhotoImage(resized_image))
    except (requests.exceptions.HTTPError, Image.UnidentifiedImageError) as e:
        print(f"Error loading image from URL: {url}. Error: {e}")

# Create a label and entry for specifying the number of dice
num_dice_label = tk.Label(window, text="Number of Dice:")
num_dice_label.pack()

num_dice_entry = tk.Entry(window)
num_dice_entry.pack()

# Create a button for rolling the dice
roll_button = tk.Button(
    window,
    text="Roll Dice",
    command=lambda: roll_and_display_dice(int(num_dice_entry.get()), selected_dice_type.get())
)
roll_button.pack()

# Create a label for displaying the results
result_label = tk.Label(window, text="Results:")
result_label.pack()

# Create a label for displaying the dice images
dice_image_label = tk.Label(window)
dice_image_label.pack()

# Create a label for the dice type
dice_type_label = tk.Label(window, text="Dice Type:")
dice_type_label.pack()

# Create buttons for selecting dice type
selected_dice_type = tk.StringVar()
selected_dice_type.set("6-sided")  # Default selected dice type
dice_type_buttons_frame = tk.Frame(window)
dice_type_buttons_frame.pack()

def select_dice_type(dice_type):
    selected_dice_type.set(dice_type)
    # Update the button appearance based on the selected dice type
    dice_type_6_button.config(relief=tk.SUNKEN if dice_type == "6-sided" else tk.RAISED)
    dice_type_4_button.config(relief=tk.SUNKEN if dice_type == "4-sided" else tk.RAISED)

dice_type_6_button = tk.Button(dice_type_buttons_frame, text="6-sided", command=lambda: select_dice_type("6-sided"))
dice_type_6_button.pack(side=tk.LEFT, padx=5)

dice_type_4_button = tk.Button(dice_type_buttons_frame, text="4-sided", command=lambda: select_dice_type("4-sided"))
dice_type_4_button.pack(side=tk.LEFT, padx=5)

def roll_and_display_dice(num_dice, dice_type):
    if dice_type == "6-sided":
        dice_results = roll_dice(num_dice, dice_type="6-sided")  # Pass the 'dice_type' argument
    elif dice_type == "4-sided":
        dice_results = roll_dice(num_dice, dice_type="4-sided")  # Pass the 'dice_type' argument
    result_label.config(text=f"Results: {dice_results}")

    # Display dice images
    dice_images_to_display = []
    for result in dice_results:
        dice_images_to_display.append(dice_images[result - 1])

    # Update the image label
    if dice_images_to_display:
        dice_image_label.config(image=dice_images_to_display[0])  # Display the first image

# Start the tkinter event loop
window.mainloop()


#Notes: Currently the app runs, and expresses the values, but it only displays the first face.