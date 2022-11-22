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
    print(x, y)
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    print(pixel)
    return pixel


def triangle(p1, p2, p3):
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # color pen red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2i(-1, 0)
    glVertex2i(0, 0)
    glVertex2i(0, 1)
    glVertex2i(-1, 1)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2i(0, 0)
    glVertex2i(1, 0)
    glVertex2i(1, 1)
    glVertex2i(0, 1)
    glEnd()
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2i(0, 0)
    glVertex2i(1, 0)
    glVertex2i(1, -1)
    glVertex2i(0, -1)
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
    ls = get_pixel(x, window_size - y)
    found = False
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j][0] != 0:
                print(f"{i =}, {j =}")
                found = True
                break
            if found:
                break


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        get_coordinates(x, y)
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        print("hi")
        k = get_pixel(x, y)
        print(k)


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
