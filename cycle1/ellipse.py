import math
from random import random

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


def ellipse(x, y, a, b):
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f(x + a * math.cos(math.radians(i)), y + b * math.sin(math.radians(i)))
    glEnd()
    glFlush()


def display():
    # gluOrtho2D(0, window_size, window_size, 0)
    # glClear(GL_COLOR_BUFFER_BIT)
    ellipse(random(), random(), random() * 0.01, random() * 0.01)
    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Ellipse drawing algorithm")
    glutDisplayFunc(display)
    glutMainLoop()


main()
