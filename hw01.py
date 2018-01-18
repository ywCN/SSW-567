import unittest


class TriangleClassification:
    def __init__(self):
        self.user_input = input('Please enter three sides separated by commas.')
        self.sides = self.parse_input()
        self.validate_input()
        self.classify_triangle()

    def parse_input(self):
        elements = self.user_input.split(',')
        parsed = []

        for element in elements:
            parsed.append(float(element.strip()))

        return sorted(parsed)

    def validate_input(self):
        if len(self.sides) != 3:
            raise Exception('You must enter exactly 3 elements.')

    def validate_triangle(self):
        if self.sides[0] + self.sides[1] <= self.sides[2]:
            raise Exception('Your triangle sides are not valid.')

    def classify_triangle(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        triangle_types = ''
        if a == b and b == c:
            triangle_types += 'equilateral'
        elif a == b or b == c:
            triangle_types += 'isosceles'
        else:
            triangle_types += 'scalene'
            if round(a * a, 6) + round(b * b, 6) == round(c * c, 6):
                triangle_types += 'and right'

        return triangle_types

    def run(self):
        """
        driver function
        :return: None
        """


def main():
    demo = TriangleClassification()
    demo.__init__()


if __name__ == '__main__':
    main()

