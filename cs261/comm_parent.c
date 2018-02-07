// Author: Joel Ristvedt
// Program: comm_parent.c
// Child: comm_child.c

/*
This program:
    -creates 3 child processes
    -sets up direct communication with each child
    -sets up communication between the children
    -gets file name and passes it to child 1
    -detects when child 1 has finished
    -continually gets a search string
    -opens the file and passes the file names inside to children 2 & 3
    -passes search string to children 2 & 3
    -terminates children, closes files, and ends when no more searches
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

char* trim_fgets(char *str, int n, FILE *stream)
    {
        printf("BEFORE:\"%s\"\n", str);
        char* tmp = fgets(str, n, stream);
        if(str[strlen(str)-1] == '\n')
        {
            str[strlen(str)-1] = '\0';
        }
        printf("AFTER:\"%s\"\n", str);
    }



int main(int argc, char** argv)
{
    // Get file name from user
    char filename[25];
    printf("<PARENT> Enter a file name: ");
    scanf(" %s", filename);

    char search_str[64];
    printf("<PARENT> Enter a search string: ");
    scanf(" %s", search_str);

    // make the named pipe and check for success
    int pipe_success = mkfifo(HALF_DUPLEX, 0666);
    if ((pipe_success == -1) && (errno != EEXIST))
    {
        perror("<PARENT> Problem creating named pipe! ");
        exit(0);
    }

    // get rid of anything in the file beforehand
    // * OBSOLETE *
    // fclose(fopen(HALF_DUPLEX, "w"));
    // open the named pipe up for reading and writing
    FILE* fd = fopen(HALF_DUPLEX, "w+");
    fprintf(fd, "%s\n", filename);
    fflush(fd);

    // Get current process's pid
    pid_t parent_pid;
    parent_pid = getpid();

    // Creates child 1
    pid_t child1_pid;
    child1_pid = fork();

    // identify and assign the new child to comm_child1 program
    switch(child1_pid)
    {
        // Failed fork
        case -1:
            printf("<PARENT> Child 1 fork failure!\n ");
            break;

        // Child 1
        case 0:
            execvp("./comm_child1", argv);

        // Parent
        default:
            wait(0);
            break;
    }

    pid_t child2_pid = fork();
    pid_t child3_pid;

    //printf("<PARENT> child2_pid: %d\n", child2_pid);
    //fprintf(fd, "%d\n", child2_pid);
    //fflush(fd);

    switch(child2_pid)
    {
        // Failed fork
        case -1:
            printf("<PARENT> Child 2 fork failure!\n");
            break;

        // Child 2
        case 0:
            execvp("./comm_child23", argv);
            break;

        // Parent
        default:
            printf("<PARENT> child2_pid: %d\n", child2_pid);
            fprintf(fd, "%d\n", child2_pid);
            fflush(fd);
            child3_pid = fork();

            fprintf(fd, "%s\n", search_str);
            fflush(fd);
            switch(child3_pid)
            {
                // Failed fork
                case -1:
                    printf("<PARENT> Child 3 fork failure!\n");
                    break;
                // Child 3
                case 0:
                    execvp("./comm_child23", argv);
                    break;
                // Parent
                default:
                    wait(0);
                    break;
            }
            wait(0);
            break;
    }
    //printf("<PARENT> child2_pid: %d\n", child2_pid);
    //fprintf(fd, "%d\n", child2_pid);
    //fflush(fd);

    char answer[1];
    while(strcmp("n", answer) != 0)
    {
        printf("<PARENT> Enter a search string: ");
        scanf(" %s", search_str);

        // send string to children 2 and 3
        fprintf(fd, "%s", search_str);
        fflush(fd);
        // wait for child 2 and 3 to finish
        wait(0);

        printf("<PARENT> Would you like to search for another string (y/n)? ");
        scanf(" %s", answer);
    }
}


/*
To Joel: You still have to hook up communication to comm_child23 or can
the existing pipe be accessed from comm_child23
*/
