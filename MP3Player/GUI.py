from tkinter import *

class GUI:

    __root = None

    def __init__(self, **kwargs):
        __root = Tk()
        mainloop()

    def getRoot():
        return __root

    def Update():
        mainloop()

class Window(Tk):

    __owner = None
    __width = 300
    __height = 300

    def __init__(self, owner):
        __owner = owner
        

    def setWidth(width):
        __width = width

