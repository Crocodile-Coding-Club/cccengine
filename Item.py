class Itme:
    """
    Item Class
    """
    def __init__(self, item_name, item_ID):
        """
        Initialize a Player instance
        """
        self.item_name = item_name
        self.item_ID = item_ID

    def getName(self):
        """
        Get the name of the item
        """
        return self.item_name