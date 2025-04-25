class Quest:
    """
    Quest Class
    """
    def __init__(self, name, category, description):
        """
        Initialize a Quest Instance
        """
        self.name = name
        self.category = category # story/annex ?
        self.description = description
        self.completed = False

    def getName(self):
        """
        Get the name of the quest
        """
        return self.name
    
    def getCategory(self):
        """
        Get the category of the quest
        """
        return self.category
    
    def getDescription(self):
        """
        Get the decription of the quest
        """
        return self.description
    
    def getStatus(self):
        """
        Get the status of the quest (True if completed False if not)
        """
        return self.completed