from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# for setting window size
window_size = 800
point_size = 10
sys.setrecursionlimit(100000)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)


#
def get_pixel(x, y):
    pixel = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
    # here the  pixel will be of format
    # [
    #     [
    #       [red,green,blue]
    #     ]
    # ]
    # for that we use indexing to get list of rgb
    return pixel[0][0]


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def rectangle(vertices, color):
    """
    :param vn pixel[0][0]ertices : it is list  of 4 vertex
        eg [
            [x1,y1],
            [x2,y2],
            [x3,y3],
            [x4,y4],
          ]
    :param color: [red,green,blue]
    :return: onnumilla
    """
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()


def plot_rect():
    glClear(GL_COLOR_BUFFER_BIT)
    # for shifting coordinate from ordinary to first quadrant with x and y maximum is window size
    gluOrtho2D(0, window_size, window_size, 0)
    # top left rectangle
    rectangle(
        [[0, 0], [0, window_size / 2], [window_size / 2, window_size / 2], [window_size / 2, 0]],
        [1, 0, 0]
    )
    rectangle(
        [[window_size / 2, 0], [window_size / 2, window_size / 2], [window_size, window_size / 2],
         [window_size, 0]],
        [1, 0, 1]
    )
    rectangle(
        [[0, window_size / 2], [0, window_size], [window_size / 2, window_size],
         [window_size / 2, window_size / 2]],
        [0, 0, 1]
    )
    rectangle(
        [[window_size / 2, window_size / 2], [window_size / 2, window_size], [window_size, window_size],
         [window_size, window_size / 2]],
        [0, 1, 1]
    )
    glFlush()


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
        flood_fill(x, y, [0, 1, .5], get_pixel(x, y))


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(plot_rect)
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()
