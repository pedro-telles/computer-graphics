from Texture import Texture
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Sphere import Sphere, rotate, set_angle, angle
import numpy

textures_files = {
    'earth': 'computer-graphics\\OpenGL\\Textura\\terra.png',
}

tx = Texture(textures_files, 'Terra', 1000, 800)
earth = Sphere(0,0,0,5, tx = tx, density = 80)

ESCAPE = b'\033'

x_rotation = y_rotation = z_rotation = 0.0
direction = (0.1, 0, 0)

stars = []
total_stars = 1000
starts_range = 100

def draw_stars():
    
    glPushMatrix()

    glTranslatef(0,0,-30)

    glBegin(GL_POINTS)
    for i in range(total_stars):
        x = stars[0][i]*starts_range
        y = stars[1][i]*starts_range
        glVertex3fv((x, y, 0))
        glVertex3fv((-y, -x, 0))
        glVertex3fv((-x, y, 0))
        glVertex3fv((y, -x, 0))
    glEnd()
    
    glPopMatrix()

def load_random_stars():

    x  = list(numpy.random.rand(1, total_stars)[0])
    y  = list(numpy.random.rand(1, total_stars)[0])
    stars.append(x)
    stars.append(y)


def DrawGLScene():
    global x_rotation, y_rotation, z_rotation, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  

    glTranslatef(0.0,0.0,-60.0)
    
    glRotatef(x_rotation,1.0,0.0,0.0)          
    glRotatef(y_rotation,0.0,1.0,0.0)           
    glRotatef(z_rotation,0.0,0.0,1.0) 
    draw_stars()

    earth.draw(rotation = (angle['earth']['translation'],1,1,1), texture_index = 'earth')
    rotate('earth')

    x_rotation = x_rotation + 0.01                 # X rotation
    y_rotation = y_rotation + 0.01                 # Y rotation
    z_rotation = z_rotation + 0.01                 # Z rotation

    glutSwapBuffers()

if __name__ == '__main__':
    
    set_angle('earth', rotation = (0,0.02), translation = (0,1))
    load_random_stars()
    tx.main(DrawGLScene)