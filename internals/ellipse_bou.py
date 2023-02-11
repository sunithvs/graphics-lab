from OpenGL.GL import *
# from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np

windowsize = 700
point = 10
scale = 100
xc = yc = 0
r = 10


def set_pixel(x, y, color=(1, 0, 1)):
    glColor3f(*color)
    glPointSize(point)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def get_pixel(x, y):
    pixel = glReadPixels(x, windowsize - y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel[0][0]


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # gluOrtho2D(0, windowsize, windowsize, 0)
    xc = windowsize / 2
    yc = windowsize / 2
    a = 150
    b = 80
    ellipse(xc, yc, a, b)
    glFlush()


def ellipse(xc, yc, a, b):
    theta = 2 * math.pi
    while theta >= 0:
        x = a * math.cos(theta)
        y = a * math.sin(theta)
        set_pixel(x + xc, y + yc)
        theta -= 0.01


def floodfill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    print(color, old_color)
    if list(color) == list(old_color):
        set_pixel(x, y, new_color)
        floodfill(x + point, y, new_color, old_color)
        floodfill(x, y + point, new_color, old_color)
        floodfill(x - point, y, new_color, old_color)
        floodfill(x, y - point, new_color, old_color)


def mouse_pointer(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        floodfill(x, y, (1, 0, 0), (0, 0, 0))


def main():
    glutInit()
    glutInitWindowSize(windowsize, windowsize)
    glutCreateWindow("ellipse")
    glutDisplayFunc(display)
    glutMouseFunc(mouse_pointer)
    glutMainLoop()


main()
