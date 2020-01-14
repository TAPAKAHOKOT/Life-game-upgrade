# здесь подключаются модули
import pygame as pg
from dot import Dot
from settings import Settings
import time
from random import randint as rnd
import math as m
import os


if __name__ == "__main__":
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (100, 100)

    # здесь определяются константы, классы и функции
    FPS = 60

    # здесь происходит инициация, создание объектов и др.
    pg.init()

    size = 800
    screen = pg.display.set_mode((size, size), flags=pg.DOUBLEBUF | pg.NOFRAME)

    surf = pg.Surface((size, size))
    clock = pg.time.Clock()

    settings = Settings(size, surf)
    # если надо до цикла отобразить объекты на экране
    pg.display.update()
    pg.font.init()
    myfont = pg.font.SysFont('Comic Sans MS', 10)

    arr = []
    poses = []
    # coors = []
    n = 550
    chanse = 3

    for k in range(n):
        x, y = rnd(0, settings.borders),\
            rnd(0, settings.borders)

        # x, y = 300 + 0 * k, 500 + k * 150

        # x, y = rnd(300, 350), rnd(300, 350)
        # polar = rnd(1, settings.polar_number)
        polar = rnd(1, 3 + chanse)
        polar = 1 if polar < 1 + chanse else polar - chanse + 1
        arr.append(Dot(x, y, polar, settings))

    rects_ready = False

    for dot in arr:
        dot.draw()
    # главный цикл
    while True:
        surf.fill((31, 46, 46))

        # задержка
        clock.tick(FPS)

        fps = round(clock.get_fps())

        text_fps = myfont.render(str(fps), True, (0, 255, 0))

        mouse_pos = pg.mouse.get_pos()
        m_rect = (int(mouse_pos[0] - settings.dots_gravity_rad * 5), int(mouse_pos[1] - settings.dots_gravity_rad * 5),
                  int(settings.dots_gravity_rad * 10), int(settings.dots_gravity_rad * 10))
        m_rect = pg.Rect(m_rect)

        for k in m_rect.collidelistall([k.rect for k in arr]):
            arr[k].check_gravity(mouse_pos[0], mouse_pos[1], "mouse", 100)

        for dot in arr:
            dot.borders_gravity()

            for t in dot.rect.collidelistall([k.rect for k in arr]):
                t = arr[t]
                if t != dot:
                    dot.check_gravity(t.x, t.y, t.polarity)

            dot.update_pos()

            dot.draw()
            if settings.show_borders:
                dot.draw_borders()

        rects_ready = True

        screen.blit(surf, (0, 0))
        # pg.display.update(surf)

        screen.blit(text_fps, (10, 10))

        # цикл обработки событий
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

        # --------
        # изменение объектов и многое др.
        # --------

        # обновление экрана
        pg.display.update()
