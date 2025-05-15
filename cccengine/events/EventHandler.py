from cccengine.events.EventListener import EventListener
from cccengine.events.Event import Event


class EventHandler:
    """
    EventHandler Class
    """

    def __init__(self, eventListeners: list[EventListener] = []):
        """
        Initialize a EventHandler instance
        """
        self.eventListeners: list[EventListener] = eventListeners
        self.events: list[Event]  = []

    def execute(self):
        """
        Execute every Events
        """
        for eventListener in self.eventListeners:
            for event in self.events:
                eventListener.onEvent(event)
                self.events.remove(event)

    def addEvent(self, event):
        """
        Add an Event
        """
        assert issubclass(type(event), Event)==True

        self.events.append(event)

    def removeEvent(self, event):
        """
        Remove an Event
        """
        assert type(event) == Event, "[Error]: event must be an Event instance"

        self.events.remove(event)
