# sunith vs
# CS B
# 2022098

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

window_size = 800
point_size = 5
sys.setrecursionlimit(100000)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)


def get_pixel(x, y):
    pixel = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel[0][0]


def set_pixel(x, y, filled_color):
    glColor3f(filled_color[0], filled_color[1], filled_color[2])
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, window_size - y)
    glEnd()
    glFlush()


def plot_rect():
    gluOrtho2D(0, window_size, 0, window_size)
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 0)
    glVertex2f(window_size / 2, 0)
    glVertex2f(window_size / 2, window_size / 2)
    glVertex2f(0, window_size / 2)
    glEnd()
    glColor3f(0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(window_size / 2, 0)
    glVertex2f(window_size, 0)
    glVertex2f(window_size, window_size / 2)
    glVertex2f(window_size / 2, window_size / 2)
    glEnd()
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2f(window_size, window_size / 2)
    glVertex2f(window_size, window_size)
    glVertex2f(window_size / 2, window_size)

    glVertex2f(window_size / 2, window_size / 2)
    glEnd()
    glFlush()


def plot_coordinates(x, y):
    set_pixel(x, y, [1.0, 1.0, 1.0])


def list_equal(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    print(color, new_color, old_color)
    if (not list_equal(color, new_color)) and list_equal(color, old_color):
        set_pixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        plot_coordinates(x, y)
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        print("hi")
        old_color = get_pixel(x, y)
        flood_fill(x, y, [1, 1, 0], old_color)


def main():
    glutInit(sys.argv)

    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(plot_rect)
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()
