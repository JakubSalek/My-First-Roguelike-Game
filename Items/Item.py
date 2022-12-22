from Items import ItemStats
from Items.ItemSlotType import ItemSlotType


class Item:
    name = ""
    description = ""
    possibleToWearSlots = ItemSlotType.NONE
    stats = ItemStats
