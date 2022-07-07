import turtle
import os



def kd(a):
    for i in range(4):
        leo.tilt(1)
        leo.pensize(2)
        leo.color(colors[i%4])
        leo.forward(a)
        leo.left(90)

colors = ["red", "blue", "green", "purple"]

screen = turtle.Screen()
screen.bgcolor("yellow")
leo = turtle.Turtle()
leo.speed(150)

dlina = 40
for i in range(60):
    kd(dlina)
    leo.right(10)
    dlina=dlina+5


def print_hi(name):

    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('GitHub')
