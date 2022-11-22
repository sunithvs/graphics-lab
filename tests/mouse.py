from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 1500


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 100, 0, 100)


def get_pixel(x, y):
    x = x - window_size / 2
    y = window_size / 2 - y
    pixel = glReadPixels(x / (window_size / 2), y / (window_size / 2), 1, 1, GL_RGB, GL_FLOAT)
    return pixel


def set_pixel(x, y, filled_color):
    glColor3f(filled_color[0], filled_color[1], filled_color[2])
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def plot_coordinates(x, y):
    print(f"{x =} {y =}")
    x = x - window_size / 2
    y = window_size / 2 - y
    print(x, y)
    set_pixel(x / (window_size / 2), y / (window_size / 2), [1.0, 1.0, 0.0])


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        plot_coordinates(x, y)
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        print("hi")
        k = get_pixel(x, y)
        print(k)


def main():
    glutInit(sys.argv)
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()
