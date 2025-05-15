import pygame
from cccengine.events.Event import Event
import cccengine.events.EventHandler as EventHandler


class ButtonClickEvent(Event):
    """
    ButtonClickEvent Class
    """

    def __init__(self, eventHandler: "EventHandler.EventHandler" , button, clicks):
        """
        Initialize a ButtonClickEvent instance
        """

        super().__init__("Button Click Event")

        self.button = button
        self.clicks = clicks
        self.eventHandler: "EventHandler.EventHandler" = eventHandler
        eventHandler.addEvent(self)

    def getClicks(self):
        return self.clicks

    def getButtons(self):
        return self.button

    def getGui(self):
        """
        Get the gui of the event
        """
        return self.button.getGui()

    def execute(self):
        if self.cancel == False:
            self.button.clicked(self.clicks)
            print("works")
 