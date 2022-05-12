from object_scene import ObjectScene
from ball import Ball


class Player(ObjectScene):
    def __init__(self, canvas, name: str, width: int, height: int, position_x, position_y, ball: Ball):
        super().__init__(name, position_x, position_y)

        self.canvas = canvas
        self.name_id = name
        self.WIDTH = width
        self.HEIGHT = height
        self.position_x = position_x
        self.position_y = position_y
        self.player_can_move = False

        self.ball = ball

        self.player_speed_x = 0
        self.player_speed_y = 10

        self.player_length = 10
        self.player_height = 50

        self.left_position = None
        self.top_position = None
        self.right_position = None
        self.bottom_position = None

        self.player = canvas.create_rectangle(10, 10, 20, 60, fill="white")
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

    def can_move(self, direction):
        self.player_can_move = False
        if self.name_id == "player_left":
            (self.left_position, self.top_position, self.right_position,
             self.bottom_position) = self.canvas.coords(self.player)
            # print("player", self.left_position, self.top_position, self.right_position, self.bottom_position)
            if direction == "down" and self.top_position == 0:
                self.player_can_move = True
            elif direction == "top" and self.top_position == 250:
                self.player_can_move = True
            elif 0 < self.top_position < 250:
                self.player_can_move = True
            else:
                self.player_can_move = False

    def send_position_player(self):
        self.ball.set_new_position_player_in_list(self.name_id, self.left_position, self.top_position,
                                                  self.right_position, self.bottom_position)
