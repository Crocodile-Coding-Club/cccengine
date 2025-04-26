from cccengine.events.Event import Event
from Player import Player


class PlayerCastEvent(Event):
    """
    PlayerCastEvent Class
    """

    def __init__(self, player=None, power=None):
        """
        Initialize a PlayerCastEvent instance
        """
        assert type(player) == Player, "[Error]: player must be a Player instance"

        super().__init__("Player Cast Event")

        self.player = player
        self.power = power

    def getPlayer(self):
        """
        Get the player of the event
        """
        return self.player

    def setPlayer(selfx, player):
        """
        Set the player of the event
        """
        assert type(player) == Player, "[Error]: player must be a Player instance"

        self.player = player

    def getPower(self):
        """
        Get the power of the event
        """
        return self.power

    def setPower(self, power):
        """
        Set the power of the event
        """
        assert type(power) == Power, "[Error]: power must be a Power instance"

        self.power = power
