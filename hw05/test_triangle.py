"""
test the classify_triangle function in triangle.py
"""

import unittest
import triangle


class TestTriangles(unittest.TestCase):
    """
    test the function in different ways
    """

    def test_invalid_input(self):
        """
        check type and range
        """
        self.assertEqual(triangle.classify_triangle(2, 2, -3), 'not valid')
        self.assertEqual(triangle.classify_triangle('a', '2', 3), 'not valid')
        self.assertEqual(triangle.classify_triangle(0, 1, 1), 'not valid')
        self.assertEqual(triangle.classify_triangle(1, 1, 2147483649), 'not valid')

    def test_invalid_triangle(self):
        """
        check if can be a trianle
        """
        self.assertEqual(triangle.classify_triangle(1, 2, 3), 'not a triangle')

    def test_right_triangle(self):
        """
        check if isosceles and right and scalene and right
        """
        self.assertEqual(triangle.classify_triangle(1, 1, 1.414213), 'isosceles and right')
        self.assertEqual(triangle.classify_triangle(3, 4, 5), 'scalene and right')

    def test_equilateral_triangle(self):
        """
        check if equilateral
        """
        self.assertEqual(triangle.classify_triangle(1, 1, 1), 'equilateral')

    def test_isosceles_triangle(self):
        """
        check if isosceles
        """
        self.assertEqual(triangle.classify_triangle(2, 2, 3), 'isosceles')
        self.assertEqual(triangle.classify_triangle(23333, 2147483648, 2147483648), 'isosceles')

    def test_scalene_triangle(self):
        """
        check if scalene
        """
        self.assertEqual(triangle.classify_triangle(4, 5, 6), 'scalene')
        self.assertEqual(triangle.classify_triangle(2147483646, 2147483647, 2147483648), 'scalene')


if __name__ == '__main__':
    unittest.main()
