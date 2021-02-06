import unittest
import ListAverage

class TestListAverage(unittest.TestCase):

    def test_1(self):
        self.assertEqual(ListAverage.findAverage([3.62,-420,1337,-6.9]), 228)
    
    def test_2(self):
        self.assertRaises(ZeroDivisionError, ListAverage.findAverage, [])

    def test_3(self):
        self.assertRaises(TypeError, ListAverage.findAverage, [3.62,-420,1337,"six.9"])

if __name__ == "__main__":
    unittest.main(verbosity=2)