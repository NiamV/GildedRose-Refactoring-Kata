# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_backstage_quality(self, item):
        if item.sell_in < 6 and item.quality < 48:
                item.quality += 3
        elif item.sell_in < 11 and item.quality < 49:
                item.quality += 2
        elif item.quality < 50:
            item.quality += 1


    def update_quality(self):
        improving_items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]
        constant_items = ["Sulfuras, Hand of Ragnaros"]

        for item in self.items:
            if (not item.name in improving_items + constant_items) and item.quality > 0:
                item.quality = item.quality - 1
            elif not item.name in constant_items:
                if item.quality < 50 and item.name != "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = item.quality + 1
                else:
                    self.increase_backstage_quality(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
