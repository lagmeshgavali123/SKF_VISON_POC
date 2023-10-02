# import required library
import webbrowser
from tkinter import *

# creating root
root = Tk()

# setting GUI title
root.title("WebBrowsers")

# setting GUI geometry
root.geometry("1024x720")

# call webbrowser.open() function.
webbrowser.open("http://127.0.0.1:8000/")
