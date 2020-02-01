import math
import turtle
from Circle import Circle
from Point import Point
from Rectangle import Rectangle

C1 = Circle(Point(150.0, 100.0), 75)
POINTS_FOR_TEST = [Point(i, j) for i in range(70, 250, 20) for j in range(20, 190, 20)]
RECTANGLES_FOR_TESTS = [Rectangle(Point(i, j), 30, 40) for i in range(0, 250, 50) for j in range(0, 250, 50)]


def is_point_in_circle(circle, point):
    distance = math.sqrt((circle.point.x - point.x)**2 + (circle.point.y - point.y)**2)
    if distance > circle.radius:
        return False
    else:
        return True


def is_rect_in_circle(circle, rectangle):
    for corner in rectangle.show_corners():
        if not is_point_in_circle(circle, corner):
            return False
    return True


def rect_circle_overlap(circle, rectangle):
    for corner in rectangle.show_corners():
        if is_point_in_circle(circle, corner):
            return True
    return False


def relation_between_element_and_circle(drawing_tool, circle, elements, function):
    drawing_tool.penup()
    circle.draw(drawing_tool)
    for element in elements:
        if function(circle, element):
            drawing_tool.color("green")
        else:
            drawing_tool.color("red")
        element.draw(drawing_tool)
    drawing_tool.color("black")


def draw_axis(drawing_tool):
    drawing_tool.penup()
    drawing_tool.goto(-200, 0)
    drawing_tool.pendown()
    drawing_tool.goto(200, 0)
    drawing_tool.penup()
    drawing_tool.goto(0, -200)
    drawing_tool.pendown()
    drawing_tool.goto(0, 200)
    drawing_tool.penup()
    drawing_tool.home()


if __name__ == '__main__':
    input("Window with graphics will be opened for presentation purposes. Please don't close that window. \n"
          "In order to move into the next presentation please come back into the terminal and PRESS ENTER.")
    marker = turtle.Turtle()
    marker.speed(0)
    test_cases = [{'message': "Press enter for presentation of points in the circle:",
                   'function': is_point_in_circle, 'elements': POINTS_FOR_TEST},
                  {'message': "Press enter for presentation of rectangles in the circle:",
                   'function': is_rect_in_circle, 'elements': RECTANGLES_FOR_TESTS},
                  {'message': "Press enter for presentation of overlapping of any corner of rectangle and the circle:",
                   'function': rect_circle_overlap, 'elements': RECTANGLES_FOR_TESTS}]
    for case in test_cases:
        input(case['message'])
        marker.clear()
        draw_axis(marker)
        relation_between_element_and_circle(marker, C1, case['elements'], case['function'])
    input("Press enter to quit")
