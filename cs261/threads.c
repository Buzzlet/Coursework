// Author: Joel Ristvedt
// Class:  cs261 Operating Systems I
// Program: threads.c

/*

This program:
    - Ultimately finds all primes below 500,000
    - Implements Sieve of Erotosthenes
    - Uses up to 5 threads
    - Uses a final thread to print summary

*/

// Includes
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <pthread.h>


#define WORKERS 2
#define NUM_PRIMES 50

void* thread_routine(void *arg);
int current_prime = 2;
// each index corresponds to an integer being checked
// prime = 
// not prime = 0
char primes[NUM_PRIMES] = {0,0};
// an array of "pthread_t"s, one for each worker
pthread_t threadID[WORKERS+1];
// an array of booleans corresponding to the status of a worker
char isBusy[WORKERS+1];
// an array of integers corresponding to a worker's ticket number
int ticket[WORKERS+1];


int main()
{
    // initialize all but 0 and 1 to prime
    int p;
    for(p=2;p<NUM_PRIMES;p++)
    {
        primes[p] = 1;
    }
    

    // thread number (an index for threadID)
    long thread_num;


    for(thread_num = 0; thread_num <= WORKERS; thread_num++)
    {
        printf("Creating threads, tnum = %ld\n", thread_num);
        if(pthread_create(&threadID[thread_num], NULL, &thread_routine, (void *) thread_num))
        {
            printf("Error creating thread!\n");
        }
    }
    for(thread_num = 0; thread_num <= WORKERS; thread_num++)
    {
        pthread_join(threadID[thread_num], NULL);
    }

}

void* thread_routine(void* arg)
{
    long thread_num = (long) arg;
    printf("<Thread %ld> Running routine!\n", thread_num);
    do
    {
        // ENTRY SECTION
        
        // END ENTRY SECTION
      
        if(primes[current_prime])
        {
            // CRITICAL SECTION
	    // Workers thread are given the current prime to work on
            int cp = current_prime;
	    int inc = current_prime;
	    printf("<Thread %ld> Working on prime %d.\n", thread_num, current_prime);
	    // END CRITICAL SECTION
	    
	    // Workers work on their primes
            while(cp < NUM_PRIMES)
            {
                cp += inc;
                if(cp < NUM_PRIMES)
                {
                    primes[cp] = 0;
                }
            }
        }
	// EXIT SECTION

	// END EXIT SECTION
	
	
        // REMAINDER SECTION
        current_prime++;
	// END REMAINDER SECTION
	
    } while(current_prime <= NUM_PRIMES);

    // for debugging
    int prime_count = 0;
    int j;
    for(j=2; j<=NUM_PRIMES; j++)
    {
        if(primes[j])
        {
            prime_count++;
            //printf("Num: %d, Prime: %d\n", j, primes[j]);
        }
    }

    printf("Total primes from 0 to %d: %d\n", NUM_PRIMES, prime_count);
    pthread_exit(0);
}
