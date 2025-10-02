import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
    
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
    
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")
    
    def test_isosceles_right(self):
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles Right")
    
    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(-1, 2, 2), "Not a triangle")
        self.assertEqual(classify_triangle(0, 5, 5), "Not a triangle")

if __name__ == "__main__":
    with open("test_output.txt", "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)
