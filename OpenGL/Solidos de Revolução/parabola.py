from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

density = 15
rotation_speed = 2

def setColor(j): 
    
    if j < density//2: 
        r = (j - 255) / (density/2 - 1)
        g = (j) / (density/2 - 1)
        b = (j) / (density/2 - 1)
    else:
        r = ((density - j - 255) / (density/2 - 1)) - 0.08
        g = ((density - j) / (density/2 - 1)) - 0.08
        b = ((density - j) / (density/2 - 1)) - 0.08
    
    glColor3f(r, g, b)

def func_2_degree (u, v):
    theta = (v * 2 * pi) / (density - 1)
    w = (u * 2 / (density - 1))

    x = w * cos(theta)
    y = w ** 2
    z = w * sin(theta)

    return x, y, z

def func_3_degree (u, v):
    theta = (v * 2 * pi) / (density - 1)
    w = ((u * 4) / (density - 1)) - 2

    x = w * cos(theta)
    y = w ** 3
    z = w * sin(theta)

    return x, y, z

def draw_2_degree_points ():
    glTranslatef(6,-1,0)
    glRotatef(angle,0,1,0)
    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)
    for i in range(density):
        for j in range(density):
            x, y, z = func_2_degree(i,j)
            glVertex3f(x, -y, z)
    glEnd()

def draw_2_degree_filled ():
    glTranslatef(-6,1,0)
    glRotatef(angle,0,1,0)

    for i in range(density):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            setColor(j)
            glVertex3fv(func_2_degree(i,j))
            glVertex3fv(func_2_degree(i - 1,j))
        glEnd()

def draw_3_degree_filled ():
    glTranslatef(0,0,0)
    glRotatef(angle,0,1,0)

    for i in range(1,density):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            setColor(j)
            glVertex3fv(func_3_degree(i,j))
            glVertex3fv(func_3_degree(i - 1,j))
        glEnd()

angle = 0

def draw():
    global angle
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    draw_2_degree_filled()    
    glPopMatrix()
   
    glPushMatrix()
    draw_3_degree_filled()    
    glPopMatrix()
    
    glPushMatrix()
    draw_2_degree_points()    
    glPopMatrix()
    
    glutSwapBuffers()
    
    angle += rotation_speed
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# MAIN
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("2/3 Degrees Functions")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-25)
glutTimerFunc(50,timer,1)
glutMainLoop()
