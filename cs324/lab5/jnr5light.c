// animate.c

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define BASE_HEIGHT 2.0
#define PEDESTAL_HEIGHT 3.0
#define PEDESTAL_RADIUS 7.0
#define CUBE_SIZE 5.0
#define CONE_SIZE 2.5
#define SPHERE_SIZE 3.0
#define SPHERE2_SIZE 2.0
#define BAR_HEIGHT 0.5
#define BAR_LENGTH 15.0
int seed = 9001;
float angle = 45.0;
float time = 0;
float cube_height = 5.0;
float cone_height = 2.5;
float sphere_height = 3.0;
float sphere2_height = 2.0;
float amp[4] = {2.0, 2.0, 0.75, 1.5};
float freq[4] = {3.0, 5.0, 23.0, 7.0};
float phase[4] = {13.0, 17.0, 19.0, 23.0};
GLUquadricObj *pedestal;

// array index corresponds to order to be drawn (index 0 is on bottom)
// number corresponds to object to be drawn
// 0 = cube, 1 = cone, 2 = sphere, 3 = sphere2
int draw_order[4] = {0, 1, 2, 3};

void base()
{
  glPushMatrix();
  glScalef(1.0, .1, 1.0);
  glutSolidCube(20);
  glPopMatrix();
}


void myPedestal()
{
  glPushMatrix();
  glRotatef(-90.0, 1.0, 0.0, 0.0);
  gluCylinder(pedestal,PEDESTAL_RADIUS, PEDESTAL_RADIUS, PEDESTAL_HEIGHT,25,25);
  glPopMatrix();
}


void myCube()
{
  glPushMatrix();
  glScalef(1.0, cube_height / CUBE_SIZE, 1.0);
  glutSolidCube(CUBE_SIZE);
  glPopMatrix();
}


void myCone()
{
  glPushMatrix();
  glScalef(1.0, cone_height / CONE_SIZE, 1.0);
  glRotatef(-90.0, 1.0, 0.0, 0.0);
  glutSolidCone(CONE_SIZE, CONE_SIZE, 25, 25);
  glPopMatrix();
}


void mySphere()
{
  glPushMatrix();
  glScalef(1.0, sphere_height / SPHERE_SIZE, 1.0);
  glutSolidSphere(SPHERE_SIZE, 25, 25);
  glPopMatrix();
}

void mySphere2()
{
  glPushMatrix();
  glScalef(1.0, sphere2_height / SPHERE2_SIZE, 1.0);
  glutSolidSphere(SPHERE2_SIZE, 25, 25);
  glPopMatrix();
}

void myBar()
{
  glPushMatrix();
  glTranslatef(0.0, BAR_HEIGHT * 0.5, BAR_LENGTH * 0.5);
  glScalef(BAR_HEIGHT / BAR_LENGTH, BAR_HEIGHT / BAR_LENGTH, 1.0);
  glutSolidCube(BAR_LENGTH);
  glPopMatrix();

}

void myInit()
{
  srand(seed);
  glClearColor(0.5, 0.5, 0.5, 1.0);
  glColor3f(0.0, 0.3, 1.0);
  glDepthFunc(GL_LEQUAL);
  glEnable(GL_DEPTH_TEST);

  GLfloat light_position0[] = {10.0, 10.0, 10.0, 0.0};
  GLfloat light_position1[] = {-10.0, 10.0, 10.0, 0.0};
  GLfloat specular1[] = {0.7, 0.7, 0.7, 1.0};
  GLfloat diffuse0[] = {0.1, 0.1, 0.1, 1.0};
  GLfloat diffuse1[] = {1.0, 0.0, 0.0, 1.0};
  glLightfv(GL_LIGHT0, GL_POSITION, light_position0);
  glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0);

  glLightfv(GL_LIGHT1, GL_POSITION, light_position1);
  glLightfv(GL_LIGHT1, GL_SPECULAR, specular1);
  glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse1);

  glEnable(GL_LIGHTING);
  glEnable(GL_LIGHT0);
  glEnable(GL_LIGHT1);

  pedestal = gluNewQuadric();
  gluQuadricDrawStyle(pedestal, GLU_FILL);
}


void myReshape(int w, int h)
{
  glViewport(0, 0, w, h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(90.0, (GLfloat) w / (GLfloat) h, 1.0, 50.0);
  gluLookAt(7.0, 35.0, 20.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
  /*glOrtho(-10.0, 10.0, -10.0 * (GLfloat) h / (GLfloat) w,
          10.0 * (GLfloat) h / (GLfloat) w, -20.0, 20.0);*/
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();

}


void display()
{
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  glLoadIdentity();

  glColor3f(0.0, 0.3, 1.0);
  base();

  glTranslatef(0.0, BASE_HEIGHT / 2.0, 0.0);
  glColor3f(1.0, 0.0, 0.0);
  myPedestal();
  glTranslatef(0.0, PEDESTAL_HEIGHT, 0.0);

  // the idea here is that each object drawn will translate the coordinate
  // system to the top of the object drawn
  for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
  {
    switch(draw_order[i])
    {
      // CUBE
      case 0:
        glTranslatef(0.0, cube_height * 0.5, 0.0);
        glColor3f(0.0, 1.0, 0.0);
        myCube();
        glTranslatef(0.0, cube_height * 0.5, 0.0);
        break;
      // CONE
      case 1:
        glColor3f(0.5, 0.0, 0.5);
        myCone();
        glTranslatef(0.0, cone_height, 0.0);
        break;
      // SPHERE
      case 2:
        glTranslatef(0.0, sphere_height, 0.0);
        glColor3f(0.8, 0.8, 1.0);
        mySphere();
        glTranslatef(0.0, sphere_height, 0.0);
        break;
      // SPHERE2
      case 3:
        glTranslatef(0.0, sphere2_height, 0.0);
        glColor3f(0.75, 0.25, 0.5);
        mySphere2();
        glTranslatef(0.0, sphere2_height, 0.0);
    }
  }

  glColor3f(0.0, 0.0, 0.5);
  glRotatef(angle, 0.0, 1.0, 0.0);
  myBar();

  glFlush();
  glutSwapBuffers();
}


void menu(int id)
{
 switch(id)
 {
   // clockwise
   case 0:
     for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
     {
       if(draw_order[i] < (sizeof(draw_order) / sizeof(int)) - 1)
       {
         draw_order[i]++;
       }
       else
       {
         draw_order[i] = 0;
       }
     }
     break;
     // counter clockwise
    case 1:
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        if(draw_order[i] != 0)
        {
          draw_order[i]--;
        }
        else
        {
          draw_order[i] = sizeof(draw_order) / sizeof(int) - 1;
        }
      }
      break;
    // Randomize
    // using a trial-and-error approach
    case 2:
      // reset the array
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        draw_order[i] = -1;
      }
      // for each index, generate a unique number ranging from 0 to the length
      // of the array
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        while(draw_order[i] == -1)
        {
          int numFound = 0;
          int randNum = rand() % 4;
          // check to see if the random number is already in the array
          for(int j = 0; j < sizeof(draw_order) / sizeof(int); j++)
          {
            if(draw_order[j] == randNum)
            {
              numFound = 1;
            }
          }
          // if the number isn't already in the array, add it
          if(numFound == 0)
          {
            draw_order[i] = randNum;
          }
        }
      }
      break;
    case 3:
      exit(0);
  }
}


void idle()
{
  time += 0.001;
  cube_height = CUBE_SIZE + amp[0] * sin(freq[0] * time + phase[0]);
  cone_height = CONE_SIZE + amp[1] * sin(freq[1] * time + phase[1]);
  sphere_height = SPHERE_SIZE + amp[2] * sin(freq[2] * time + phase[2]);
  sphere2_height = SPHERE2_SIZE + amp[3] * sin(freq[3] * time + phase[3]);
  display();
}


void keyPressed(unsigned char key, int x, int y)
{
  switch(key)
  {
    case 'z':
      if(angle + 5.0 < 360.0)
      {
        angle += 5.0;
      }
      else
      {
        angle = 0.0;
      }
      break;
    case 'Z':
      if(angle - 5.0 > 0.0)
      {
        angle -= 5.0;
      }
      else
      {
        angle = 360.0;
      }
      break;
    case 'x':
      if(angle + 20.0 < 360.0)
      {
        angle += 20.0;
      }
      else
      {
        angle = 0.0;
      }
      break;
    case 'X':
      if(angle - 20.0 > 0.0)
      {
        angle -= 20.0;
      }
      else
      {
        angle = 360.0;
      }
  }
  display();
}

void main(int argc, char **argv)
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutInitWindowPosition(0, 0);
  glutCreateWindow("Statue");
  myInit();
  glutReshapeFunc(myReshape);
  glutDisplayFunc(display);
  glutIdleFunc(idle);
  glutKeyboardFunc(keyPressed);

  glutCreateMenu(menu);
  glutAddMenuEntry("Cycle Clockwise", 0);
  glutAddMenuEntry("Cycle Counter-Clockwise", 1);
  glutAddMenuEntry("Randomize", 2);
  glutAddMenuEntry("Quit", 3);
  glutAttachMenu(GLUT_RIGHT_BUTTON);
  glutMainLoop();
}
