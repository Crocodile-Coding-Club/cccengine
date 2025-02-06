import pygame
from cccengine.events.Event import Event
from gui.Gui import Gui


class ButtonClickEvent(Event):
    """
    ButtonClickEvent Class
    """

    def __init__(self, button: Button, clickType, button: Button):
        """
        Initialize a ButtonClickEvent instance
        """
        assert type(gui) == Gui, "[Error]: gui must be a Gui instance"

        super().__init__()

        self.event_name = "Button Click Event"
        self.button = button

    def getGui(self):
        """
        Get the gui of the event
        """
        return self.gui

    def execute(self):
        if self.cancel == False:
            self.gui.display()
