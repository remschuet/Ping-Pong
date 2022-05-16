class Point:
    def __init__(self, canvas, name_id: str, position_x: int, position_y: int, points: int):
        self.canvas = canvas
        self.name_id = name_id
        self.position_x = position_x
        self.position_y = position_y

        self.point = points

        self.graphic_point = self.canvas.create_text(self.position_x, self.position_y, text=self.point, font="Times 15 italic bold", fill="red")

    def add_points(self):
        self.point = self.point + 1
        print(self.point)
        self.update_points()

    def update_points(self):
        self.canvas.itemconfig(self.graphic_point, text=self.point)
