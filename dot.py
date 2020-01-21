# import turtle as tt
import math as m
from random import randint as rnd
import pygame as pg
# from numba import njit


class Dot:
    def __init__(self, x_cor, y_cor, pol, settings):

        self.settings = settings
        # self.dwr = self.settings.main_drawer
        self.show_borders = self.settings.show_borders

        self.mass = 10

        self.v = rnd(7, 13) / 10

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

        self.color = self.settings.colors[1]
        # self.color = self.settings.colors[self.polarity - 1]

    def draw(self):
        # self.rect_ch = pg.draw.circle(self.settings.screen, (31, 250, 46, 250),
        #                               (int(self.x), int(self.y)), self.gravity_rad, 1)

        self.rect_d = pg.draw.circle(self.settings.screen, self.color,
                                     (int(self.x), int(self.y)), self.rad)
        rect = (int(self.x - self.gravity_rad), int(self.y - self.gravity_rad),
                int(self.gravity_rad * 2), int(self.gravity_rad * 2))
        self.rect = pg.Rect(rect)

    def update_pos(self):
        if self.rad < self.x + self.speed_x < self.settings.borders - self.rad:
            self.x += self.speed_x

            # if self.speed_x > self.settings.maxpspeed:
            #     self.speed_x = self.settings.maxpspeed

            if self.speed_x != 0:
                self.speed_x *= self.settings.f_tr

                if abs(self.speed_x) <= 0.05:
                    self.speed_x = 0

        if self.rad < self.y + self.speed_y < self.settings.borders - self.rad:
            self.y += self.speed_y

            # if self.speed_y > self.settings.maxpspeed:
            #     self.speed_y = self.settings.maxpspeed

            if self.speed_y != 0:
                self.speed_y *= self.settings.f_tr

                if abs(self.speed_y) <= 0.05:
                    self.speed_y = 0

    def borders_gravity(self):
        # Отталкивание от стенок границы
        # <<<<<

        if self.y <= 60 or self.y >= self.settings.borders - 60\
                or self.x <= 60 or self.x >= self.settings.borders - 60:

            self.f_speed_x = 0
            self.f_speed_y = 0

            bb = 60
            force = 5
            dist = self.settings.borders - self.x
            if dist <= bb:
                self.speed_x -= ((bb - dist) / bb) * force * self.v
            dist = self.x
            if dist <= bb:
                self.speed_x += ((bb - dist) / bb) * force * self.v

            dist = self.settings.borders - self.y
            if dist <= bb:
                self.speed_y -= ((bb - dist) / bb) * force * self.v
            dist = self.y
            if dist <= bb:
                self.speed_y += ((bb - dist) / bb) * force * self.v
        # >>>>>

    def check_gravity(self, x, y, polar, gr=0):

        if not gr:
            gr = self.gravity_rad

        if m.sqrt((self.x - x)**2 + (self.y - y)**2) <= gr:

            if polar != "mouse":
                pg.draw.line(self.settings.screen, self.color,
                             (self.x, self.y), (x, y), 1)

            self.polarity_koef = self.settings.polars[
                self.polarity][str(polar)]
            if not self.polarity_koef:
                self.polarity_koef = -0.3

            full_dist = m.sqrt((self.x - x)**2 + (self.y - y)**2)

            dist_x = abs(self.x - x)
            koef_x = -1 if self.x < x else 1

            if dist_x <= gr:
                if dist_x != 0:
                    self.f_speed_x = koef_x * (dist_x / 50) * self.v
                    # self.f_speed_x = koef_x * \
                    #     ((self.gravity_rad - dist_x) / (self.gravity_rad / 2)) / 13

            dist_y = abs(self.y - y)
            koef_y = -1 if self.y < y else 1

            if dist_y <= gr:
                if dist_y != 0:
                    self.f_speed_y = koef_y * (dist_y / 50) * self.v
                    # self.f_speed_y = koef_y * \
                    #     ((self.gravity_rad - dist_y) / (self.gravity_rad / 2)) / 13

            self.speed_x += self.f_speed_x * self.polarity_koef
            self.speed_y += self.f_speed_y * self.polarity_koef
            #
            # self.f_speed_x *= self.polarity_koef
            # self.f_speed_y *= self.polarity_koef

            # if self.speed_x > self.settings.maxpspeed:
            #     self.speed_x = self.settings.maxpspeed
            #
            # if self.speed_y > self.settings.maxpspeed:
            #     self.speed_y = self.settings.maxpspeed

            return True
        return False

    def draw_borders(self):
        pg.draw.circle(self.settings.screen, self.settings.colors[2],
                       (int(self.x), int(self.y)), self.gravity_rad, 1)
