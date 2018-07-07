from tkinter import *

class GUI:

    def __init__(self, **kwargs):
        root = Tk()
        root.minsize(300,150)
        root.mainloop()

class Window:
    __width = 300
    __height = 300

    def __init__(self, width, height):
        __width = width
        __height = height