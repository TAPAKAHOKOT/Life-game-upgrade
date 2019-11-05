import turtle as tt
from dot import Dot
from settings import Settings
import time
from random import randint as rnd
import math as m

tt.tracer(0, 0)

settings = Settings()


def setka():
    set = tt.Turtle()
    set.speed(0)
    set.hideturtle()
    set.color("grey")

    c = [-settings.borders, -settings.borders]
    step_nums = 24
    step = abs(c[0] * 2 / step_nums)
    all_way = abs(c[0]) * 2

    for i in range(2):
        set.left(90)
        for k in range(step_nums + 1):
            set.up()
            set.goto(c[0], c[1])
            set.down()

            set.fd(all_way)
            c[i] += step
        all_way += step * 2


if settings.show_borders:
    setka()

arr = []
# coors = []
n = 100

for k in range(n):
    x, y = rnd(-settings.borders, settings.borders),\
        rnd(-settings.borders, settings.borders)
    polar = rnd(1, settings.polar_number)
    arr.append([Dot(x, y, polar, settings), x, y, polar])
    # coors.append([x, y, arr[k].polarity])

# print(coors)
while True:

    settings.main_drawer.clear()
    b = arr

    for n, dot in enumerate(arr):
        dot = dot[0]
        b = sorted(b, key=lambda el: m.sqrt(
            (el[1] - dot.x) ** 2 + (el[2] - dot.y)**2))

        for t in b:
            if not dot.check_gravity(t[1], t[2], t[3]):
                break

        dot.update_pos()
        arr[n][1] = dot.x
        arr[n][2] = dot.y

        dot.draw()

    # time.sleep(0.01)
    tt.update()


tt.mainloop()
