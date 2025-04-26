from cccengine.Sprite import Sprite

class Entity(Sprite):
    """
    Entity class
    """
    def __init__(self, type, x=0, y=0, skills=[]):
        """
        Initialize an Entity instance
        """
        self.type = type
        self.x = x
        self.y = y
        self.skills = skills

    def getType(self):
        """
        Get the type of the entity
        """
        return self.type

    def getLocation(self):
        """
        Get the x and y position of the entity
        """

        return (self.x, self.y)

    def getX(self):
        """
        Get the x position of the entity
        """

        return self.x

    def setX(self, x):
        """
        Set the x position of the entity
        """
        assert type(x) == int, "[Error]: x must be an integer"

        self.x = x

    def getY(self):
        """
        Get the y position of the entity
        """

        return self.y
    
    def setY(self, y):
        """
        Set the y position of the entity
        """
        assert type(y) == int, "[Error]: y must be an integer"

        self.y = y

    def getSkills(self):
        """
        Get the skills of the entity
        """
        return self.skills