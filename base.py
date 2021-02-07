import math

TIME_GRANULARITY = 1e-3


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y)

    # scalar multiplication
    def __mul__(self, other: float):
        return Vector(other * self.x, other * self.y)

    def __rmul__(self, other: float):
        return self.__mul__(other)

    def __truediv__(self, other: float):
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    @property
    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Particle:
    def __init__(self, quality: float, position: Vector, velocity: Vector):
        self.m = quality
        self.pos = position
        self.v = velocity

        self._alive = True

    @property
    def momentum(self):
        return self.m * self.v

    @property
    def kinetic_energy(self):
        return 0.5 * self.m * (self.v.norm ** 2)

    @property
    def is_alive(self):
        return self._alive

    def __str__(self):
        return f'Particle({self.m}, {self.pos}, {self.v})'

    def remove(self):
        self._alive = False
        self.m = 0
        self.v = Vector()

    def copy(self):
        p = Particle(self.m, self.pos, self.v)
        p._alive = self._alive
        return p


def update_vec(vector: Vector, derivative: Vector):
    delta = derivative * TIME_GRANULARITY
    return vector + delta
