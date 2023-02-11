import math
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def get_pixel(x, y):
    return glReadPixels(x, 500 - y, 1, 1, GL_RGB, GL_FLOAT)


def draw_ellipse(x, y, a, b):
    glBegin(GL_POINTS)
    for i in range(360):
        glVertex2f(x + a * math.cos(math.radians(i)), y + b * math.sin(math.radians(i)))
    glEnd()
    glFlush()


def draw():

    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(2)
    glColor3f(1, 1, 1)
    draw_ellipse(0.5, 0.5, 50, 30)
    gluOrtho2D(0, 500, 500, 0)
    # glutPostRedisplay()


def main():
    glutInit()
    glutInitWindowSize(500, 500)

    glutCreateWindow("Bresenham circle with floodfill")
    glutDisplayFunc(draw)

    glutMainLoop()


if __name__ == '__main__':
    main()
