// Author: Joel Ristvedt
// Program: comm_child23.c
// Parent: comm_parent.c

/*
This program:
    -gets filename and search string from parent
    -continuously opens filename and searches for search string
    -returns number of occurences to parent
    -terminates on parent's signal
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
    int child_num = 3;

    char comm_buf[MAX_BUF_SIZE];
    FILE* fd = fopen(HALF_DUPLEX, "a+");
    fgets(comm_buf, MAX_BUF_SIZE, fd);

    char filename[MAX_BUF_SIZE];

    strcpy(filename, comm_buf);

    int name_len = strlen(filename)-1;
    filename[name_len] = '.';
    filename[name_len+1] = 'd';
    filename[name_len+2] = 'a';
    filename[name_len+3] = 't';
    filename[name_len+4] = '\0';

    fgets(comm_buf, MAX_BUF_SIZE, fd);
    pid_t child2_pid = atoi(comm_buf);
    printf("<CHILD2/3> child2_pid: %d\n", child2_pid);

    char child2_head[] = "<CHILD_2>";
    char child3_head[] = "<CHILD_3>";
    char* print_head = child3_head;

    // identify second child
    if(getpid() == child2_pid)
    {
        print_head = child2_head;
        child_num = 2;
    }

    fgets(comm_buf, MAX_BUF_SIZE, fd);

    char search_str[50];
    strcpy(search_str, comm_buf);

    char instruction[100];

    char current_file[50];
    int file_count;
    FILE * files_file = fopen(filename, "a+");
    FILE * file_point;

    char result_str[10];
    int occurrences = 0;

    search_str[strlen(search_str)-1] = '\0';

    while(fgets(current_file, 50, files_file) != 0)
    {
        printf("%s File acquired: %s", print_head, current_file);
        if((child_num % 2) == (file_count % 2))
        {
            current_file[strlen(current_file)-1] = '\0';

            sprintf(instruction, "grep -o \"%s\" %s | wc -l", search_str, current_file);
            //printf("%s\n",instruction);
            file_point = popen(instruction, "r");
            fgets(result_str, 10, file_point);
            //printf("Result string: %s\n", result_str);
            occurrences += atoi(result_str);
        }
        file_count++;
    }

    printf("%s Occurrences from Process %d: %d\n", print_head, child_num, occurrences);

}
