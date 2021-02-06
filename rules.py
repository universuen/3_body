from base import Particle

G = 6.67e-11


# elastic collision
def collide(p1: Particle, p2: Particle):
    assert p1.pos == p2.pos
    p1_v = (p1.v * (p1.m - p2.m) + 2 * p2.momentum) / (p1.m + p2.m)
    p2_v = (p2.v * (p2.m - p1.m) + 2 * p1.momentum) / (p1.m + p2.m)
    p1.v = p1_v
    p2.v = p2_v


# universal gravitation
def gravitation(p1: Particle, p2: Particle):
    r = (p1.pos - p2.pos).norm
    if r == 0:
        return 0
    delta_pos = p2.pos - p1.pos
    force_scalar = G * p1.m * p2.m / r ** 2
    force = (delta_pos / r) * force_scalar
    return force


