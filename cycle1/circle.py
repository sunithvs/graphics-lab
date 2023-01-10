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


def get_pixel(x, y):
    pixel = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
    return np.array([round(x, 1) for x in pixel[0][0]])


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def translate_origin(x, y):
    return x + window_size / 2, y + window_size / 2


def circle(xc, yc, radius):
    gluOrtho2D(0, window_size, window_size, 0)
    x = 0
    y = radius
    p = (1 - radius)
    glPointSize(point_size)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(*translate_origin(x + xc, y + yc))
    while x < y:
        if p < 0:
            x = x + 1
            glVertex2f(*translate_origin(x + xc, y + yc))
            p = p + 2 * x + 1
        elif p >= 0:
            x = x + 1
            y = y - 1
            glVertex2f(*translate_origin(x + xc, y + yc))
            p = p + 2 * x + 1 - 2 * y
        symmetry(x, y, xc, yc)
    glEnd()
    glFlush()


def symmetry(x, y, xc, yc):
    glVertex2f(*translate_origin(-x + xc, y + yc))
    glVertex2f(*translate_origin(x + xc, -y + yc))
    glVertex2f(*translate_origin(-x + xc, -y + yc))
    glVertex2f(*translate_origin(y + xc, x + yc))
    glVertex2f(*translate_origin(-y + xc, x + yc))
    glVertex2f(*translate_origin(y + xc, -x + yc))
    glVertex2f(*translate_origin(-y + xc, -x + yc))


def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    if all(color == old_color):
        set_pixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(x, y)
        flood_fill(x, y, [0, 1, .5], get_pixel(x, y))


def main():
    glutInit()
    xc = 0
    yc = 0
    radius = 100
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Bresenham circle with floodfill")
    glutDisplayFunc(lambda: circle(xc, yc, radius))
    glutMouseFunc(mouse_click)
    glutMainLoop()


main()
