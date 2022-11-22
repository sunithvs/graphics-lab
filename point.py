from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 1500


def line(p1, p2):
    glBegin(GL_LINES)
    glVertex2f(p1[0] / window_size, p1[1] / window_size)
    glVertex2f(p2[0] / window_size, p2[1] / window_size)
    glEnd()


def get_pixel(x, y):
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel


def triangle(p1, p2, p3):
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex2f(p1[0] / window_size, p1[1] / window_size)
    glVertex2f(p2[0] / window_size, p2[1] / window_size)
    glVertex2f(p3[0] / window_size, p3[1] / window_size)
    glEnd()


def set_pixel(x, y, filled_color):
    print(f"{x =} {y =}")
    glColor3f(filled_color[0], filled_color[1], filled_color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(3)
    triangle((0, 0), (0, 800), (800, 0))
    glFlush()


# get the coordinates of the position of the mouse click
def get_coordinates(x, y):
    print(f"{x =} {y =}")
    x = x - window_size / 2
    y = window_size / 2 - y
    print(x, y)
    set_pixel(x / (window_size / 2), y / (window_size / 2), [1.0, 1.0, 0.0])


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        get_coordinates(x, y)


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutMouseFunc(mouse_click)
    glutDisplayFunc(plot)
    glutMainLoop()


if __name__ == '__main__':
    main()
