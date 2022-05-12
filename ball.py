from object_scene import ObjectScene


class Ball(ObjectScene):
    def __init__(self, name, canvas, width: int, height: int, position_x, position_y, root):
        super().__init__(name, position_x, position_y)

        self.name = name
        self.canvas = canvas
        self.speed_x = int
        self.speed_y = int
        self.WIDTH = width
        self.HEIGHT = height
        self.root = root

        self.position_x = position_x
        self.position_y = position_y

        self.left_position = None
        self.top_position = None
        self.right_position = None
        self.bottom_position = None
        self.object_name = None

        self.contact_with_player = False

        self.get_speed()
        self.player_position_dic = {}

        self.ball = canvas.create_oval(10, 10, 50, 50, fill="white")

        self.check_collision_border()

    def get_speed(self):
        self.speed_x = 4
        self.speed_y = 4

    def check_collision_border(self):
        self.canvas.move(self.ball, self.speed_x, self.speed_y)
        (self.left_position, self.top_position, self.right_position,
         self.bottom_position) = self.canvas.coords(self.ball)

        self.position_x = self.left_position
        self.position_y = self.top_position

        # Detect if collision
        self.check_collision_with_object(self.name, self.left_position, self.top_position, self.right_position, self.bottom_position)

        self.set_new_position_player_in_list(self.name, self.left_position, self.top_position,
                                             self.right_position, self.bottom_position)

        if self.contact_with_player:
            print("touché")
            print(self.player_position_dic)
            self.move_ball_direction_x()

        elif self.left_position <= 0:
            self.root.destroy()

        elif self.right_position >= self.WIDTH:
            self.move_ball_direction_x()

        elif self.top_position <= 0 or self.bottom_position >= self.HEIGHT:
            print(self.left_position, self.top_position, self.right_position, self.bottom_position)
            self.speed_y = -int(self.speed_y)
            self.position_y = -int(self.speed_y)
            self.set_new_position_player_in_list(self.name, self.left_position, self.top_position,
                                                 self.right_position, self.bottom_position)

        self.canvas.after(30, self.check_collision_border)

    def move_ball_direction_x(self):
        print(self.left_position, self.top_position, self.right_position, self.bottom_position)
        self.speed_x = -int(self.speed_x)
        self.position_x = -int(self.speed_x)
        self.set_new_position_player_in_list(self.name, self.left_position, self.top_position,
                                             self.right_position, self.bottom_position)

    def set_new_position_player_in_list(self, players_name, left_position, top_position, right_position, bottom_position):
        self.player_position_dic[players_name] = (left_position, top_position,
                                                  right_position, bottom_position)

    def check_collision_with_object(self, name, position_a, position_b, position_c, position_d):
        for self.object_name, (a, b, c, d) in self.player_position_dic.items():
            self.contact_with_player = False
            if name != self.object_name:
                if a + c >= position_a and \
                        a <= position_a + position_c and \
                        b + d >= position_b and \
                        b <= position_b + position_d:
                    self.contact_with_player = True
