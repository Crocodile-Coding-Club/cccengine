import pygame
from cccengine.events.Event import Event
from gui.Gui import Gui


class GuiOpenEvent(Event):
    """
    GuiOpenEvent Class
    """

    def __init__(self, gui: Gui, clickTypes):
        """
        Initialize a GuiOpenEvent instance
        """
        assert type(gui) == Gui, "[Error]: gui must be a Gui instance"

        super().__init__()

        self.event_name = "Gui Open Event"
        self.gui = gui

    def getSound(self):
        """
        Get the gui of the event
        """
        return self.gui

    def execute(self):
        if self.cancel == False:
            self.sound.play()
