import unittest


class Triangle:
    def __init__(self):
        self.user_input = input('Please enter three sides separated by commas.')
        self.sides = self.parse_input()
        self.validate_input()
        self.validate_triangle()

    def parse_input(self):
        elements = self.user_input.split(',')
        parsed = []

        try:
            for element in elements:
                parsed.append(float(element.strip()))
        except ValueError:
            print('\'{}\' is not a valid input.'.format(self.user_input))
            exit()
            return False

        return sorted(parsed)

    def validate_input(self):
        if len(self.sides) != 3:
            print('Your triangle must have exactly 3 sides.')
            return False
        return True

    def validate_triangle(self):
        if self.sides[0] + self.sides[1] <= self.sides[2]:
            print('Your triangle sides cannot build a triangle.')
            return False
        return True


class TriangleClassification:
    def __init__(self):
        self.triangle = Triangle()

    def classify_triangle(self):
        a = self.triangle.sides[0]
        b = self.triangle.sides[1]
        c = self.triangle.sides[2]

        triangle_types = ''
        if a == b and b == c:
            triangle_types += 'equilateral'
        elif a == b or b == c:
            triangle_types += 'isosceles'
        else:
            triangle_types += 'scalene'
            if round(a * a, 2) + round(b * b, 6) == round(c * c, 6):
                triangle_types += ' and right'

        return triangle_types

    def run(self):
        """
        driver function
        :return: None
        """

        triangle_types = self.classify_triangle()
        print('Your triangle is ' + triangle_types + '.')


class TestTriangle(unittest.TestCase):
    def test_parse_input(self):



class TriangleClassification(unittest.TestCase):



def main():
    demo = TriangleClassification()
    demo.run()


if __name__ == '__main__':
    main()
    unittest.main()

