from logging import handlers
from cccengine.events.EventListener import EventListener
from cccengine.events.Event import Event


class EventHandler:
    """
    EventHandler Class
    """

    def __init__(self, events=[]):
        """
        Initialize a EventHandler instance
        """
        EventHandler.handlers.append(self)

    def execute(self):
        """
        Execute every Events
        """
        for event in self.events:
            for listener in EventListener.listeners:
                listener.onEvent(event)
            self.launchEvent(event)

    def launchEvent(self, event):
        """
        Execute one event
        """
        assert type(event) == Event, "[Error]: event must be an Event instance"

        event.execute()

    def addEvent(self, event):
        """
        Add an Event
        """
        assert type(event) == Event, "[Error]: event must be an Event instance"

        self.events.append(event)

    def removeEvent(self, event):
        """
        Remove an Event
        """
        assert type(event) == Event, "[Error]: event must be an Event instance"

        self.events.remove(event)
