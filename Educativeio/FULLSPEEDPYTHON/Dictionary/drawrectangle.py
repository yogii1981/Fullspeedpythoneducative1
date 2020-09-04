dimensions = {}
dimensions["width"] = 20
dimensions["height"] = 40

import turtle


def drawRectangle(turtle, **dimensions):
    width = 10
    height = 10
    if "width" in dimensions:
        width = dimensions["width"]
    if "height" in dimensions:
        height = dimensions["height"]
    drawFigure(turtle, width, 90, height, 90, width, 90, height, 90)


def drawFigure(turtle, *args):
    for i in range(0, len(args), 2):
        turtle.forward(args[i])
        turtle.left(args[i + 1])


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    drawRectangle(t, width=40, height=20)
    screen.exitonclick()


if __name__ == "__main__":
    main()
