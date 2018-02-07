// dorm.c

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <jpeglib.h>
#include <jerror.h>

#define BED 1 // height of 10, 2.5 above, 7.5 below
#define CHAIR 2 // height of 9, 4.5 above, 4.5 below
#define DESK 3 // height of 11, 1 above origin, 10 below
#define LAMP 4 // height of 5, 5 above origin

int debug = FALSE;

GLuint portrait, portrait2, wall, window, wood, checkerboard;
GLfloat position[] = {0.0, 17.0, 0.0, 1.0};


GLuint loadTexJPG(const char * filename)
{
  GLuint texture;
  GLuint type = GL_RGB;

  FILE* file = fopen(filename, "rb");  //open the file
  struct jpeg_decompress_struct info;  //the jpeg decompress info
  struct jpeg_error_mgr err; // error handler

  info.err = jpeg_std_error(&err);


  jpeg_create_decompress(&info);       //sets info to all the default stuff
  jpeg_stdio_src(&info, file);    //tell the jpeg lib the file we'er reading
  jpeg_read_header(&info, TRUE);   //tell it to start reading it
  if(debug){printf("Channels: %d\n", info.num_components);}
  jpeg_start_decompress(&info);    //decompress the file
  unsigned long size = info.output_width * info.output_height * 3;

  unsigned char * dataBuff = malloc(size);
  unsigned char ** dataPointer = malloc(sizeof(unsigned char *));
  *dataPointer = dataBuff;
  // while scan lines remain to be read
  while(info.output_scanline < info.output_height)
  {
    jpeg_read_scanlines(&info, dataPointer, 1);
    *dataPointer = dataBuff + (info.output_scanline * 3 * info.output_width);
  }

  jpeg_finish_decompress(&info);   //finish decompressing this file

  fclose(file);                    //close the file

  // allocate a texture name
  glGenTextures(1, &texture);
  // select current texture
  glBindTexture(GL_TEXTURE_2D, texture);
  // mix texture with color for shading
  glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);

  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

  glTexImage2D(GL_TEXTURE_2D, 0, type, info.output_width, info.output_height, 0,
               type, GL_UNSIGNED_BYTE, dataBuff);

  if(debug)
  {
    unsigned char * address = dataBuff;
    int counter;
    while(address < dataBuff + size)
    {
      counter++;
      printf("R: %d, G: %d, B: %d\n", *address, *(address+1), *(address+2));
      address += 3;
    }
    printf("Pixels: %d\n", counter);
  }

  return texture;
}


void myInit()
{
  glClearColor(0.5, 0.5, 0.5, 1.0);
  glDepthFunc(GL_LEQUAL);
  glEnable(GL_DEPTH_TEST);

  GLfloat global_ambient[] = {0.3, 0.3, 0.3, 1.0};
  GLfloat specular[] = {0.8, 0.8, 0.8, 1.0};
  GLfloat diffuse[] = {0.7, 0.7, 0.7, 1.0};


  glEnable(GL_LIGHTING);
  glEnable(GL_LIGHT0);

  glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient);
  glShadeModel(GL_SMOOTH);

  glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse);
  glLightfv(GL_LIGHT0, GL_SPECULAR, specular);
  glLightfv(GL_LIGHT0, GL_POSITION, position);

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);
  glEnable(GL_COLOR_MATERIAL);

  portrait = loadTexJPG("portrait.jpg");
  portrait2 = loadTexJPG("portrait2.jpg");
  wall = loadTexJPG("wall.jpg");
  wood = loadTexJPG("wood.jpg");
  window = loadTexJPG("window.jpg");
  checkerboard = loadTexJPG("checkerboard.jpg");

  glEnable(GL_TEXTURE_2D);
}

void displayRoom()
{
  // floor
  glColor3f(0.6, 0.12, 0.12);
  glPushMatrix();
  glTranslatef(0.0, -1.0, 0.0);
  glScalef(1.0, 0.05, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // floor
  glBegin(GL_QUADS);
  glBindTexture(GL_TEXTURE_2D, wood);
  glTexCoord2d(1, 0);glVertex3d(20, 0, 20);
  glTexCoord2d(0, 0);glVertex3d(20, 0, -20);
  glTexCoord2d(0, 1);glVertex3d(-20, 0, -20);
  glTexCoord2d(1, 1);glVertex3d(-20, 0, 20);
  glEnd();
  glBindTexture(GL_TEXTURE_2D, 0);

  // left wall
  glColor3f(0.5, 0.5, 0.5);
  glPushMatrix();
  glTranslatef(-21.0, 10.0, 0.0);
  glScalef(0.05, 0.5, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // right wall
  glPushMatrix();
  glTranslatef(21.0, 10.0, 0.0);
  glScalef(0.05, 0.5, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // back wall
  glPushMatrix();
  glTranslatef(0.0, 10.0, -21.0);
  glScalef(1.0, 0.5, 0.05);
  glutSolidCube(40);
  glPopMatrix();

  // checkerboard back wall
  glBindTexture(GL_TEXTURE_2D, checkerboard);
  glBegin(GL_QUADS);
  glTexCoord2d(1, 0);glVertex3d(20, 20, -20);
  glTexCoord2d(0, 0);glVertex3d(-20, 20, -20);
  glTexCoord2d(0, 1);glVertex3d(-20, 0, -20);
  glTexCoord2d(1, 1);glVertex3d(20, 0, -20);
  glEnd();

  // left wall
  glBindTexture(GL_TEXTURE_2D, wall);
  glBegin(GL_QUADS);
  glTexCoord2d(1, 0);glVertex3d(-20, 20, -20);
  glTexCoord2d(0, 0);glVertex3d(-20, 20, 20);
  glTexCoord2d(0, 1);glVertex3d(-20, 0, 20);
  glTexCoord2d(1, 1);glVertex3d(-20, 0, -20);
  glEnd();

  // right wall
  glBegin(GL_QUADS);
  glTexCoord2d(1, 0);glVertex3d(20, 20, 20);
  glTexCoord2d(0, 0);glVertex3d(20, 20, -20);
  glTexCoord2d(0, 1);glVertex3d(20, 0, -20);
  glTexCoord2d(1, 1);glVertex3d(20, 0, 20);
  glEnd();

  // ceiling
  glColor3f(0.4, 0.4, 0.4);
  glPushMatrix();
  glTranslatef(0.0, 21.0, 0.0);
  glScalef(1.0, 0.05, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // right wall
  glBegin(GL_QUADS);
  glTexCoord2d(1, 0);glVertex3d(20, 20, 20);
  glTexCoord2d(0, 0);glVertex3d(20, 20, -20);
  glTexCoord2d(0, 1);glVertex3d(-20, 20, -20);
  glTexCoord2d(1, 1);glVertex3d(-20, 20, 20);
  glEnd();

  glBindTexture(GL_TEXTURE_2D, 0);
}

void display()
{
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  glLoadIdentity();

  displayRoom();
  glPushMatrix();
  glTranslatef(-10.0, 10, -17.5);
  glCallList(DESK);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(10.0, 10, -17.5);
  glCallList(DESK);
  glPopMatrix();

  glPushMatrix();
  glColor3f(0, 0.4, 0);
  glTranslatef(-15, 7.5, 7.5);
  glRotatef(90, 0, 1, 0);
  glCallList(BED);
  glPopMatrix();

  glPushMatrix();
  glColor3f(0, 0, 0.4);
  glTranslatef(15, 7.5, 7.5);
  glRotatef(90, 0, 1, 0);
  glCallList(BED);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(5, 4.5, 0);
  glRotatef(-45, 0, 1, 0);
  glCallList(CHAIR);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(-5, 4.5, 10);
  glRotatef(0, 0, 1, 0);
  glCallList(CHAIR);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(-5, 11, -17);
  glCallList(LAMP);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(15, 11, -17);
  glCallList(LAMP);
  glPopMatrix();

  // draw a box for ceiling light
  glPushMatrix();
  glColor3f(1, 1, 0);
  glTranslatef(position[0], position[1] + 3.5, position[2]);
  glScalef(3.0, 1.0, 6.0);
  glutSolidCube(1);
  glPopMatrix();

  // portrait on left wall (Joel)
  glColor3f(0.8, 0.8, 0.8);
  glBindTexture(GL_TEXTURE_2D, portrait);
  glBegin(GL_QUADS);
  glTexCoord2d(1, 0);glVertex3d(-19.9, 17.5, -5);
  glTexCoord2d(0, 0);glVertex3d(-19.9, 17.5, 0);
  glTexCoord2d(0, 1);glVertex3d(-19.9, 12.5, 0);
  glTexCoord2d(1, 1);glVertex3d(-19.9, 12.5, -5);
  glEnd();

  // portrait on right wall (Caleb)
  glBindTexture(GL_TEXTURE_2D, portrait2);
  glBegin(GL_QUADS);
  glTexCoord2d(1, 0);glVertex3d(20, 17.5, -5);
  glTexCoord2d(0, 0);glVertex3d(20, 17.5, 0);
  glTexCoord2d(0, 1);glVertex3d(20, 12.5, 0);
  glTexCoord2d(1, 1);glVertex3d(20, 12.5, -5);
  glEnd();

  glBindTexture(GL_TEXTURE_2D, 0);

  glFlush();
  glutSwapBuffers();
}


void myReshape(int w, int h)
{
  glViewport(0, 0, w, h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(90.0, (GLfloat) w / (GLfloat) h, 1.0, 100.0);
  gluLookAt(0.0, 15.0, 25.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
}



void defineDisplayLists()
{
  GLuint myIndex = glGenLists(3);

  ///////////////////////// DEFINE A STANDARD BED /////////////////////////
  glNewList(myIndex, GL_COMPILE);
  // Matress
  glPushMatrix();
  glScalef(1.0, 0.15, 0.5);
  glutSolidCube(20);
  glPopMatrix();
  // One End
  glColor3f(0.42, 0.28, 0.22);
  glPushMatrix();
  glTranslatef(10.5, -2.5, 0.0);
  glScalef(0.1, 1.0, 1.0);
  glutSolidCube(10);
  glPopMatrix();
  // Other End
  glPushMatrix();
  glTranslatef(-10.5, -2.5, 0.0);
  glScalef(0.1, 1.0, 1.0);
  glutSolidCube(10);
  glPopMatrix();
  glEndList();

  /////////////////////// DEFINE A STANDARD CHAIR /////////////////////
  glNewList(myIndex+1, GL_COMPILE);
  // Chair seat
  glColor3f(0.3, 1.0, 0.3);
  glPushMatrix();
  glScalef(1.0, 0.25, 1.0);
  glutSolidCube(4);
  glPopMatrix();
  // Chair back
  glColor3f(0.42, 0.28, 0.22);
  glPushMatrix();
  glTranslatef(-1.825, 2.5, 0.0);
  glScalef(0.125, 1.0, 1.0);
  glutSolidCube(4);
  glPopMatrix();
  // leg 1
  glPushMatrix();
  glTranslatef(1.875, -2.5, 1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();
  // leg 2
  glPushMatrix();
  glTranslatef(-1.875, -2.5, 1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();
  // leg 3
  glPushMatrix();
  glTranslatef(1.875, -2.5, -1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();
  // leg 4
  glPushMatrix();
  glTranslatef(-1.875, -2.5, -1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();

  glEndList();

  ///////////////////////// DEFINE A STANDARD DESK ///////////////////////////
  glNewList(myIndex+2, GL_COMPILE);
  //Desk top
  glColor3f(0.42, 0.28, 0.22);
  glPushMatrix();
  glScalef(1.0, 0.1, 0.5);
  glutSolidCube(20);
  glPopMatrix();
  // Desk large side
  glPushMatrix();
  glTranslatef(5.5, -5.5, 0.0);
  glScalef(0.45, 0.45, 0.5);
  glutSolidCube(20);
  glPopMatrix();
  // Desk top drawer
  glPushMatrix();
  glTranslatef(5.5, -3.5, 5.125);
  glScalef(7.0, 3.0, 0.25);
  glutSolidCube(1);
  glPopMatrix();
  // Desk bottom drawer
  glPushMatrix();
  glTranslatef(5.5, -7.5, 5.125);
  glScalef(7.0, 3.0, 0.25);
  glutSolidCube(1);
  glPopMatrix();
  // Desk small side
  glPushMatrix();
  glTranslatef(-9.5, -5.5, 0.0);
  glScalef(0.05, 0.45, 0.5);
  glutSolidCube(20);
  glPopMatrix();

  glEndList();

  //////////////////////// DEFINE A STANDARD LAMP /////////////////////////////
  glNewList(myIndex+3, GL_COMPILE);

  // base of lamp
  glColor3f(0.38, 0.68, 0.1);
  glPushMatrix();
  glTranslatef(0.0, 1.5, 0.0);
  glScalef(1.0, 3.0, 1.0);
  glutSolidCube(1);
  glPopMatrix();

  // lamp top
  glColor3f(0.95, 0.95, 0.31);
  glPushMatrix();
  glTranslatef(0.0, 2.5, 0.0);
  glutSolidSphere(1, 100, 100);
  glPopMatrix();

  glEndList();

  glListBase(myIndex);
}

void main(int argc, char **argv)
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutInitWindowPosition(0, 0);
  glutCreateWindow("Dorm");
  myInit();
  glutReshapeFunc(myReshape);
  glutDisplayFunc(display);
  defineDisplayLists();
  glutMainLoop();
}
