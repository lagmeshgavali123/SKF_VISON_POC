import tkinter as tk
from tkinter import ttk
import time

def loading_simulation():
    # Create the main tkinter window
    window = tk.Tk()
    window.title("Loading")

    # Create a progress bar
    progress = ttk.Progressbar(window, mode='indeterminate')
    progress.pack(pady=20)

    # Start the progress bar animation
    progress.start()

    # Close the tkinter window when the loading is complete
    # You can replace this with any logic that determines when the loading is done
    # For example, you can use a timer or an event to trigger this.
    window.after(5000, window.destroy)  # Close the window after 5 seconds (adjust as needed)

    # Start the tkinter main loop
    window.mainloop()

if __name__ == "__main__":
    while True:
        print("Loading screen is running...")
        time.sleep(3)
        loading_simulation()
