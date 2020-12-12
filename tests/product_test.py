import unittest 

from models.product import Product

class TestProduct (unittest.TestCase):
    def setup(self):
        self.product_1 = Product('Omnitronic BD-1350 Turntable', 'Belt drive DJ turntable with adjustable speed control', '50', '80', '150')
        self.product_2 = Product('Pioneer DDJ-400', 'DJ Controller with FULL Rekordbox Software', '40', '150', '200' ) 

    def test_product_has_name (self):
        self.assertEqual('Omnitronic BD-1350 Turntable', self.product_1.name)

    def test_product_has_description(self):
        self.assertEqual ('Belt drive DJ turntable with adjustable speed control', self.product_1.description)
    
    def test_stock_quantity (self):
        self.assertEqual ('50', self.product_1.stock_quantity)

    def test_buying_cost (self):
        self.assertEqual ('80', self.product_1.buying_cost)

    def test_selling_price (self):
        self.assertEqual ('150', self.product_1.selling_price)

    def test_product_has_id(self):
        self.assertEqual (None, self.product_1.id)
