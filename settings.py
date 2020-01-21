import turtle as tt


class Settings:
    def __init__(self, size, screen):

        self.screen = screen

        self.show_borders = False

        self.mouse_force = 4

        self.dots_num = 1

        self.f_tr = 0.93

        self.dots_gravity_rad = 30

        self.borders = size

        self.polar_number = 1

        self.lines = []

        self.dots_rad = 2

        self.obs = []

        # self.maxpspeed = 150

        self.colors = [(255, 51, 0), (102, 153, 255),
                       (255, 191, 0), (241, 156, 187)]

        # 1: red       2: blue       3:yellow       4: pink

        self.polars = {
            1: {"1": 0.9999999, "2": 0, "3": 1, "4": 0, "mouse": self.mouse_force},
            2: {"1": 0, "2": 0.999, "3": 1, "4": 1, "mouse": self.mouse_force},
            3: {"1": 0.1, "2": 1, "3": 1, "4": 0, "mouse": self.mouse_force},
            4: {"1": 1, "2": 1, "3": 3, "4": -0.1, "mouse": self.mouse_force}
        }
