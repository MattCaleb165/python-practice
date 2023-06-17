import tkinter as tk

# Try importing the Tkinter module
try:
    import tkinter
    from tkinter import messagebox
except ImportError:
    print("Tkinter module not found. Please ensure Tkinter is installed.")
    exit(1)

# Tkinter is installed, print the version information
print("Tkinter version:", tkinter.TkVersion)
