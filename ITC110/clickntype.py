from graphics import *

#Create window object

win=GraphWin()

for i n range(50):
    point = win.getMouse()
    key = win.getKey()
    label = Text(point, key)
    label.draw(win)

    
