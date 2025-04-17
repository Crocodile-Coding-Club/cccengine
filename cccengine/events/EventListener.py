from cccengine.events.Event import Event


class EventListener:
    listeners: list = []

    def __init__(self):
        EventListener.listeners.append(self)

    def onEvent(self, event: Event):
        event.execute()
