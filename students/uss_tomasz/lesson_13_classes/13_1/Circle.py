class Circle:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

    def draw(self, drawing_tool):
        drawing_tool.penup()
        drawing_tool.goto(self.point.x, self.point.y - self.radius)
        drawing_tool.pendown()
        drawing_tool.circle(self.radius)
        drawing_tool.penup()
        drawing_tool.home()
