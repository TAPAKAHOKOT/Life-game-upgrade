import turtle as tt


class Settings:
    def __init__(self):

        self.show_borders = False

        self.main_drawer = tt.Turtle()
        self.main_drawer.speed(0)
        self.main_drawer.hideturtle()
        self.main_drawer.fillcolor("red")

        self.dots_num = 1

        self.f_tr = 0.97

        self.dots_gravity_rad = 60

        self.borders = 400

        self.polar_number = 4

        self.dots_rad = 1

        self.colors = ["red", "blue", "green", "purple"]
