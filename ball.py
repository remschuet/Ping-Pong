import random

from object_scene import ObjectScene
from points import Point


class Ball(ObjectScene):
    def __init__(self, name_id, canvas, width: int, height: int, position_a, position_b, position_c,
                 position_d, root, points_left: Point, points_right: Point):
        super().__init__(name_id, position_a, position_b, position_c, position_d)

        self.name = name_id
        self.canvas = canvas
        self.WIDTH = width
        self.HEIGHT = height
        self.root = root

        self.points_left = points_left          # ADD POINTS
        self.points_right = points_right

        self.position_a = position_a
        self.position_b = position_b
        self.position_c = position_c
        self.position_d = position_d

        self.speed_x = 4
        self.speed_y = 4

        self.player_position_dic = {}

        self.ball = canvas.create_oval(self.position_a, self.position_b, self.position_c, self.position_d, fill="white")

        self.check_collision_border()

    def position_reset(self):
        self.position_a = None
        self.position_b = None
        self.position_c = None
        self.position_d = None

    def check_collision_border(self):
        self.canvas.move(self.ball, self.speed_x, self.speed_y)
        self.position_reset()
        (self.position_a, self.position_b, self.position_c,
         self.position_d) = self.canvas.coords(self.ball)

        if self.check_collision_with_object(self.name, self.position_a, self.position_b, self.position_c, self.position_d):
            print("touché")
            self.move_ball_direction_x()

        elif self.position_a <= 0:
            self.points_right.add_points()
            self.move_ball_direction_x()

        elif self.position_c >= self.WIDTH:
            self.points_left.add_points()
            self.move_ball_direction_x()

        elif self.position_b <= 0 or self.position_d >= self.HEIGHT:
            print(self.position_a, self.position_b, self.position_c, self.position_d)
            self.speed_y = -int(self.speed_y)
            self.position_b = -int(self.speed_y)

        self.set_new_position_object_in_list(self.name, self.position_a, self.position_b,
                                             self.position_c, self.position_d)
        self.canvas.after(30, self.check_collision_border)

    def move_ball_direction_x(self):
        print(self.position_a, self.position_b, self.position_c, self.position_d)
        self.speed_x = -int(self.speed_x)
        self.position_a = -int(self.speed_x)
        self.set_new_position_object_in_list(self.name, self.position_a, self.position_b,
                                             self.position_c, self.position_d)

    def set_new_position_object_in_list(self, players_name, position_a, position_b, position_c, position_d):
        self.player_position_dic[players_name] = (position_a, position_b,
                                                  position_c, position_d)
        # print(self.player_position_dic)

    def check_collision_with_object(self, name, position_a, position_b, position_c, position_d):
        for object_name, (a, b, c, d) in self.player_position_dic.items():
            if name != object_name:
                if c >= position_a and \
                        a <= position_c and \
                        d >= position_b and \
                        b <= position_d:
                    return True
        return False
