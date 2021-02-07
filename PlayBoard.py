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

        temp_list = self.p_list.copy()
        for i, _ in enumerate(temp_list):
            temp_list[i] = temp_list[i].copy()

        for i, p in enumerate(temp_list):
            if p.is_alive is False:
                continue

            # update velocity
            a = Vector()
            for other_p in temp_list:
                if other_p == p or other_p.is_alive is False:
                    continue
                elif (other_p.pos - p.pos).norm < 1:
                    collide(p, other_p)
                    continue
                else:
                    a += gravitation(p, other_p) / p.m
            v = update_vec(p.v, a)
            # update position
            pos = update_vec(p.pos, p.v)
            temp_list[i].pos = pos
            temp_list[i].v = v
            if self._update_cnt % 50 == 0:
                self.line_list[i][0].append(pos.x)
                self.line_list[i][1].append(pos.y)
                if len(self.line_list[i][0]) > 1000:
                    self.line_list[i][0].pop(0)
                    self.line_list[i][1].pop(0)

        self.p_list = temp_list.copy()

    def simulate(self, generation=-1):
        plt.ion()
        plt.style.use('dark_background')

        total_m = sum([p.m for p in self.p_list])
        while generation != 0:
            # calculate the coordinates
            self._update()
            generation -= 1
            if generation % 1000 == 0:
                # show the particles
                for i, line in enumerate(self.line_list):
                    plt.scatter(line[0], line[1], s=10 * (self.p_list[i].m / total_m))
                    # break
                plt.show()
                plt.pause(0.001)
                plt.figure(1).clear()
                # print([p.v.norm for p in self.p_list])
