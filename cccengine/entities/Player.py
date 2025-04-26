from cccengine.entities.Entity import Entity

class Player(Entity):
    """
    Player Class
    """
    def __init__(self, player_name, x, y):
        """
        Initialize a Player instance
        """
        assert type(player_name) == str, "[Error]: player_name must be a string"
        
        super().__init__("player", y, x)

        self.player_name = player_name

    def getName(self):
        """
        Get the name of the player
        """
        return self.player_name

    def setName(self, player_name):
        """
        Set the name of the player
        """
        assert type(player_name) == str, "[Error]: player_name must be a string"

        self.player_name = player_name
