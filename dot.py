import turtle as tt
import math as m
from random import randint as rnd


class Dot:
    def __init__(self, x_cor, y_cor, pol, settings):
        self.settings = settings
        self.dwr = self.settings.main_drawer
        self.show_borders = self.settings.show_borders

        self.mass = 10

        self.x = x_cor
        self.y = y_cor

        self.speed_x = 0
        self.speed_y = 0

        self.f_speed_x = 0
        self.f_speed_y = 0

        self.rad = self.settings.dots_rad
        self.gravity_rad = self.settings.dots_gravity_rad

        self.polarity = pol
        self.polarity_koef = 1

    def draw(self):
        self.dwr.up()
        self.dwr.goto(self.x, self.y - self.rad)
        self.dwr.down()

        self.dwr.color(self.settings.colors[self.polarity - 1])
        self.dwr.width(5)
        self.dwr.circle(self.rad)

        if self.show_borders:
            self.draw_borders()

        self.dwr.setheading(0)

    def update_pos(self):
        if -self.settings.borders < self.x + self.speed_x < self.settings.borders:
            self.x += self.speed_x

            if self.speed_x != 0:
                self.speed_x *= self.settings.f_tr

                if abs(self.speed_x) <= 0.05:
                    self.speed_x = 0

        if -self.settings.borders < self.y + self.speed_y < self.settings.borders:
            self.y += self.speed_y

            if self.speed_y != 0:
                self.speed_y *= self.settings.f_tr

                if abs(self.speed_y) <= 0.05:
                    self.speed_y = 0

    def check_gravity(self, x, y, polar):
        if m.sqrt((self.x - x)**2 + (self.y - y)**2) <= self.gravity_rad * 2:
            if polar == self.polarity:
                self.polarity_koef = -1
            else:
                self.polarity_koef = 1
            # self.polarity_koef = -1

            full_dist = m.sqrt((self.x - x)**2 + (self.y - y)**2)

            dist_x = abs(self.x - x)
            koef_x = -1 if self.x < x else 1

            if dist_x <= self.gravity_rad:
                self.f_speed_x = koef_x * \
                    (dist_x / self.gravity_rad) / 13

            dist_y = abs(self.y - y)
            koef_y = -1 if self.y < y else 1

            if dist_y <= self.gravity_rad:
                self.f_speed_y = koef_y * \
                    (dist_y / self.gravity_rad) / 13

            self.speed_x += self.f_speed_x * self.polarity_koef
            self.speed_y += self.f_speed_y * self.polarity_koef

            return True
        return False

    def draw_borders(self):
        self.dwr.up()
        self.dwr.goto(self.x, self.y - self.gravity_rad)
        self.dwr.down()

        self.dwr.color("green")
        self.dwr.width(1)
        self.dwr.circle(self.gravity_rad)
