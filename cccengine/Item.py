class Item:
    """
    Item Class
    """
    def __init__(self, item_name, item_ID, category):
        """
        Initialize a Player instance
        """
        self.item_name = item_name
        self.item_ID = item_ID
        self.category = category

    def getName(self):
        """
        Get the name of the item
        """
        return self.item_name

    def getID(self):
        """
        Get the ID of the item
        """
        return self.item_ID
    
    def getCategory(self):
        """
        Get the category of the item
        """
        return self.category
