import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

# for setting window size
window_size = 800
point_size = 2
sys.setrecursionlimit(1000000)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # gluOrtho2D(0,window_size,window_size,0)


def set_pixel(x, y):
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def ellipse(xc, yc, a, b):
    theta = 2 * math.pi
    while theta >= 0:
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        set_pixel(x + xc, y + yc)
        theta -= 0.02



def display():
    glClear(GL_COLOR_BUFFER_BIT)
    xc = -.3
    yc = .3
    a = .5
    b = .3
    ellipse(xc, yc, a, b)
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Ellipse drawing algorithm")
    glutDisplayFunc(display)
    glutMainLoop()


main()
