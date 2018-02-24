"""
This file will validate input and return a string triangle type.
"""
def classify_triangle(side_a, side_b, side_c):
    """
    This function accepts 3 inputs and returns a string triangle type.
    """
    types = {'equilateral': 'equilateral',
             'isosceles': 'isosceles',
             'scalene': 'scalene',
             'isosceles and right': "isosceles and right",
             'scalene and right': 'scalene and right',
             'not valid': 'not valid',
             'not a triangle': 'not a triangle'}
    sides = [side_a, side_b, side_c]
    try:
        if not validate_input(sides):
            return types['not valid']
    except TypeError:
        return types['not valid']

    sides = parse_input(sides)

    if not validate_sides(sides):
        return types['not a triangle']

    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]

    if side_a == side_b and side_b == side_c:
        triangle_types = types['equilateral']
    elif side_a == side_b or side_b == side_c:
        triangle_types = types['isosceles']
        if check_right(side_a, side_b, side_c):
            triangle_types = types['isosceles and right']
    else:
        triangle_types = types['scalene']
        if check_right(side_a, side_b, side_c):
            triangle_types = types['scalene and right']

    return triangle_types


def validate_input(sides):
    """
    check input range
    """
    for element in sides:
        if element <= 0 or element > 2147483648:
            return False

    return True


def parse_input(sides):
    """
    convert input to float
    """
    parsed = []
    for element in sides:
        parsed.append(float(element))
    return sorted(parsed)


def validate_sides(sides):
    """
    check if can be a triangle
    """
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True


def check_right(side_a, side_b, side_c):
    """
    check if it is a right triangle
    """
    if round(side_a * side_a, 2) + round(side_b * side_b, 2) == round(side_c * side_c, 2):
        return True
    return False
