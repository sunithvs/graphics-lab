from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

window_size = 800
point_size = 2


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def clear_screen():
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-window_size, window_size, window_size, -window_size)
    glClear(GL_COLOR_BUFFER_BIT)


def ball():
    glPointSize(point_size)
    glColor3f(1, 0, 0, )
    glBegin(GL_POINTS)
    for i in range(0, 360, 5):
        glVertex2f(100 * cos(i), 100 * sin(i))
    glEnd()


def display():
    # ball(
    pass


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("ellipse")
    glutDisplayFunc(display)
    # glutMouseFunc(mouse_pointer)
    glutMainLoop()


main()