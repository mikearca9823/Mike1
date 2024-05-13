#Simple Pon in Python 3
#By @TokyoEdTech
#Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#stop the window from updating
wn.tracer(0)


#Main game loop
while True:
    wn.update()