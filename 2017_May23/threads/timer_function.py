class ScheduleFunction:
    def __init__(self, interval, fn, *args, **kwargs):
        from threading import Thread
        self.fn, self.args, self.kwargs = fn, args, kwargs
        self.interval = interval

        self.thread = Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        from time import sleep
        while True:
            self.fn(*self.args, **self.kwargs)
            sleep(self.interval)

def foo():
    from time import ctime
    print("Time now is {}".format(ctime()))

timer = ScheduleFunction(interval=5, fn=foo)
for i in range(10):
    c = input("Enter command: ")
    print("Processing {}".format(c))


