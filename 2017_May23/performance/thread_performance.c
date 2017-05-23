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


typedef struct {
    int value;
} integer_t;

integer_t *alloc_integer(int v)
{
    integer_t *i = (integer_t *)malloc(sizeof(integer_t));
    i->value = v;
    return i;
}

void free_integer(integer_t *i)
{
    free(i);
}

void* worker(void *arg)
{
    integer_t *iobj, *jobj, *yobj;
    int i, j, y;

    integer_t *w = (integer_t *)arg;

    yobj = alloc_integer(0);

    rprintf("Starting worker: %d\n", w->value);

    for (i=0; i<1000; i++) {
        iobj = alloc_integer(i);
        for (j=0; j<10000; j++) {
            jobj = alloc_integer(j);
            yobj->value += iobj->value * jobj->value;
            free_integer(jobj);
        }
        free_integer(iobj);
    }
    rprintf("Worker %d complete.\n", w->value);
    free_integer(w);

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
        pthread_create(&pool[i], NULL, worker, alloc_integer(i+1));
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

