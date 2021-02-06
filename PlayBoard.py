from base import Vector, Particle, update_vec
from rules import collide, gravitation
from matplotlib import pyplot as plt


class PlayBoard:
    def __init__(self, *args):
        self.p_list = list()
        self.line_list = list()
        for p in args:
            assert isinstance(p, Particle)
            self.p_list.append(p)
            self.line_list.append([list(), list()])
        self._update_cnt = 0

    def _update(self):
        self._update_cnt += 1
        for i, p in enumerate(self.p_list):
            if p.is_alive is False:
                continue
            pos = update_vec(p.pos, p.v)
            a = Vector()
            for other_p in self.p_list:
                if other_p == p or other_p.is_alive is False:
                    continue
                elif (other_p.pos - p.pos).norm < 0.001:
                    collide(p, other_p)
                    continue
                else:
                    a += gravitation(p, other_p) / p.m
            v = update_vec(p.v, a)
            p.pos = pos
            if self._update_cnt % 50 == 0:
                self.line_list[i][0].append(p.pos.x)
                self.line_list[i][1].append(p.pos.y)
                if len(self.line_list[i][0]) > 1000:
                    self.line_list[i][0].pop(0)
                    self.line_list[i][1].pop(0)
            p.v = v

    def simulate(self, generation=-1):
        plt.ion()
        plt.style.use('dark_background')

        total_m = sum([p.m for p in self.p_list])
        while generation != 0:
            # calculate the coordinates
            self._update()
            generation -= 1
            if generation % 300 == 0:
                # show the particles
                for i, line in enumerate(self.line_list):
                    plt.scatter(line[0], line[1], s=10 * (self.p_list[i].m / total_m))
                    # break
                plt.show()
                plt.pause(0.001)
                plt.figure(1).clear()
