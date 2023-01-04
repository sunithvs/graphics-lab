# sunith vs
# CS B
#  Line clipping

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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


def plot_line(p1, p2, color=(1, 1, 0)):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(*p1)
    glVertex2f(*p2)
    glEnd()
    glFlush()


def plot_clipping_window():
    glColor3f(.2, .2, 0)
    glBegin(GL_POLYGON)
    glVertex2f(border, border)
    glVertex2f(border, window_size - border)
    glVertex2f(window_size - border, window_size - border)
    glVertex2f(window_size - border, border)
    glEnd()


def get_clipped_point(point, m):
    """
    1001 | 1000 | 1010
  .....................
    0001 | 0000 | 0010
  .....................
    0101 | 0100 | 0110

    :param point: list[float]
    :param m: int
    :return: list[float]
    """
    code = point_code(*point)
    print(point, code)

    if code[-1] == 1:
        """left portion"""
        if code[0] == 1:
            point[1] = window_size - border
        elif code[1] == 1:
            point[1] = border
        else:
            point[1] = point[1] + m * (border - point[0])
        point[0] = border
    elif code[-2] == 1:
        """right portion"""
        if code[0] == 1:
            point[1] = window_size - border
        elif code[1] == 1:
            point[1] = border
        else:
            point[1] = point[1] + m * (window_size - border - point[0])
        point[0] = window_size - border
    elif code[0] == 1:
        """top portion"""
        if code[-1] == 1:
            point[0] = border
        elif code[-2] == 1:
            point[0] = window_size - border
        else:
            point[0] = point[0] + (window_size - border - point[1]) / m
        point[1] = window_size - border
    elif code[1] == 1:
        """bottom portion"""
        if code[-1] == 1:
            point[0] = border
        elif code[-2] == 1:
            point[0] = window_size - border
        else:
            point[0] = point[0] + (border - point[1]) / m
        point[1] = border


def slop(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def get_clipped_points(p1, p2):
    visibility, _ = check_line_visibility(p1, p2)
    if visibility == 3:
        m = slop(p1, p2)
        print("m before", m)
        get_clipped_point(p1, m)
        get_clipped_point(p2, m)
        print("m after", slop(p1, p2))
    print(p1, p2)
    return p1, p2


def plot_clipped_line(p1, p2):
    plot_line(*get_clipped_points(p1, p2))


def display():
    gluOrtho2D(0, window_size, 0, window_size)
    glClear(GL_COLOR_BUFFER_BIT)
    plot_clipping_window()
    p1 = [window_size / 2, window_size - 50]
    p2 = [window_size - 50, window_size / 2]
    print("point to be plotted", p1, p2)
    plot_line(p1, p2, [0, 1, 1])
    plot_clipped_line(p1, p2)
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("transformations")
    glutDisplayFunc(display)
    glutMainLoop()


main()
