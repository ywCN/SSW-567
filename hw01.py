import unittest

class TriangleClassification:
    def __init__(self, a=None, b=None, c=None):
        self.sides = [a, b, c]

    def validate_input(self):
        if None in self.sides:
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
        if not self.validate_input():
            return False

        self.parse_input()
        # print(self.sides)

        if not self.validate_sides():
            return False
        print(self.sides)


        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]

        triangle_types = ''
        if a == b and b == c:
            triangle_types += 'equilateral'
        elif a == b or b == c:
            triangle_types += 'isosceles'
            if self.check_right(a, b, c):
                triangle_types += ' and right'
        else:
            triangle_types += 'scalene'
            if self.check_right(a, b, c):
                triangle_types += ' and right'

        return triangle_types

    def run(self):
        """
        driver function
        :return: None
        """

        triangle_types = self.classify_triangle()

        if triangle_types:
            print('Your triangle is ' + triangle_types + '.')


# class TestTriangleClassification(unittest.TestCase):
#     def test



def main():
    demo = TriangleClassification(1, 2, 3)
    demo.run()


if __name__ == '__main__':
    main()
    # unittest.main()

