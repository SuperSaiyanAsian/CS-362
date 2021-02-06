import unittest
import CubeVolume

class TestCubeVolume(unittest.TestCase):

    def test_1(self):
        self.assertEqual(CubeVolume.findVolume(5), 125)

    def test_2(self):
        self.assertEqual(CubeVolume.findVolume(-6.9), -329)

    def test_3(self):
        self.assertRaises(TypeError, CubeVolume.findVolume, "six")

if __name__ == "__main__":
    unittest.main(verbosity=2)