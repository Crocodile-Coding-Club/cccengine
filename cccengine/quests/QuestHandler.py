class QuestHandler:
    """
    QuestHandler Class
    """
    def __init__(self, quests=[]):
        """
        Initialize a QuestHandler instance
        """
        self.quests = quests

    def getQuests(self):
        """
        Get the quests of the player
        """
        return self.quests

    def addQuest(self, quest):
        """
        Add a Quest
        """
        if not quest in self.quests:
            self.quests.append(quest)
        
