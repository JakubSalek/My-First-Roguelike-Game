from Items.Item import Item


class Inventory:
    itemsInBag = []
    headSlot = Item
    armorSlot = Item
    bootsSlot = Item
    weaponSlot = Item
    ringSlot = Item

    def __init__(self):
        self.maxBackPackSlots = 15
