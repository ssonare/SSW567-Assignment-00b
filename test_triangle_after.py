"""
Unit tests for triangle classification module.
"""
import unittest
import os
from io import StringIO
import sys
from triangle import classify_triangle, main, write_results_to_file


class TestTriangle(unittest.TestCase):
    """Test cases for triangle classification function."""

    def test_equilateral(self):
        """Test equilateral triangle classification."""
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        """Test isosceles triangle classification."""
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_scalene(self):
        """Test scalene triangle classification."""
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        """Test right triangle classification."""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_isosceles_right(self):
        """Test isosceles right triangle classification."""
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles Right")

    def test_invalid_triangle_sum_equals(self):
        """Test invalid triangle where sum of two sides equals third."""
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")

    def test_negative_side(self):
        """Test triangle with negative side length."""
        self.assertEqual(classify_triangle(-1, 2, 2), "Not a triangle")

    def test_zero_side(self):
        """Test triangle with zero side length."""
        self.assertEqual(classify_triangle(0, 5, 5), "Not a triangle")

    def test_all_sides_zero(self):
        """Test triangle with all sides zero."""
        self.assertEqual(classify_triangle(0, 0, 0), "Not a triangle")

    def test_two_sides_zero(self):
        """Test triangle with two sides zero."""
        self.assertEqual(classify_triangle(0, 0, 5), "Not a triangle")

    def test_invalid_triangle_inequality_first_combination(self):
        """Test invalid triangle: a + b <= c."""
        self.assertEqual(classify_triangle(1, 2, 10), "Not a triangle")

    def test_invalid_triangle_inequality_second_combination(self):
        """Test invalid triangle: a + c <= b."""
        self.assertEqual(classify_triangle(1, 10, 2), "Not a triangle")

    def test_invalid_triangle_inequality_third_combination(self):
        """Test invalid triangle: b + c <= a."""
        self.assertEqual(classify_triangle(10, 1, 2), "Not a triangle")

    def test_equilateral_large_numbers(self):
        """Test equilateral triangle with large numbers."""
        self.assertEqual(classify_triangle(1000, 1000, 1000), "Equilateral")

    def test_equilateral_right(self):
        """Test that equilateral triangles are not classified as right."""
        result = classify_triangle(5, 5, 5)
        self.assertEqual(result, "Equilateral")
        self.assertNotIn("Right", result)

    def test_isosceles_not_right(self):
        """Test isosceles triangle that is not right."""
        result = classify_triangle(5, 5, 8)
        self.assertEqual(result, "Isosceles")
        self.assertNotIn("Right", result)

    def test_scalene_not_right(self):
        """Test scalene triangle that is not right."""
        result = classify_triangle(4, 5, 6)
        self.assertEqual(result, "Scalene")
        self.assertNotIn("Right", result)

    def test_floating_point_sides(self):
        """Test triangle with floating point side lengths."""
        result = classify_triangle(3.5, 4.5, 5.5)
        self.assertEqual(result, "Scalene")

    def test_main_function_executes(self):
        """Test that main function executes without errors."""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            main()
            output = captured_output.getvalue()
            # Verify some output was produced
            self.assertIn("Sides:", output)
            self.assertIn("Equilateral", output)
        finally:
            sys.stdout = sys.__stdout__

    def test_write_results_to_file_creates_file(self):
        """Test that write_results_to_file creates output file."""
        # Remove file if it exists
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        
        # Call the function
        write_results_to_file()
        
        # Verify file was created
        self.assertTrue(os.path.exists("output.txt"))
        
        # Verify file has content
        with open("output.txt", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Sides:", content)
            self.assertIn("Equilateral", content)
            self.assertIn("Not a triangle", content)
        
        # Clean up
        if os.path.exists("output.txt"):
            os.remove("output.txt")

    def test_write_results_file_content(self):
        """Test that output file contains expected results."""
        write_results_to_file()
        
        with open("output.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Should have 7 lines (one for each example)
            self.assertEqual(len(lines), 7)
        
        # Clean up
        if os.path.exists("output.txt"):
            os.remove("output.txt")


if __name__ == "__main__":
    with open("test_output.txt", "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)