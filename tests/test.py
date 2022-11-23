import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 1000

x_increment = .4
y_increment = .4


def plot_point():
    global x_increment
    global y_increment
    x_increment = int(input("x inc"))/window_size
    y_increment = int(input("y inc"))/window_size
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10)
    glColor(1, .5, 0)
    glBegin(GL_POLYGON)
    glVertex2f(.3 + x_increment, 0 + y_increment)
    glVertex2f(.3 + x_increment, .3 + y_increment)
    glVertex2f(0 + x_increment, .3 + y_increment)
    glVertex2f(0 + x_increment, 0 + y_increment)
    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("testing")
    glutIdleFunc(plot_point)
    glutMainLoop()


main()
