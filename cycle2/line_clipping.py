from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

window_size = 800
border = 100
point_size = 5


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


def point_code(x, y):
    return [1 if y > window_size - border else 0, 1 if y < border else 0, 1 if x > window_size - border else 0,
            1 if x < border else 0]


def perform_and(p1, p2):
    return [c1 and c2 for c1, c2 in zip(point_code(*p1), point_code(*p2))]


def perform_or(p1, p2):
    return [c1 or c2 for c1, c2 in zip(point_code(*p1), point_code(*p2))]


def check_line_visibility(p1, p2):
    if perform_or(p1, p2) == [0, 0, 0, 0]:
        return 1, "visible"
    elif perform_and(p1, p2) != [0, 0, 0, 0]:
        print(perform_and(p1, p2))
        return 2, "invisible"
    else:
        return 3, "clipped"


def plot_line(p1, p2):
    glColor3f(1, 1, 0)
    glBegin(GL_LINES)
    glVertex2f(*p1)
    glVertex2f(*p2)
    glEnd()
    glFlush()


def plot_clipping_window():
    glColor3f(.2, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(border, border)
    glVertex2f(border, window_size - border)
    glVertex2f(window_size - border, window_size - border)
    glVertex2f(window_size - border, border)
    glEnd()


def get_clipped_point(point, m):
    code = point_code(*point)
    if code[-1] == 1:
        point[0] = border
        point[1] = point[1] + m * (point[0])
    elif code[-2] == 1:
        point[0] = window_size - border
    if code[1] == 1:
        point[1] = window_size - border
        point[0] = point[0] + (point[1] - window_size - border) / m
    elif code[2] == 1:
        point[1] = border
        point[0] = point[0] + (point[1] - window_size - border) / m
    return point


def get_clipped_points(p1, p2):
    visibility, _ = check_line_visibility(p1, p2)
    if visibility == 3:
        m = (p2[1] - p1[1]) / p2[0] - p1[0]

        p1 = get_clipped_point(p1, m)
        p2 = get_clipped_point(p2, m)
    print(p1,p2)
    return p1, p2


def plot_clipped_line(p1, p2):
    plot_line(*get_clipped_points(p1, p2))


def display():
    gluOrtho2D(0, window_size, 0, window_size)
    glClear(GL_COLOR_BUFFER_BIT)
    plot_clipping_window()
    p1 = [window_size/2, window_size/2]
    p2 = [border/2, window_size/2]
    plot_clipped_line(p1, p2)
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("transformations")
    glutDisplayFunc(display)
    glutMainLoop()


main()
