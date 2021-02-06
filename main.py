from base import Vector, Particle
from PlayBoard import PlayBoard

if __name__ == '__main__':
    p1 = Particle(300, Vector(10, 20), Vector(5, 1))
    p2 = Particle(4000, Vector(50, 30), Vector(1, -6))
    p3 = Particle(500, Vector(70, 80), Vector(-7, 3))
    pb = PlayBoard(p1, p2, p3)
    pb.simulate()