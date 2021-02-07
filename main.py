from base import Vector, Particle
from PlayBoard import PlayBoard

if __name__ == '__main__':
    p_list = [
        Particle(90, Vector(10, 20), Vector(0, -1)),
        Particle(30, Vector(35, 15), Vector(-1.5, 1)),
        Particle(30, Vector(60, 25), Vector(0.9, 0.2)),
    ]
    pb = PlayBoard(*p_list)
    pb.simulate()
