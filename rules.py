from base import Particle, Vector

G = 1


# collision
def collide(p1: Particle, p2: Particle):
    if p1.is_alive and p2.is_alive:
        v = (p1.momentum + p2.momentum) / (p1.m + p2.m)
        m = p1.m + p2.m
        p1.v = v
        p1.m = m
        p2.remove()


# universal gravitation
def gravitation(p1: Particle, p2: Particle):
    r = (p1.pos - p2.pos).norm
    # if they get too close, the law will no longer work
    # if any([r < 0.1 * p1.m, r < 0.1 * p2.m]):
    #     r *= 0.01 * p1.m * p2.m
    delta_pos = p2.pos - p1.pos
    force_scalar = G * p1.m * p2.m / (r ** 2)
    force = (delta_pos / r) * force_scalar
    return force
