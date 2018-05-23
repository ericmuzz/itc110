from graphics import *
import time

win = GraphWin("My animation", 300, 300, autoflush = False)

center = Point(40, 100)
circle = Circle(center, 25)
circle.setFill('Green')
circle.draw(win)

for i in range(30):
    circle.move(5, 10)
    update(30)

for i in range(30):
    circle.move(-5, -10)
    update(30)

input("Press enter to close.")

win.close()
