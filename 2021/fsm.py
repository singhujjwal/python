
# generator

def fib():
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a+b

        # coroutines consume

def grep(substr):
    while True:
        line = yield
        if substr in line:
            print (f"Found the substr {substr} in {line}" )


class FSM:
    def __init__(self):
        # initializing states
        self.start = self._create_start()
        self.q1 = self._create_q1()
        self.q2 = self._create_q2()
        self.q3 = self._create_q3()
        
        # setting current state of the system
        self.current_state = self.start

        # stopped flag to denote that iteration is stopped due to bad
        # input against which transition was not defined.
        self.stopped = False

    def send(self, char):
        """The function sends the curretn input to the current state
        It captures the StopIteration exception and marks the stopped flag.
        """
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True
        
    def does_match(self):
        """The function at any point in time returns if till the current input
        the string matches the given regular expression.

        It does so by comparing the current state with the end state `q3`.
        It also checks for `stopped` flag which sees that due to bad input the iteration of FSM had to be stopped.
        """
        if self.stopped:
            return False
        return self.current_state == self.q3

    ...
    
    # @prime
    def _create_q2(self):
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if char == 'b':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.q2
            elif char == 'c':
                # on receiving `c` the state moves to `q3`
                self.current_state = self.q3
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break



if __name__ == '__main__':
    fgen = fib()
    print ([next(fgen) for _ in range(10)])
