import unittest


class TriangleClassification:
    def __init__(self, *arg):
        self.sides = []
        for argument in arg:
            self.sides.append(argument)
        self.types = {'equilateral': 'equilateral',
                      'isosceles': 'isosceles',
                      'scalene': 'scalene',
                      'isosceles and right': 'isosceles and right',
                      'scalene and right': 'scalene and right',
                      'not valid': 'not valid',
                      'invalid input': 'not valid. Please check your input'}

    def validate_input(self):
        if len(self.sides) != 3:
            return False
        for element in self.sides:
            if element <= 0:
                return False

        return True

    def parse_input(self):
        parsed = []
        for element in self.sides:
            parsed.append(float(element))
        self.sides = sorted(parsed)

    def validate_sides(self):
        if self.sides[0] + self.sides[1] <= self.sides[2]:
            return False
        return True

    @staticmethod
    def check_right(a, b, c):
        if round(a * a, 2) + round(b * b, 2) == round(c * c, 2):
            return True
        return False

    def classify_triangle(self):
        try:
            if not self.validate_input():
                return self.types['invalid input']
        except TypeError:
            return self.types['invalid input']

        self.parse_input()

        if not self.validate_sides():
            return 'not valid'

        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]

        if a == b and b == c:
            triangle_types = self.types['equilateral']
        elif a == b or b == c:
            triangle_types = self.types['isosceles']
            if self.check_right(a, b, c):
                triangle_types = self.types['isosceles and right']
        else:
            triangle_types = self.types['scalene']
            if self.check_right(a, b, c):
                triangle_types = self.types['scalene and right']

        return triangle_types

    def run(self):
        """
        driver function
        :return: None
        """

        triangle_types = self.classify_triangle()

        if triangle_types:
            print('Your triangle is ' + triangle_types + '.')


class TestTriangleClassification(unittest.TestCase):
    def test_classify_triangle(self):
        t0 = TriangleClassification(1, 1, 1)
        self.assertEqual(t0.classify_triangle(), 'equilateral')

        t1 = TriangleClassification(1, 2, 3)
        self.assertEqual(t1.classify_triangle(), 'not valid')

        t2 = TriangleClassification(2, 2, 3)
        self.assertEqual(t2.classify_triangle(), 'isosceles')

        t3 = TriangleClassification(4, 5, 6)
        self.assertEqual(t3.classify_triangle(), 'scalene')

        t4 = TriangleClassification(1, 1, 1.414213)
        self.assertEqual(t4.classify_triangle(), 'isosceles and right')

        t5 = TriangleClassification(3, 4, 5)
        self.assertEqual(t5.classify_triangle(), 'scalene and right')

        t6 = TriangleClassification(3, 4, 5, 6)
        self.assertEqual(t6.classify_triangle(), 'not valid. Please check your input')

        t7 = TriangleClassification(1, 2)
        self.assertEqual(t7.classify_triangle(), 'not valid. Please check your input')

        t8 = TriangleClassification('a', 'b')
        self.assertEqual(t8.classify_triangle(), 'not valid. Please check your input')



# def main():
#     TriangleClassification(1, 2, 3).run()
#     TriangleClassification(2, 2, 3).run()
#     TriangleClassification(4, 5, 6).run()
#     TriangleClassification(1, 1, 1.414213).run()
#     TriangleClassification(3, 4, 5).run()


if __name__ == '__main__':
    # main()
    unittest.main()

