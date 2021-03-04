import unittest
import pytest
import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(fibonacci.nthFibonacci(0), 0)
        self.assertEqual(fibonacci.nthFibonacci(1), 1)
        self.assertEqual(fibonacci.nthFibonacci(2), 1)
        self.assertEqual(fibonacci.nthFibonacci(3), 2)
        self.assertEqual(fibonacci.nthFibonacci(4), 3)
        self.assertEqual(fibonacci.nthFibonacci(5), 5)
        self.assertEqual(fibonacci.nthFibonacci(10), 55)
    
    def test_invalid(self):
        self.assertRaises(ValueError, fibonacci.nthFibonacci, -1)
        self.assertRaises(ValueError, fibonacci.nthFibonacci, -2)
        self.assertRaises(ValueError, fibonacci.nthFibonacci, -3)

    def test_valid2(self):
        assert fibonacci.nthFibonacci(0) == 0
        assert fibonacci.nthFibonacci(1) == 1
        assert fibonacci.nthFibonacci(2) == 1
        assert fibonacci.nthFibonacci(3) == 2
        assert fibonacci.nthFibonacci(4) == 3
        assert fibonacci.nthFibonacci(5) == 5
        assert fibonacci.nthFibonacci(10) == 55

    def test_invalid2(self):
        with pytest.raises(ValueError):
            fibonacci.nthFibonacci(-1)
            fibonacci.nthFibonacci(-2)
            fibonacci.nthFibonacci(-3)  

if __name__ == "__main__":
    unittest.main(verbosity=2)