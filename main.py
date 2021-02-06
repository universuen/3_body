from base import Vector, Particle
from PlayBoard import PlayBoard

if __name__ == '__main__':
    p1 = Particle(30, Vector(10, 20), Vector())
    p2 = Particle(40, Vector(30, 15), Vector())
    p3 = Particle(50, Vector(70, 25), Vector())
    pb = PlayBoard(p1, p2, p3)
    pb.simulate()