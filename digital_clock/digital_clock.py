# Import the required modules
from tkinter import *  # Used for creating the GUI
from time import strftime  # Used for formatting the time string

# Create the main window for the application
root = Tk()
root.title("Digital Clock")  # Set the title of the window

# Create and configure the label widget to display the time
label = Label(root, font=("areal", 160, "bold"), bg="black", fg="white")
label.pack(anchor="center", fill="both", expand=1)  # Place the label in the center of the window, filling and expanding it

# Define a function to update the label with the current time
def Time():
    # Get the current time in 12-hour format with AM/PM
    string = strftime("%I:%M:%S %p")
    # Update the label's text with the current time
    label.config(text=string)
    # Schedule the Time function to run again after 1000 milliseconds (1 second)
    label.after(1000, Time)

# Call the Time function to start the clock
Time()

# Run the main loop to keep the application window open
root.mainloop()