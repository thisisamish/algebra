import math
from functools import reduce


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new_coordinates = [coord1 + coord2 for (coord1, coord2) in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self, v):
        new_coordinates = [coord1 - coord2 for (coord1, coord2) in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def scalar_mul(self, scalar):
        new_coordinates = [scalar * coord for coord in self.coordinates]
        return Vector(new_coordinates)

    def mag(self):
        return math.sqrt(sum([coord ** 2 for coord in self.coordinates]))

    def normalize(self):
        try:
            return self.scalar_mul(1 / self.mag())
        except ZeroDivisionError:
            raise Exception("Cannot normalize a zero vector")

    def is_zero_vector(self):
        return reduce(lambda x, y: x & y, [True if coord == 0 else False for coord in self.coordinates])

    def dot_prod(self, v):
        if v.is_zero_vector() or self.is_zero_vector():
            return 0
        return sum([coord1 * coord2 for (coord1, coord2) in zip(v.coordinates, self.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            angle_in_rad = math.acos(self.normalize().dot_prod(v.normalize()))
            return math.degrees(angle_in_rad) if in_degrees else angle_in_rad
        except ZeroDivisionError:
            raise Exception("Cannot find angle with a zero vector")


v1 = Vector([0, 1])
v2 = Vector([-1, 1])
print(v1.angle_with(v2, in_degrees=True))
