// Author:  Joel Ristvedt
// Class:   cs261
// Program: create_child.c

/*
Description: Spawns four simultaneous children and prints out the total time
of itself and the accumulative user time of all children along with the 
process ids of all processes.
*/

int child_count = 4;

// includes
# include <stdio.h>
# include <stdlib.h>
# include <errno.h>
# include <ctype.h>
# include <sys/stat.h>
# include <sys/wait.h>
# include <time.h>
# include <unistd.h>


long get_cpu_time()
{
    return((double)clock() / CLOCKS_PER_SEC);
}


int main(int argc, char** argv)
{
    long parent_start_time = get_cpu_time();
    if(argc > 1)
    {
        // convert extra arguement to a number and set child_count to that number
        char* temp = argv[1];
        sscanf(temp, "%d", &child_count);
        //printf("i = %s, child_count = %d\n", temp, child_count);
    }

    // print parent pid
    pid_t parent_pid = getpid();
    printf("\nParent PID: %d\n", parent_pid);

    // make array to hold children pids and start/end times
    pid_t* children_pids = malloc(child_count * sizeof(pid_t));
    long* child_start_times = malloc(child_count * sizeof(long));
    long* child_end_times = malloc(child_count * sizeof(long));

    //fork the children processes
    for(int i = 0; i < child_count; i++)
    {
        children_pids[i] = fork();
        switch(children_pids[i])
        {

            // fork failed
            case -1:
                printf("The fork failed!\n");
                break;

            // Child process
            case 0:
                child_start_times[i] = get_cpu_time();
                execvp("./child", argv);
                child_end_times[i] = get_cpu_time();
                break;

            // Parent process
            default:
                printf("\n<PARENT> New fork's PID: %d\n", children_pids[i]);
                wait(0);
                break;

        }
    }

    float total_child_time;
    // print out pid of forked children
    printf("\n<PARENT> Children and execution times\n");
    for(int i = 0; i < child_count; i++)
    {
        float dt = child_end_times[i] - child_start_times[i];
        printf("<PARENT> CHILD %d: %2.5f sec\n", children_pids[i], dt);
        total_child_time += dt;
    }

    // print total accumulative user time of all children
    printf("\n<PARENT> Total user time for all children: %2.5f\n", total_child_time);

    // print parents total user time
    long parent_stop_time = get_cpu_time();
    long parent_total_time = parent_stop_time - parent_start_time;
    printf("<PARENT> Total user time: %ld\n\n", parent_total_time);

    return(0);
}

/*
Analysis:
The output does as I expect. It generates informational messages about a variable
number of processes making it appear that a variable number of processes have been
executed. The output will always say that it has taken 0 seconds to complete each child
process. The processes take so little time to execute so the ellapsed time is
mostly insignificant.
*/
