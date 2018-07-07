from GUI import *

class MP3Player:
    """Base Class for App"""
    gui = GUI()

    window = Window(gui.getRoot())
    gui.Update()