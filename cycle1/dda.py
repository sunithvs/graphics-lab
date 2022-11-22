from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Simple DDA program


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 100, 0, 100)


def plotLine(x1, y1, x2, y2):

    deltaX = x2-x1
    deltaY = y2-y1
    steps = 0
    if(abs(deltaX) > abs(deltaY)):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)
    Xincrement = deltaX/steps
    Yincrement = deltaY/steps

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)

    for step in range(1, steps+1):
        glVertex2f(round(x1), round(y1))
        x1 = x1 + Xincrement
        y1 = y1 + Yincrement

    glEnd()
    glFlush()


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("Starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Simple DDA")
    glutDisplayFunc(lambda: plotLine(x1, y1, x2, y2))
    # glutIdleFunc(lambda: plotLine(x1, y1, x2, y2))
    init()
    glutMainLoop()


main()