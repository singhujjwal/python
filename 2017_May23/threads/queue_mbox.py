from threading import Thread
from queue import Queue
from random import sample, random
from time import sleep

SAMPLE_SIZE = 10

data_queue = Queue(SAMPLE_SIZE)
result_queue = Queue(SAMPLE_SIZE)

def producer():
    batch_count = 0
    while True:
        batch_count += 1
        dataset = sample(tuple(range(1, 100)), 10)
        print("producer: batch {}, sample data = {}".format(batch_count,
                                                            str(dataset)))
        for v in dataset:
            sleep(random())
            data_queue.put(v)

        print("producer: waiting for batch {} to complete.".format(batch_count))
        data_queue.join()

        result = []
        for v in range(SAMPLE_SIZE):
            result.append(result_queue.get())
        print("producer: batch {} complete: result = {}.".format(batch_count,
                                                                 str(result)))
        result_queue.task_done()



def consumer(n):
    while True:
        print("consumer-{}: waiting for value...".format(n))
        v = data_queue.get()
        print("consumer-{}: got value: {}".format(n, v))
        sleep(random())
        if result_queue.full(): result_queue.join()
        result_queue.put(v*v)
        data_queue.task_done()

p = Thread(target=producer)
consumers = {}
for i in range(10):
    consumers[i+1] = Thread(target=consumer, args=(i+1,))
    consumers[i+1].start()

p.start()


