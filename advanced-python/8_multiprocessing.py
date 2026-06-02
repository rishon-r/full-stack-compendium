from multiprocessing import Process
from time import sleep

# CASE 1: Creating processes with classes (NON PYTHONIC)

print("-------Multiprocessing with classes-------\n")

class Hello(Process):

    def do(self):
        for i in range(5):
            print("Hello", i+1, "SYNC")

    def run(self):
        # The run method will be run in a separate process when start() is called
        for i in range(5):
            print("Hello", i+1, "ASYNC")

class Hi(Process):
    def do(self):
        for i in range(5):
            print("Hi", i+1, "SYNC")

    def run(self):
        for i in range(5):
            print("Hi", i+1, "ASYNC")

if __name__ == "__main__":
    print()  # For formatting sake
    print('An example of Synchronous Execution:\n')
    p1 = Hello()  # Creating Hello process object
    p2 = Hi()     # Creating Hi process object

    # Calling do() on both — runs in the CURRENT process, one after another
    p1.do()
    p2.do()
    # Above, Hello will be printed 5 times, then Hi will be printed 5 times (SYNCHRONOUS EXECUTION)

    print()  # For formatting sake
    print('An example of Asynchronous Execution:\n')
    # These will execute in separate processes (true parallelism, unlike threads)
    p1.start()  # Spawns a new process and calls run()
    p2.start()

    # Wait for both processes to finish before the main process continues
    p1.join()
    p2.join()

    # CASE 2: Multiprocessing with functions (PYTHONIC WAY)

    print()  # For formatting sake
    print("-------Multiprocessing with functions-------\n")

    def hi():
        for i in range(5):
            print("Hi", i+1, "ASYNC")
            sleep(1)

    def hello():
        for i in range(5):
            print("Hello", i+1, "ASYNC")
            sleep(1)

    def howdy():
        for i in range(5):
            print("Howdy", i+1, "ASYNC")
            sleep(1)

    # Initialising processes
    pf1 = Process(target=hi)     # Set target to the function each process should run
    pf2 = Process(target=hello)
    pf3 = Process(target=howdy)

    # Starting processes
    pf1.start()
    pf2.start()
    pf3.start()

    # Joining processes
    pf1.join()  # Wait here until pf1 finishes before proceeding
    pf2.join()
    pf3.join()

    # It is convention to join all processes before finishing an application.
    # Without these, the main process could exit before child processes finish,
    # which can cause incomplete execution or messy output.

    # KEY DIFFERENCE FROM THREADING:
    # Threads share the same memory space — multiprocessing spawns entirely separate
    # Python interpreters, each with their own memory. This bypasses the GIL (Global
    # Interpreter Lock), making multiprocessing better suited for CPU-bound tasks
    # (heavy computation), while threading is better for I/O-bound tasks (file reads,
    # network calls, sleep, etc.).