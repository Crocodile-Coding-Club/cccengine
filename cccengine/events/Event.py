class Event:
    """
    Event Class
    """
    def __init__(self, event_name, cancel = False):
        """
        Initialize an Event instance
        """
        assert type(event_name) == str, "[Error]: event_name must be a string"
        assert type(cancel) == bool, "[Error]: cancel must be a boolean"

        self.event_name = event_name
        self.cancel = cancel

    def getEventName(self):
        """
        Get the name of the event
        """
        return self.event_name

    def getCancel(self):
        """
        Get the state of the event
        """
        return self.cancel
    
    def setCancel(self, cancel):
        """
        Set the state of the event
        """
        assert type(cancel) == bool, "[Error]: cancel must be a boolean"

        return self.cancel
    
    def execute(self):
        pass
