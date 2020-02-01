from Circle import Circle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, drawing_tool):
        Circle(Point(self.x, self.y), 1).draw(drawing_tool)
