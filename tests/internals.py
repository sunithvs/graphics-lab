from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy

window_size = 1000
point_size = 5


def clear():
    gluOrtho2D(0, window_size, window_size, 0)
    glClear(GL_COLOR_BUFFER_BIT)


def read_pixel(x, y):
    color = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
    return numpy.array(color[0][0])


def plot_point(x, y, color=(0, 1, 1)):
    glColor3f(*color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def plot_symmetry(x, y, xc, yc):
    plot_point(x + xc, y + yc)
    plot_point(y + xc, x + yc)
    plot_point(-x + xc, y + yc)
    plot_point(-y + xc, x + yc)
    plot_point(-x + xc, -y + yc)
    plot_point(-y + xc, -x + yc)
    plot_point(x + xc, -y + yc)
    plot_point(y + xc, -x + yc)


def circle(xc, yc, radius):
    x = 0
    y = radius
    p = (1 - radius)
    glPointSize(point_size)
    glColor3f(1.0, 1.0, 0.0)
    plot_point(x + xc, y + yc)
    while x < y:
        if p < 0:
            x = x + 1
            plot_point(x + xc, y + yc)
            p = p + 2 * x + 1
        elif p >= 0:
            x = x + 1
            y = y - 1
            plot_point(x + xc, y + yc)
            p = p + 2 * x + 1 - 2 * y
        plot_symmetry(x, y, xc, yc)


def display():
    clear()
    circle(window_size / 2, window_size / 2, window_size / 3)

    glFlush()


def boundary_fill(x, y, new_color, boundary_color):
    color = read_pixel(x, y)
    plot_point(x, y)
    glFlush()

    if not (all(color == new_color)) and not all(color == boundary_color):

        plot_point(x, y, new_color)
        boundary_fill(x + point_size, y, new_color, boundary_color)
        boundary_fill(x, y + point_size, new_color, boundary_color)
        boundary_fill(x - point_size, y, new_color, boundary_color)

        boundary_fill(x, y - point_size, new_color, boundary_color)


def mouse(button, state, x, y):
    if state == GLUT_DOWN:
        print(x, y)
        boundary_fill(x, y, [1, .5, 0], [0, 1.0, 1.0])


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()


main()
