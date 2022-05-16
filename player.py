from object_scene import ObjectScene
from ball import Ball


class Player(ObjectScene):
    def __init__(self, canvas, name_id: str, position_a, position_b, position_c, position_d, ball: Ball):
        super().__init__(name_id, position_a, position_b, position_c, position_d)

        self.canvas = canvas
        self.name_id = name_id

        self.position_a = position_a
        self.position_b = position_b
        self.position_c = position_c
        self.position_d = position_d

        self.player_can_move = False

        self.ball = ball

        self.player_speed_x = 0
        self.player_speed_y = 10

        self.player = canvas.create_rectangle(self.position_a, self.position_b, self.position_c, self.position_d,
                                              fill="white")

        self.ball.set_new_position_object_in_list(self.name_id, self.position_a, self.position_b,
                                                  self.position_c, self.position_d)

        self.movement()

    def movement(self):
        self.canvas.move(self.player, self.player_speed_x, self.player_speed_y)

    def move_top(self, _):
        direction = "top"
        self.can_move(direction)
        if self.player_can_move:
            self.send_position_player()
            self.player_speed_y = -10
            self.movement()

    def move_down(self, _):
        direction = "down"
        self.can_move(direction)
        if self.player_can_move:
            self.send_position_player()
            self.player_speed_y = +10
            self.movement()

    def position_reset(self):
        self.position_a = None
        self.position_b = None
        self.position_c = None
        self.position_d = None

    def can_move(self, direction):
        self.player_can_move = False
        self.position_reset()
        (self.position_a, self.position_b, self.position_c,
         self.position_d) = self.canvas.coords(self.player)
        if direction == "down" and self.position_b == 0:
            self.player_can_move = True
        elif direction == "top" and self.position_b == 250:
            self.player_can_move = True
        elif 0 < self.position_b < 250:
            self.player_can_move = True
        else:
            self.player_can_move = False

    def send_position_player(self):
        self.ball.set_new_position_object_in_list(self.name_id, self.position_a, self.position_b,
                                                  self.position_c, self.position_d)
