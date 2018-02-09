import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):

    def testInvalidInput(self):
        """
        T1
        2. Verify the Input
        """
        self.assertEqual(classify_triangle(2, 2, -3), 'not valid')

        self.assertEqual(classify_triangle('a', '2', 3), 'not valid')

    def testInvalidTriangle(self):
        """
        T2
        3. Verify that the sides form a legal triangle
        :return:
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'not valid')

    def testRightTriangle(self):
        """
        T3
        4. Determine if the triangle is a right triangle
        6. Display type of triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1.414213), 'isosceles and right')

        self.assertEqual(classify_triangle(3, 4, 5), 'scalene and right')

    def testEquilateralTriangle(self):
        """
        T4
        5.1 If the sides are all equal, then the triangle is “Equilateral”
        6. Display type of triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')

    def testIsoscelesTriangle(self):
        """
        T5
        5.2 Else if two side are equal, but not three, then the triangle is “Isosceles”
        6. Display type of triangle
        """
        self.assertEqual(classify_triangle(2, 2, 3), 'isosceles')

    def testScaleneTriangle(self):
        """
        T6
        5.2 Else if two side are equal, but not three, then the triangle is “Isosceles”
        6. Display type of triangle
        """
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene')


if __name__ == '__main__':
    unittest.main()

