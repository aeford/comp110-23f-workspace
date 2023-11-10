"""TODO: Flower scene."""
__author__ = "730566761"

from turtle import Screen, Turtle, done

screen = Screen()
screen.bgcolor("lightblue")


def main() -> None:
    """The entrypoint of my scene."""
    spider: Turtle = Turtle()
    simple()
    big_mountain(spider, -400, -325, 10)
    big_mountain(spider, -150, -325, 10)
    big_mountain(spider, 100, -325, 10)
    small_mountain(spider, -300, -325, 10)
    small_mountain(spider, 0, -325, 10)
    smallest_mountain(spider, -475, -325, 10)
    smallest_mountain(spider, -250, -325, 10)
    smallest_mountain(spider, -100, -325, 10)
    smallest_mountain(spider, 200, -325, 10)
    sun(spider, 200, 200, 10)
    done()


def cloud(spider: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the clouds."""
    spider.penup()
    spider.goto(x, y)
    spider.pendown()
    spider.color("white")
    spider.fillcolor("white")
    spider.speed(50)
    spider.begin_fill()
    r = 50
    spider.circle(r)
    spider.end_fill()


def big_mountain(spider: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the back mountain."""
    spider.penup()
    spider.goto(x, y)
    spider.pendown()
    spider.color("darkgreen")
    spider.speed(50)
    spider.begin_fill()
    i: int = 0
    while i < 3:
        spider.forward(300)
        spider.left(120)
        i = i + 1
    spider.end_fill()


def small_mountain(spider: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the middle mountain."""
    spider.penup()
    spider.goto(x, y)
    spider.pendown()
    spider.color("green")
    spider.speed(50)
    spider.begin_fill()
    i: int = 0
    while i < 3:
        spider.forward(300)
        spider.left(120)
        i = i + 1
    spider.end_fill()


def smallest_mountain(spider: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the front mountain."""
    spider.penup()
    spider.goto(x, y)
    spider.pendown()
    spider.color("lightgreen")
    spider.speed(50)
    spider.begin_fill()
    i: int = 0
    while i < 3:
        spider.forward(300)
        spider.left(120)
        i = i + 1
    spider.end_fill()


def sun(spider: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the sun."""
    spider.penup()
    spider.goto(x, y)
    spider.pendown()
    spider.color("yellow")
    spider.fillcolor("yellow")
    spider.speed(50)
    spider.begin_fill()
    r = 50
    spider.circle(r)
    spider.end_fill()


def simple() -> None:
    """Simplifying main function."""
    spider: Turtle = Turtle()
    cloud(spider, -80, 80, 10)
    cloud(spider, -100, 100, 60)
    cloud(spider, -40, 120, 10)
    cloud(spider, -60, 140, 10)
    cloud(spider, 10, 60, 10)
    cloud(spider, 20, 90, 10)
    cloud(spider, -70, 70, 10)
    cloud(spider, -65, 70, 10)
    cloud(spider, 0, 120, 10)
    cloud(spider, 30, 90, 10)
    cloud(spider, 200, 120, 10)
    cloud(spider, 250, 120, 10)
    cloud(spider, 300, 120, 10)
    cloud(spider, 225, 150, 10)
    cloud(spider, 275, 150, 10)
    cloud(spider, 325, 150, 10)
    cloud(spider, 325, 120, 10)
    cloud(spider, 280, 170, 10)
    cloud(spider, -350, 150, 10)
    cloud(spider, -375, 150, 10)
    cloud(spider, -300, 150, 10)
    cloud(spider, -325, 170, 10)
    cloud(spider, -375, 170, 10)


main()