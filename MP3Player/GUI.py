from tkinter import *

class GUIElement(Tk):

    __owner = None
    __width = 300
    __height = 300

    def __init__(self, owner):
        __owner = owner
        

    def setWidth(width):
        __width = width

class GUI:

    __root = None

    def __init__(self, **kwargs):
        __root = Tk()

    def getRoot():
        return __root

    def Update():
        mainloop()