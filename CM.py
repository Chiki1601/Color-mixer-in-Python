#!python
'''A Color Mixer Program'''

from turtle import *


class ColorTurtle(Turtle):
    """ our turtle class that we will use to generate our 
    color turtles"""

    def __init__(self, x, y):
        """Initalizing our Turtles with their various properties"""
        Turtle.__init__(self)
        self.shape('turtle')
        self.resizemode('user')
        self.shapesize(3, 3, 5)
        self.pensize(9)
        self._color = [0, 0, 0]
        self.x = x
        self._color[x] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.penup()
        self.setposition(x, 0)
        self.pendown()
        self.sety(1)
        self.penup()
        self.sety(y)
        self.pencolor('gray25')
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0, min(y, 1)))
        self._color[self.x] = self.ycor()
        self.fillcolor(self._color)
        setbackground()


def setbackground():
    """Sets the screen background using the value of the
    y-cordinate of our turtles on screen """
    screen.bgcolor(red.ycor(), green.ycor(),   blue.ycor())


def main():
    global screen, red, green, blue
    screen = Screen()
    screen.title("My Color Plate")
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)
    screen.setup(width=.65, height=.80, startx=None, starty=50)

    red = ColorTurtle(0, .5)
    green = ColorTurtle(1, .5)
    blue = ColorTurtle(2, .5)
    setbackground()

    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.setposition(1, 1.15)
    writer.write('DRAW!', align="center", font=("Arial", 30, ("bold", "italic")))
    return "EVENTLOOP"


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
