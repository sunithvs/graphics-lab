# sunith vs
# CS B
# 2022098


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

window_size = 800
point_size = 5
sys.setrecursionlimit(1000000)


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
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    gluOrtho2D(0, window_size, 0, window_size)
    glColor3f(1, 0, 0)
    glLineWidth(point_size)
    glBegin(GL_POLYGON)
    glVertex2f(10, 10)
    glVertex2f(window_size / 2, 10)
    glVertex2f(window_size / 2, window_size / 2)
    glVertex2f(10, window_size / 2)
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


def boundary_fill(x, y, fill_color, boundary_color):
    color = get_pixel(x, y)
    print(color, fill_color, boundary_color)
    if (not list_equal(color, fill_color)) and not list_equal(color, boundary_color):
        print("setting px ")
        set_pixel(x, y, fill_color)
        boundary_fill(x + point_size, y, fill_color, boundary_color)
        boundary_fill(x, y + point_size, fill_color, boundary_color)
        boundary_fill(x - point_size, y, fill_color, boundary_color)
        boundary_fill(x, y - point_size, fill_color, boundary_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        plot_coordinates(x, y)
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        print("hi")
        old_color = [1, 0, 0]
        boundary_fill(x, y, [1, 1, 0], old_color)


def main():
    glutInit(sys.argv)

    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(plot_rect)
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()
