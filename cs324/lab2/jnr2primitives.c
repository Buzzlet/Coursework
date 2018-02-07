// Geometric Primitives
// CS324 Lab2
// Donald Sylwester
// Joel Ristvedt 1/26/2016

#include <GL/glut.h>
#include <stdio.h>
int which = 0;

void myinit()
{
  glClearColor(1.0, 1.0, 1.0, 1.0);
  glColor3f(0.0, 0.3, 0.0);
  glPointSize(5.0);
  glLineWidth(2.5);

  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(0.0, 50.0, 0.0, 50.0);
  glMatrixMode(GL_MODELVIEW);
}

void vertices()
{
  GLfloat vertices[6][3] = {{0.0, 0.0, 0.0},
                            {20.0, 10.0, 0.0},
                            {10.0, 20.0, 0.0},
                            {25.0, 25.0, 0.0},
                            {40.0, 50.0, 0.0},
                            {50.0, 40.0, 0.0}};

  //glBegin(GL_TRIANGLES);
  glVertex3f(vertices[0][0], vertices[0][1], vertices[0][2]);
  glVertex3f(vertices[1][0], vertices[1][1], vertices[1][2]);
  glVertex3f(vertices[2][0], vertices[2][1], vertices[2][2]);
  //glEnd();

  //glBegin(GL_TRIANGLES);
  glVertex3f(vertices[3][0], vertices[3][1], vertices[3][2]);
  glVertex3f(vertices[4][0], vertices[4][1], vertices[4][2]);
  glVertex3f(vertices[5][0], vertices[5][1], vertices[5][2]);
  //glEnd();
}

void display()
{
  glClear(GL_COLOR_BUFFER_BIT);
  //glCullFace(GL_FRONT_AND_BACK);
  //glEnable(GL_CULL_FACE);
  //printf("Frame Update! Which = %d\n", which);
  switch(which)
  {
    case 0:
      glBegin(GL_POINTS);
      vertices();
      glEnd();
      glFlush();
      break;

    case 1:
      glBegin(GL_LINES);
      vertices();
      glEnd();
      glFlush();
      break;

    case 2:
      glBegin(GL_LINE_STRIP);
      vertices();
      glEnd();
      glFlush();
      break;

    case 3:
      glBegin(GL_LINE_LOOP);
      vertices();
      glEnd();
      glFlush();
      break;

    case 4:
      glBegin(GL_TRIANGLES);
      vertices();
      glEnd();
      glFlush();
      break;

    case 5:
      glBegin(GL_TRIANGLE_STRIP);
      vertices();
      glEnd();
      glFlush();
      break;

    case 6:
      glBegin(GL_TRIANGLE_FAN);
      vertices();
      glEnd();
      glFlush();
      break;

    case 7:
      glBegin(GL_QUADS);
      vertices();
      glEnd();
      glFlush();
      break;

    case 8:
      glBegin(GL_QUAD_STRIP);
      vertices();
      glEnd();
      glFlush();
      break;

    case 9:
      glBegin(GL_POLYGON);
      vertices();
      glEnd();
      glFlush();
      break;

    case 10:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidSphere(25, 1000, 10);
      glPopMatrix();
      glFlush();
      break;

    case 11:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireSphere(25, 1000, 10);
      glPopMatrix();
      glFlush();
      break;

    case 12:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidCube(25);
      glPopMatrix();
      glFlush();
      break;

    case 13:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireCube(25);
      glPopMatrix();
      glFlush();
      break;

    case 14:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidCone(25, 30, 1000, 10);
      glPopMatrix();
      glFlush();
      break;

    case 15:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireCone(25, 30, 1000, 10);
      glPopMatrix();
      glFlush();
      break;

    case 16:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidTorus(10, 15, 10, 10);
      glPopMatrix();
      glFlush();
      break;

    case 17:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireTorus(10, 15, 10, 10);
      glPopMatrix();
      glFlush();
      break;

    case 18:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidDodecahedron();
      glPopMatrix();
      glFlush();
      break;

    case 19:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireDodecahedron();
      glPopMatrix();
      glFlush();
      break;

    case 20:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidOctahedron();
      glPopMatrix();
      glFlush();
      break;

    case 21:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireOctahedron();
      glPopMatrix();
      glFlush();
      break;

    case 22:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidTetrahedron();
      glPopMatrix();
      glFlush();
      break;

    case 23:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireTetrahedron();
      glPopMatrix();
      glFlush();
      break;

    case 24:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidIcosahedron();
      glPopMatrix();
      glFlush();
      break;

    case 25:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireIcosahedron();
      glPopMatrix();
      glFlush();
      break;

    case 26:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutSolidTeapot(15);
      glPopMatrix();
      glFlush();
      break;

    case 27:
      glPushMatrix();
      glTranslatef(25.0, 25.0, 0.0);
      glutWireTeapot(15);
      glPopMatrix();
      glFlush();
  }// and I just realized I could have put one glFlush() down here..
}


void keyPressed(unsigned char key, int x, int y)
{
  //printf("Entered keyPressed! Key = %d\n", key);
  switch(key)
  {
    case 'a':
      which = 0;
      break;
    case 'b':
      which = 1;
      break;
    case 'c':
      which = 2;
      break;
    case 'd':
      which = 3;
      break;
    case 'e':
      which = 4;
      break;
    case 'f':
      which = 5;
      break;
    case 'g':
      which = 6;
      break;
    case 'h':
      which = 7;
      break;
    case 'i':
      which = 8;
      break;
    case 'j':
      which = 9;
      break;
    case 'k':
      which = 10;
      break;
    case 'K':
      which = 11;
      break;
    case 'l':
      which = 12;
      break;
    case 'L':
      which = 13;
      break;
    case 'm':
      which = 14;
      break;
    case 'M':
      which = 15;
      break;
    case 'n':
      which = 16;
      break;
    case 'N':
      which = 17;
      break;
    case 'o':
      which = 18;
      break;
    case 'O':
      which = 19;
      break;
    case 'p':
      which = 20;
      break;
    case 'P':
      which = 21;
      break;
    case 'q':
      which = 22;
      break;
    case 'Q':
      which = 23;
      break;
    case 'r':
      which = 24;
      break;
    case 'R':
      which = 25;
      break;
    case 's':
      which = 26;
      break;
    case 'S':
      which = 27;
  }
  display();
}


int main(int argc, char** argv)
{
  glutInit(&argc, argv);
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
  glutInitWindowSize(500, 500);
  glutInitWindowPosition(0, 0);
  glutCreateWindow("Geometric Primitives");
  glutKeyboardFunc(keyPressed);
  glutDisplayFunc(display);
  myinit();
  glutMainLoop();
}
