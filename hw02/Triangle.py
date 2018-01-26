def classify_triangle(a, b, c):
    types = {'equilateral': 'equilateral',
             'isosceles': 'isosceles',
             'scalene': 'scalene',
             'isosceles and right': "isosceles and right",
             'scalene and right': 'scalene and right',
             'not valid': 'not valid'}
    sides = [a, b, c]
    try:
        if not validate_input(sides):
            return types['not valid']
    except TypeError:
        return types['not valid']

    sides = parse_input(sides)

    if not validate_sides(sides):
        return 'not valid'

    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == b and b == c:
        triangle_types = types['equilateral']
    elif a == b or b == c:
        triangle_types = types['isosceles']
        if check_right(a, b, c):
            triangle_types = types['isosceles and right']
    else:
        triangle_types = types['scalene']
        if check_right(a, b, c):
            triangle_types = types['scalene and right']

    return triangle_types


def validate_input(sides):
    for element in sides:
        if element <= 0:
            return False

    return True


def parse_input(sides):
    parsed = []
    for element in sides:
        parsed.append(float(element))
    return sorted(parsed)


def validate_sides(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True


def check_right(a, b, c):
    if round(a * a, 2) + round(b * b, 2) == round(c * c, 2):
        return True
    return False
