from base import Vector, Particle
from PlayBoard import PlayBoard

if __name__ == '__main__':
    p_list = [
        Particle(60, Vector(10, 20), Vector(0.5, -0.5)),
        Particle(60, Vector(50, 10), Vector(-1.5, 0)),
        Particle(60, Vector(35, 0), Vector(2, 0.2)),
    ]
    pb = PlayBoard(*p_list)
    pb.simulate()
