from graphics import *

win = GraphWin()

p1 = Point(20, 30)
p2 = Point(27, 8)

p1.draw(win)
p2.draw(win)

print("Point 1 is at X=", p1.getX(), "y=", p1.getY())

#Draw some fancy shapes!

center = Point(99, 99)
circle = Circle(center, 30)
circle.setFill('Green')
circle.draw(win)

top_left = Point(12, 12)
bottom_right = Point(36, 36)
rectangle = Rectangle(top_left, bottom_right)
rectangle.setFill('Purple')
rectangle.draw(win)

point_a = Point(75, 5)
point_b = Point(157, 190)
line = Line(point_a, point_b)
line.draw(win)

oval =Oval(Point(93, 102), Point(32, 67))
oval.setFill('Blue')
oval.draw(win)

text = Text(Point(99, 150), "Howdy, folks")
text.draw(win)


input("Press enter to close.")

win.close()
