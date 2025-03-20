class Player(Sprite):
    """
    Player Class
    """
    def __init__(self, player_name, player_x, player_y):
        """
        Initialize a Player instance
        """
        assert type(player_name) == str, "[Error]: player_name must be a string"
        
        super().__init__()

        self.player_name = player_name
        self.player_x = player_x
        self.player_y = player_y

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

    def getLocation(self):
        """
        Get the x and y position of the player
        """

        return (self.player_x, self.player_y)

    def getX(self):
        """
        Get the x position of the player
        """

        return self.player_x

    def setX(self, player_x):
        """
        Set the x position of the player
        """
        assert type(player_x) == int, "[Error]: player_x must be an integer"

        self.player_x = player_x

    def getY(self):
        """
        Get the y position of the player
        """

        return self.player_y
    
    def setY(self, player_y):
        """
        Set the y position of the player
        """
        assert type(player_y) == int, "[Error]: player_y must be an integer"

        self.player_y = player_y