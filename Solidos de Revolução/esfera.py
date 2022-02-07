from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

density = 50
rotation_speed = 2
radius = 2
half_pi = pi/2

def setColor(i, j): 
    
    if i < density//2: 
        r = (i) / (density/2 - 1)
        g = (i) / (density/2 - 1)
        b = (i) / (density/2 - 1)
    else:
        r = ((density - i) / (density/2 - 1)) - 0.08
        g = ((density - i) / (density/2 - 1)) - 0.08
        b = ((density - i) / (density/2 - 1)) - 0.08
    
    glColor3f(r, g, b)

def sphere(u, v):
    theta = (u * pi / (density - 1)) - half_pi
    phi = (v * 2 * pi) / (density - 1)

    x = radius * cos(theta) * cos(phi)
    y = radius * sin(theta)
    z = radius * cos(theta) * sin(phi)
    
    return x, y, z

def draw_sphere_points():
    glTranslatef(2.5,0,0)
    glRotatef(angle,1,1,1)
    glBegin(GL_POINTS)

    glColor3f(1, 1, 1)

    for i in range(density):
        for j in range(density):
            glVertex3fv(sphere(i,j))
    glEnd()

def draw_filled_sphere():
    glTranslatef(-2.5,0,0)
    glRotatef(angle,1,1,1)
    
    for i in range(density):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            setColor(i, j)
            glVertex3fv(sphere(i,j))
            glVertex3fv(sphere(i - 1,j))
        glEnd()

angle = 0

def draw():
    global angle
  
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    draw_filled_sphere()    
    glPopMatrix()
    
    glPushMatrix()
    draw_sphere_points()    
    glPopMatrix()
    
    glutSwapBuffers()
    
    angle += rotation_speed
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Sphere")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(50,timer,1)
glutMainLoop()


