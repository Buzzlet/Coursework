// Author: Joel Ristvedt
// Program: comm_child1.c
// Parent: comm_parent.c

/*
This program:
    -gets filename from parent to contain other file names
    -generates a list of search files from /tmp in the form cs261*
    -stores search file names in filename
*/

//Includes
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>

#define HALF_DUPLEX     "halfduplex.dat"
#define MAX_BUF_SIZE    255


int main(int argc, char** argv)
{
    printf("<CHILD 1> Comm_child1 started! \n");
    char comm_buf[MAX_BUF_SIZE];

    int num_read;
    FILE* pipe_file = fopen(HALF_DUPLEX, "a+");
    fgets(comm_buf, MAX_BUF_SIZE, pipe_file);

    num_read = strlen(comm_buf)-1;
    // Add ending and a null terminator
    comm_buf[num_read] = '.';
    comm_buf[num_read+1] = 'd';
    comm_buf[num_read+2] = 'a';
    comm_buf[num_read+3] = 't';
    comm_buf[num_read+4] = '\0';

    printf("<CHILD 1> File name aquired: %s\n", comm_buf);

    FILE* files_file = fopen(comm_buf,"w+");

    FILE* ls_pipe = popen("ls /tmp/cs261*", "r");
    if (ls_pipe == NULL)
    {
        printf("<CHILD 1> Error opening LS pipe! ");
        exit(0);
    }

    char file_buf[100];

    while(fgets(file_buf, 100, ls_pipe) != NULL)
    {
        fwrite(file_buf, 1, strlen(file_buf), files_file);
        printf("<CHILD 1> Search file found: %s",file_buf);
    }

    // Note to Joel: the parent process already knows the files_file name
    // implicitly

    fclose(files_file);
    pclose(ls_pipe);
    fclose(pipe_file);
}
