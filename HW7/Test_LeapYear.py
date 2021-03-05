import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):

    def test_1(self):
        self.assertEqual(LeapYear.leap(420), "Year 420 is a leap year.")
        self.assertEqual(LeapYear.leap(421), "Year 421 is not a leap year.")

    def test_2(self):
        self.assertEqual(LeapYear.leap(300), "Year 300 is not a leap year.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
