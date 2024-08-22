import tkinter as tk
from PIL import Image, ImageTk
import subprocess


def start_game():
    """
    Open the Pygame when the Start button is clicked
    """
    subprocess.Popen(["python", "maze.py"])


# Creates the main window
root = tk.Tk()
root.title("Maze Game Launcher")

# Background image!
background_image = Image.open("den-pixelart-cards.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Creates a label for the background image
background_label = tk.Label(root, image=background_photo)
background_label.pack()

# Creates a label for instructions with nice text
instructions_text = "Welcome to the Maze Game!\n\n"
instructions_text += "Your goal in the maze is to avoid the blocks and reach the square.\n\n"
instructions_text += "Click the button below to start."
instructions_label = tk.Label(root, text=instructions_text, font=("Arial", 14), bg="white",
                              fg="#333333")  # Adjusted text color
instructions_label.place(relx=0.5, rely=0.4, anchor="center")  # Adjusted vertical position

# Create a button to start the game with styled text
start_button = tk.Button(root, text="START!", command=start_game, font=("Arial", 16, "bold"), bg="#F9F3CC",
                         fg="#333333", padx=20, pady=10)  # Adjusted button color and text color
start_button.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted vertical position

# Run the GUI
root.mainloop()
