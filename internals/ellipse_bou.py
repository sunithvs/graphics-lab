import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

# for setting window size
window_size = 700
point_size = 8
sys.setrecursionlimit(1000000)


def set_pixel(x, y, color=(1, 1, 1)):
    glColor3f(*color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def get_pixel(x, y):
    pixel = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel[0][0]


def ellipse(xc, yc, a, b):
    theta = 2 * math.pi
    while theta >= 0:
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        set_pixel(x + xc, y + yc)
        # print(x, y)
        theta -= 0.01


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    gluOrtho2D(0, window_size, window_size, 0)
    xc = window_size / 2
    yc = window_size / 2
    a = 150
    b = 80
    ellipse(xc, yc, a, b)
    glFlush()


def boundary_fill(x, y, new_color, boundary_color):
    color = get_pixel(x, y)
    if list(color) != list(new_color) and list(color) != list(boundary_color):
        set_pixel(x, y, new_color)
        boundary_fill(x + point_size, y, new_color, boundary_color)
        boundary_fill(x - point_size, y, new_color, boundary_color)
        boundary_fill(x, y + point_size, new_color, boundary_color)
        boundary_fill(x, y - point_size, new_color, boundary_color)


def mouse_handler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        boundary_fill(x, y, (1, 1, 0), (1, 1, 1))


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Ellipse drawing algorithm")
    glutDisplayFunc(display)
    glutMouseFunc(mouse_handler)
    glutMainLoop()


main()
