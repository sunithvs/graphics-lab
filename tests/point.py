from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL import images

window_size = 1500


# Change coordinate system of window


def line(p1, p2):
    glBegin(GL_LINES)
    glVertex2f(p1[0] / window_size, p1[1] / window_size)
    glVertex2f(p2[0] / window_size, p2[1] / window_size)
    glEnd()


def get_pixel(x, y):
    color = [0, 0, 0]
    pixel = glReadPixels(x, y, 3, 3, GL_RGB, GL_FLOAT)
    return images.returnFormat(pixel, GL_FLOAT)


def triangle(p1, p2, p3):
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # color pen red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(p1[0], p1[1])
    glVertex2i(p2[0], p2[1])
    glVertex2i(p3[0], p3[1])
    glEnd()


def set_pixel(x, y, filled_color):
    print(f"{x =} {y =}")
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(filled_color[0], filled_color[1], filled_color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(3)
    triangle((0, 0), (200, 300), (0, 500))
    glFlush()


# get the coordinates of the position of the mouse click
def get_coordinates(x, y):
    print(f"{x =} {y =}")
    x = x - window_size / 2
    y = window_size / 2 - y
    print(x, y)
    ls = get_pixel(x, y)
    for i in ls:
        for j in i:
            print(j, end=" ")
        print()


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        get_coordinates(x, y)


def main():
    glutInit()
    glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutMouseFunc(mouse_click)
    glutDisplayFunc(plot)
    glutMainLoop()


if __name__ == '__main__':
    main()
