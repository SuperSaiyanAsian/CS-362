import unittest
import FullName

class TestFullName(unittest.TestCase):

    def test_1(self):
        self.assertEqual(FullName.generateFullName("Vijay", "Tadimeti"), "Vijay Tadimeti")

    def test_2(self):
        self.assertRaises(TypeError, FullName.generateFullName, "Cody", 7)

    def test_3(self):
        self.assertRaises(TypeError, FullName.generateFullName, "Mahon", "Khosh7")

if __name__ == "__main__":
    unittest.main(verbosity=2)