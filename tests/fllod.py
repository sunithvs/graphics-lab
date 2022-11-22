# boundary filling algorithm  using only opengl

import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 1500
sys.setrecursionlimit(10000000)

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, window_size, 0.0, window_size)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def setPixel(x, y, filled_color):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def getPixel(x, y):
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel


def boundaryFill(x, y, fill_color, boundary_color):
    color = getPixel(x, y)
    print(color,boundary_color)
    if color != boundary_color and color != fill_color:
        setPixel(x, y, fill_color)
        boundaryFill(x + 1, y, fill_color, boundary_color)
        boundaryFill(x - 1, y, fill_color, boundary_color)
        boundaryFill(x, y + 1, fill_color, boundary_color)
        boundaryFill(x, y - 1, fill_color, boundary_color)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    # draw a polygon
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 100)
    glVertex2f(100, 400)
    glVertex2f(400, 400)
    glVertex2f(400, 100)
    glEnd()

    boundaryFill(150, 150, [1.0, 0.0, 0.0], [1.0, 1.0, 1.0])

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_size, window_size)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Boundary Fill Algorithm")
    glutDisplayFunc(display)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
