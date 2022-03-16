from Texture import Texture
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

textures_files = {
    'dice': 'dado.png',
}

tx = Texture(textures_files, 'Dado', 1000, 800)

ESCAPE = b'\033'

x_rotation = y_rotation = z_rotation = 0.0
direction = (0.1, 0, 0)

def DrawGLScene():
    global x_rotation, y_rotation, z_rotation, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.5,0.5,0.5,1.0)            
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(x_rotation,1.0,0.0,0.0)          
    glRotatef(y_rotation,0.0,1.0,0.0)           
    glRotatef(z_rotation,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, tx.textures['dice'])
    glBegin(GL_QUADS)              
    
    # Face da frente
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(0.0, 1/2); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0,  1.0,  1.0)   
    glTexCoord2f(1/3, 0.0); glVertex3f(-1.0,  1.0,  1.0)  

    # Face de tras
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0, -1.0, -1.0)    
    glTexCoord2f(2/3, 1.0); glVertex3f(-1.0,  1.0, -1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    
    glTexCoord2f(1.0, 1/2); glVertex3f( 1.0, -1.0, -1.0)   
    
    # Face de cima
    glTexCoord2f(1/3, 0); glVertex3f(-1.0,  1.0, -1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0,  1.0,  1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(2/3, 0); glVertex3f( 1.0,  1.0, -1.0)   

    # Face de baixo   
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0, -1.0, -1.0)   
    glTexCoord2f(1/3, 1); glVertex3f( 1.0, -1.0, -1.0)   
    glTexCoord2f(2/3, 1); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0, -1.0,  1.0)    
    
    # Face da direita
    glTexCoord2f(2/3, 0.0); glVertex3f( 1.0, -1.0, -1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0, -1.0)   
    glTexCoord2f(1, 1/2); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(1, 0.0); glVertex3f( 1.0, -1.0,  1.0)  
    
    # Face da esquerda
    glTexCoord2f(0, 1/2); glVertex3f(-1.0, -1.0, -1.0)  
    glTexCoord2f(0, 1); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1/3, 1); glVertex3f(-1.0,  1.0,  1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f(-1.0,  1.0, -1.0)   
    
    glEnd()
    
    x_rotation = x_rotation + 0.01                 # X rotation
    y_rotation = y_rotation + 0.01                 # Y rotation
    z_rotation = z_rotation + 0.01                 # Z rotation

    glutSwapBuffers()

def keyPressed(tecla, x, y):
    global direction
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        direction = (1, 0, 0)
    elif tecla == b'y' or tecla == b'Y':   
        direction = (0, 1, 0)
    elif tecla == b'z' or tecla == b'Z':
        direction = (0, 0, 1)

def specialKeyPressed(tecla, x, y):
    global x_rotation, y_rotation, z_rotation, direction
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")
        x_rotation -= direction[0]
        y_rotation -= direction[1]
        z_rotation -= direction[2]
    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
        x_rotation += direction[0]
        y_rotation += direction[1]
        z_rotation += direction[2]
    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")

if __name__ == '__main__':
    tx.main(DrawGLScene, keyPressed, specialKeyPressed)