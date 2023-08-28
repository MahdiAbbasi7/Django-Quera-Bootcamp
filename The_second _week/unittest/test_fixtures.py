"""test for fixtures"""

import unittest
from fixtures import Person

class TestFixture(unittest.TestCase):
    def setUp(self):
        self.p1 = Person("mahdi", "abbasi")
        self.p2 = Person("john", "deo")     

    def tearDown(self):
        print("Tear down fixture")

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), "mahdi abbasi")
        self.assertEqual(self.p2.fullname(), "john deo")

    def test_email(self):
        self.assertEqual(self.p1.email(), "mahdiabbasi@gmail.com")
        self.assertEqual(self.p2.email(), "johndeo@gmail.com")

if __name__ == "__main__":
    unittest.main()

