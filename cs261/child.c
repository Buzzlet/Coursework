// Author:  Joel Ristvedt
// Class:   cs261
// Program: child.c

# include <stdio.h>
# include <stdlib.h>
# include <errno.h>
# include <ctype.h>
# include <sys/stat.h>
# include <sys/wait.h>
# include <time.h>
# include <unistd.h>


int main(int argc, char** argv)
{
    long start_time = clock();
    // print parent's PID
    printf("<CHILD %d> PPID: %d\n", getpid(), getppid());

    // print the child's total user time and pid
    long end_time = clock();
    float total_time = (end_time - start_time)/CLOCKS_PER_SEC;
    printf("<CHILD %d> Child process executed in %2.5f seconds!\n", getpid(), total_time);
    return(0);
}
