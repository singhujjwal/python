

def daemonize():
    import os
    pid = os.fork()
    if pid > 0: 
        with open("daemon1.pid", "w") as f: f.write(str(pid))
        exit(0)

    os.close(0)
    os.close(1)
    os.close(2)
    os.setsid()


print "Creating a background service..."
daemonize()

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
from time import sleep
for i in range(60):
    sleep(1)
    logging.info("Counting: {}".format(i))

logging.info("Exiting daemon...")

