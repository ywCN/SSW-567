import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquilateralTriangle(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene')

    def testRightTriangle(self):
        self.assertEqual(classify_triangle(1, 1, 1.414213), 'isosceles and right')

        self.assertEqual(classify_triangle(3, 4, 5), 'scalene and right')

    def testInvalidTriangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'not valid')

        self.assertEqual(classify_triangle(2, 2, -3), 'not valid')

        self.assertEqual(classify_triangle('a', '2', 3), 'not valid')


if __name__ == '__main__':
    unittest.main()

