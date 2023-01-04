import math
import time

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

# Global variables
angle = 0.0


# Set up the projection matrix
def setup_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.0, 0.1, 100.0)


# Set up the modelview matrix
def setup_modelview():
    global angle

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # Rotate the pendulum around the y-axis
    glRotatef(angle, 0.0, 1.0, 0.0)


# Draw the pendulum
def draw_pendulum():
    # Set the color to red
    glColor3f(1.0, 0.0, 0.0)

    # Draw the pivot point
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    # Draw the rod
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    gluCylinder(gluNewQuadric(), 0.1, 0.1, 1.0, 20, 20)
    glPopMatrix()

    # Draw the bob
    glPushMatrix()
    glTranslatef(0.0, 0.0, 1.0)
    glutSolidSphere(0.2, 20, 20)
    glPopMatrix()


# Update the modelview matrix
def update():
    global angle

    # Increment the angle of the pendulum
    # based on the elapsed time
    elapsed_time = time.time() - start_time
    angle = math.sin(elapsed_time) * 90.0


# Display callback
def display():
    # Clear the buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set up the projection matrix
    setup_projection()

    # Set up the modelview matrix
    setup_modelview()

    # Draw the pendulum
    draw_pendulum()

    # Swap the buffers
    glutSwapBuffers()


# Timer callback
def timer(value):
    # Update the modelview matrix
    update()

    # Redisplay the scene
    glutPostRedisplay()

    # Call the timer again after a certain interval
    glutTimerFunc(16, timer, 0)


def main():
    glutInit(sys.argv)

    glutInitWindowSize(1000, 1000)
    glutCreateWindow("pendulum")
    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == '__main__':
    main()
