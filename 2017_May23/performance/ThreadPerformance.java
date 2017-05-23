class Worker implements Runnable {
    Long y = 0L;
    public void run() {
        String w = Thread.currentThread().getName();

        System.out.println("Starting worker: " + w);
        for (Integer i=0; i<1000; i++) {
            for (Integer j=0; j<10000; j++) {
                y += i*j;
            }
        }
        System.out.println("Worker " + w + " complete");
    }
}

class ThreadPerformance {
    public static void startWorkers() throws Exception {
        Runnable worker = new Worker();
        Thread[] pool = new Thread[16];
        
        for (int i=0; i<16; i++) {
            pool[i] = new Thread(worker);
            pool[i].start();
        }
        System.out.println("Created 16 workers...");

        for (int i=0; i<16; i++) {
            pool[i].join();
        }
        System.out.println("All workers complete...");
    }

    public static void main(String[] args) throws Exception {
   
        long start = System.currentTimeMillis();
        startWorkers();
        long duration = System.currentTimeMillis() - start;
        System.out.printf("startWorkers: %f seconds.\n", duration / 1000.0);
    }
}

