# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_degrades_double(self):
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        currentQual = items[0].quality
        gilded_rose.update_quality()
        self.assertEqual((10 - currentQual)*2, currentQual - items[0].quality)

    def test_nonnegative_quality(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 10):
            gilded_rose.update_quality()
        self.assertTrue(items[0].quality >= 0)

    def test_agedbrie_improves(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(items[0].quality > 0)

    def test_not_more_than_50_quality(self):
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 10):
            gilded_rose.update_quality()
        self.assertTrue(items[0].quality <= 50)

    def test_Sulfuras_is_constant(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)
        self.assertEqual(items[0].sell_in, 5)

    def test_Backstage_Passes_Aged_Correctly_MoreThan10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 7)

    def test_Backstage_Passes_Aged_Correctly_LessThan10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)

    def test_Backstage_Passes_Aged_Correctly_LessThan5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)

    def test_Backstage_Passes_Aged_Correctly_LessThan0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_degrades_doubly(self):
        items = [Item("Conjured", 5, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)



        
if __name__ == '__main__':
    unittest.main()
