from base import Vector, Particle
from PlayBoard import PlayBoard

if __name__ == '__main__':
    p1 = Particle(3000000, Vector(1, 2), Vector())
    p2 = Particle(4000000, Vector(6, 3), Vector())
    p3 = Particle(5000000, Vector(7, 2), Vector())
    pb = PlayBoard(p1, p2, p3)
    pb.simulate()