from base import Vector, Particle, update_vec
from rules import collide, gravitation


class PlayBoard:
    def __init__(self, *args):
        self.p_list = list()
        for p in args:
            assert isinstance(p, Particle)
            self.p_list.append(p)

    def _update(self):
        for p in self.p_list:
            pos = update_vec(p.pos, p.v)
            a = Vector()
            for other_p in self.p_list:
                if other_p == p:
                    continue
                a += gravitation(p, other_p) / p.m
            v = update_vec(p.v, a)
            p.pos = pos
            p.v = v

    def simulate(self, generation=-1):
        while generation != 0:
            generation -= 1
            self._update()
            for p in self.p_list:
                print(p.pos)

