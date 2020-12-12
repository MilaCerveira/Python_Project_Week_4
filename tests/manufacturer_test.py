import unittest 

from models.manufacturer import Manufacturer

class TestManufacturer (unittest.TestCase):
    def setup (self):
        self.manufacturer_1 = Manufacturer ('Pioneer', '8380 4944', 'www.pioneer.com','orders@pioneer.com')
        self.manufacturer_2 = Manufacturer ('Juno', '6680 3344', 'www.juno.com','order@juno.com')
    
    def test_manufacturer_has_name(self):
        self.assertEqual('Pioneer', self.manufacturer_1.name)

    def test_manufacturer_has_phone_number(self):
        self.assertEqual('8380 4944', self.manufacturer_1.phone)

    def test_manufacturer_has_website(self):
        self.assertEqual('www.pioneer.com', self.manufacturer_1.website)

    def test_manufacturer_has_email(self):
        self.assertEqual('orders@pioneer.com', self.manufacturer_1.email)

    def test_manufacturer_has_id(self):
        self.assertEqual(None, self.manufacturer_1.id) 
        





