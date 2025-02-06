import pygame
from cccengine.events.Event import Event


class GuiOpenEvent(Event):
    """
    GuiOpenEvent Class
    """

    def __init__(self, guiManager, gui):
        """
        Initialize a GuiOpenEvent instance
        """
        super().__init__()

        self.event_name = "Gui Open Event"
        self.gui = gui
        self.guiManager = guiManager

    def getGui(self):
        """
        Get the gui of the event
        """
        return self.gui

    def getGuiManager(self):
        """
        Get the gui manager linked to the gui
        """
        return self.guiManager

    def execute(self):
        if self.cancel == False:
            self.guiManager.guis.append(self.gui)
