#This is assignment 4, Draw a meh face
from graphics import *
import random

win = GraphWin()

text = Text(Point(99, 10), "meh")
text.draw(win)

center = Point(99, 99)
circle = Circle(center, 60)
circle.setFill('Green')
circle.draw(win)

point_a = Point(65, 125)
point_b = Point(135, 125)
mouth = Line(point_a, point_b)
mouth.draw(win)

point_a = Point(60, 70)
point_b = Point(80, 70)
leftBrow = Line(point_a, point_b)
leftBrow.draw(win)

point_a = Point(130, 70)
point_b = Point(150, 70)
rightBrow = Line(point_a, point_b)
rightBrow.draw(win)

point_a = Point(99, 40)
point_b = Point(99, 30)
hair1 = Line(point_a, point_b)
hair1.draw(win)

point_a = Point(95, 40)
point_b = Point(95, 30)
hair2 = Line(point_a, point_b)
hair2.draw(win)

point_a = Point(90, 40)
point_b = Point(90, 30)
hair3 = Line(point_a, point_b)
hair3.draw(win)

point_a = Point(105, 40)
point_b = Point(105, 30)
hair4 = Line(point_a, point_b)
hair4.draw(win)

center = Point(65, 90)
leftEye = Circle(center, 15)
leftEye.setFill('Black')
leftEye.draw(win)

center = Point(135, 90)
rightEye = Circle(center, 15)
rightEye.setFill('Black')
rightEye.draw(win)

input("Press enter to close.")

win.close()
