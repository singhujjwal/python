#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>
#include <stdarg.h>

int rprintf(const char *fmt, ...);

int rprintf(const char *fmt, ...)
{
    va_list args;
    char buf[512];
    int rc;

    va_start( args, fmt );

    rc = vsnprintf(buf, sizeof(buf), fmt, args);
    va_end (args);

    if (rc > 0 && rc < sizeof(buf)) 
        write(1, buf, rc);

    return rc;
}

double diff_time(struct timespec start, struct timespec end)
{
    struct timespec interval;
	double duration;

    if ((end.tv_nsec - start.tv_nsec) < 0) {
        interval.tv_sec = end.tv_sec - start.tv_sec - 1;
        interval.tv_nsec = 1000000000 + end.tv_nsec - start.tv_nsec;
    } else {
        interval.tv_sec = end.tv_sec - start.tv_sec;
        interval.tv_nsec = end.tv_nsec - start.tv_nsec;
    }
    duration = interval.tv_sec + interval.tv_nsec / 1000000000.0;
    return duration;
}


void* worker(void *arg)
{
    int i, j, y;

    int *w = (int *)arg;

    rprintf("Starting worker: %d\n", *w + 1);

    for (i=0; i<1000; i++) {
        for (j=0; j<10000; j++) {
            y += i * j;
        }
    }
    rprintf("Worker %d complete.\n", *w + 1);

    return NULL;
}

void start_workers(void)
{
    struct timespec start, end;

    pthread_t pool[16];
    int i; 
    void *ret;

    clock_gettime(CLOCK_REALTIME, &start);
    for (i=0; i<16; i++) {
        pthread_create(&pool[i], NULL, worker, &i);
    }
    rprintf("Created 16 workers...\n");

    for (i=0; i<16; i++) {
        pthread_join(pool[i], &ret);
    }

    rprintf("All workers complete.\n");
    clock_gettime(CLOCK_REALTIME, &end);
	rprintf("start_workers : %f seconds.\n", diff_time(start, end));

}

int main()
{
    start_workers();
    return 0;
}

