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
#include <sys/param.h>
#include <time.h>

// Macros
#define NUM_PRIMES 500000

// Variables
void* sieve(void* arg);
void* prime_summary(void* arg);
int current_prime = 1;
// each index corresponds to an integer being checked
// prime = 1
// not prime = 0
char primes[NUM_PRIMES] = {0,0};
int workers = 5;
int result = 0;
// the greatest number whose primality we know
int sieve_progress = 3;
pthread_mutex_t cake_bouncer = PTHREAD_MUTEX_INITIALIZER;
char preamble[] =
    "\nThreads Program\n This program implements the Sieve of Eratosthenes " 
    "using by default 5 worker threads. Ultimately, all of the primes below 500,000 "
    "should be discovered and counted.\n";


int main()
{
    clock_t start_clock = clock();
    clock_t end_clock;
    clock_t ellapsed_time;
    // Get the number of worker threads 
    printf("\nPress enter for the default number of workers enter a number of workers(1-5): ");
    scanf(" %d", &result);
    if(result > 0 && result <= 5)
	workers = result;
    
    // an array of "pthread_t"s, one for each worker
    pthread_t threadID[workers+1];

    // initialize all but 0 and 1 to prime
    int p;
    for(p=2;p<NUM_PRIMES;p++)
    {
        primes[p] = 1;
    }
    

    // thread number (an index for threadID)
    long thread_num;

    // create and start worker threads
    for(thread_num = 0; thread_num < workers; thread_num++)
    {
        printf("Creating thread %ld\n", thread_num);
        if(pthread_create(&threadID[thread_num], NULL, &sieve, (void *) thread_num))
            printf("Error creating thread %ld!\n", thread_num);
    }

    // wait for all the threads to complete then join back up to just one thread
    for(thread_num = 0; thread_num < workers; thread_num++)
    {
        pthread_join(threadID[thread_num], NULL);
    }

    
    printf("Creating thread %ld\n", thread_num++);
    // make the summary thread and start it
    if(pthread_create(&threadID[thread_num], NULL, &prime_summary, (void*) thread_num))
	printf("Error creating thread %d\n", thread_num);
    pthread_join(threadID[thread_num], NULL);
    
    
    // print result 
    int prime_count = 0;
    int j;
    for(j=2; j<NUM_PRIMES; j++)
    {
	if(primes[j])
        {
            prime_count++;
            //printf("Num: %d, Prime: %d\n", j, primes[j]);
        }
    }

    printf("Total primes from 0 to %d: %d\n", NUM_PRIMES, prime_count);
    end_clock = clock();
    ellapsed_time = end_clock - start_clock;
    printf("Program completion time: %.10f secs\n", (float)  ellapsed_time / CLOCKS_PER_SEC);
}

void* sieve(void* arg)
{
    
    long id = (long) arg;
    int my_prime;
        
    printf("<Thread %ld> Running routine!\n", id);

    do 
    {
	my_prime = -1;
	// ONLY ONE CAN EAT CAKE
	pthread_mutex_lock(&cake_bouncer);
        // Find the next potential prime after the current prime
	int test_num;
	for(test_num = current_prime+1; my_prime == -1; test_num++)
	{
	    // wait until the sieve is far enough to guarantee primality
	    while(sieve_progress <= test_num);
	    if(primes[test_num])
	    {
		my_prime = test_num;
	    }
	}
	// change prime to search from
	current_prime = my_prime;
	
	// LET THEM EAT CAKE
	pthread_mutex_unlock(&cake_bouncer);
	// Mark off all multiples of my_prime
	if (my_prime < 1000)
	    printf("<Thread %ld> Processing prime %d...\n", id, my_prime);

	int counter = my_prime;
	while(counter < NUM_PRIMES)
	{
	    counter += my_prime;
	    if(counter < NUM_PRIMES)
	    {
		primes[counter] = 0;
	    }
	}

	// Update sieve progress
	sieve_progress = MAX(sieve_progress, my_prime * my_prime);
	
    } while(sieve_progress <= NUM_PRIMES);

    pthread_exit(0);
}

void* prime_summary(void* arg)
{
    int i;
    int count = 0;
    printf("Primes\n");
    for(i=0; i<1000; i++)
	{
	    if(primes[i])
		{
		    count++;
		    printf("%5d", i);
		}
	    if(count > 6)
		{
		    printf("\n");
		    count = 0;
		}
	}
}


/*

Analysis: This program produces correct output, but is not optimal. It uses a
mutex lock to keep threads from being assigned the same prime to mark off
multiples for. The more threads you add, the slower this program executes.
I'm not sure exactly why this is, but it is still a functional multithreaded
sieve.

*/
