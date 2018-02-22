import unittest
import Triangle


class TestTriangles(unittest.TestCase):

    def testInvalidInput(self):
        self.assertEqual(Triangle.classify_triangle(2, 2, -3), 'not valid')
        self.assertEqual(Triangle.classify_triangle('a', '2', 3), 'not valid')
        self.assertEqual(Triangle.classify_triangle(0, 1, 1), 'not valid')
        self.assertEqual(Triangle.classify_triangle(1, 1, 2147483649), 'not valid')

    def testInvalidTriangle(self):
        self.assertEqual(Triangle.classify_triangle(1, 2, 3), 'not a triangle')

    def testRightTriangle(self):
        self.assertEqual(Triangle.classify_triangle(1, 1, 1.414213), 'isosceles and right')
        self.assertEqual(Triangle.classify_triangle(3, 4, 5), 'scalene and right')

    def testEquilateralTriangle(self):
        self.assertEqual(Triangle.classify_triangle(1, 1, 1), 'equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(Triangle.classify_triangle(2, 2, 3), 'isosceles')
        self.assertEqual(Triangle.classify_triangle(23333, 2147483648, 2147483648), 'isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(Triangle.classify_triangle(4, 5, 6), 'scalene')
        self.assertEqual(Triangle.classify_triangle(2147483646, 2147483647, 2147483648), 'scalene')


if __name__ == '__main__':
    unittest.main()
