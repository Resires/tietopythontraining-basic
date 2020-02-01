import copy


class Rectangle:
    def __init__(self, point, width, height):
        self.point = point
        self.width = width
        self.height = height

    def draw(self, drawing_tool):
        drawing_tool.penup()
        points = self.show_corners()
        drawing_tool.goto(points[-1].x, points[-1].y)
        drawing_tool.pendown()
        for point in points:
            drawing_tool.goto(point.x, point.y)
        drawing_tool.penup()
        drawing_tool.home()

    def show_corners(self):
        a = self.point
        b = copy.deepcopy(a)
        c = copy.deepcopy(a)
        d = copy.deepcopy(a)
        b.x += self.width
        c.x += self.width
        c.y += self.height
        d.y += self.height
        return [a, b, c, d]
