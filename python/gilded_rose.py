# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def increase_backstage_quality(item):
        if item.sell_in < 0:
            return item.quality * -1
        elif item.sell_in < 5:
            return 3
        elif item.sell_in < 10:
            return 2
        else:
            return 1

    def update_quality(self):
        improving_items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]
        constant_items = ["Sulfuras, Hand of Ragnaros"]

        for item in self.items:
            # advance time
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            # set degrade speed based on item type and sell by date
            degrade_speed = 1
            if item.name == "Conjured":
                degrade_speed *= 2
            if item.sell_in < 0:
                degrade_speed *= 2

            # standard items degrade
            if not item.name in improving_items + constant_items:
                degrade_speed *= -1

            # set degrade speed differently for special items
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                degrade_speed = self.increase_backstage_quality(item)

            if item.name == "Sulfuras, Hand of Ragnaros":
                degrade_speed = 0
            # set item quality (to between 0 and 50) according to degrade speed
            item.quality = max(min(item.quality + degrade_speed, 50), 0)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
