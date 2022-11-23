from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

sys.setrecursionlimit(1000000)
window_size = 1500


def clear_screen():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, window_size, window_size, 0)


def set_pixel(x, y, filled_color):
    glColor3f(filled_color[0], filled_color[1], filled_color[2])
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def get_pixel(x, y):
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel[0][0]


def flood_fill(x, y, old_color, new_color):
    if all([get_pixel(x, y)[i] == old_color[i] for i in range(len(new_color))]):
        set_pixel(x, window_size - y, new_color)
        flood_fill(x + 5, y, old_color, new_color)
        flood_fill(x, y + 5, old_color, new_color)
        flood_fill(x - 5, y, old_color, new_color)
        flood_fill(x, y - 5, old_color, new_color)
    glFlush()


def plot_rectangle():
    clear_screen()
    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 0)
    glVertex2f(500, 0)
    glVertex2f(500, 500)
    glVertex2f(0, 500)
    glEnd()
    glFlush()


def check_mouse_event(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, window_size - y, [1, 1, 0], [0, 1, 1])
        glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("flood fill")
    glutDisplayFunc(plot_rectangle)
    glutMouseFunc(check_mouse_event)
    glutMainLoop()


if __name__ == '__main__':
    main()
