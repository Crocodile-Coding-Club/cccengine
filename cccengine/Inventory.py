class Inventory:
    """
    Inventory class
    """
    def __init__(self):
        """
        Initialize an Inventory instance
        """
        self.items = {}
        """
        {
            "category1": [{
                "item_ID1": {
                    "object": "class",  # return the object
                    "item_name": "str",
                    "owned": "int"  # number of item owned
                }
            },
            {
                "item_ID2": {
                    "object": "class",  # return the object
                    "item_name": "str",
                    "owned": "int"  # number of item owned
                }
            }],
            "category2": [
                ...
            ]
            ...
        }
        """

    def addCategory(self, name):
        """
        Add an item category in the inventory
        """
        self.items[name] = {}

    def addItem(self, object, amount = 1):
        """
        Add an amount of item into the inventory
        """ 
        if not object.getID() in self.items[object.getCategory()]:
            self.items[object.getCategory()][object.getID()] = {
                "object": object,
                "item_name": object.getName(),
                "owned": amount
            }
        else:
            self.items[object.getCategory()][object.getID()]["amount"] += amount

    def getItems(self):
        """
        Get all the items as a list of dictionaries
        """
        items = []
        for category in self.items:
            items.append(self.items[category])
        return items

    def getCategory(self, category):
        """
        Get the items of a specific category as a list of dictionaries
        """
        return self.items[category]
    
    def removeItem(self, object, amount = 1):
        """
        Remove an amount of item from the inventory
        """
        item = self.items[object.getCategory()][object.getID()]
        print(item["owned"])
        assert amount <= item["owned"], "[Error]: amount is over the quantity owned"

        item["owned"] -= amount
        if item["owned"] == 0:
            del self.items[object.getCategory()][object.getID()]
