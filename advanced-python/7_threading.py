# THREADING 

'''
SOME THEORY:

What is threading? - Threading is essentially a concept by which we are allowed to run multiple operations at seemingly
the same time. This helps reduce the time it takes for our programs to run

In Python, we implement threading using the threading module.

What is a thread? - A thread refers to a lightweight subprocess. Multiple threads within the same process share resources and
memory.
(A lightweight subprocess is essentially a subprocess that does not require too many resources to run)

Python's threading module allows concurrent execution of code via multiple threads. 

What is concurrency?- Concurrency is simply the idea of doing multiple things at once. Tasks start, stop and resume over time, 
possibly overlapping in execution.

When discussing concurrency, we must also discuss parallelism.

What is parallelism?- Parallelism refers to the process of doing multiple things at exactly the same time, usually on multiple
CPU coures.

How do concurrency and parallelism differ?- Concurrency dicusses STRUCTURE, Parallelism is about EXECUTION.

Python gives us concurrency, but not true parallelism. This is due to something known as the Global Interpreter Lock (GIL).

To  understand threading further, we need to understand the difference between I/O bound tasks and CPU bound tasks.

What is a CPU bound task?- A CPU bound task is one that requires a lot of CPU cycles. These are essentially tasks that require
intensive computation. Some examples of such tasks are Image Processing and Matrix Multiplication. Such tasks benefit from
multiprocessing not threading. Multiprocessing involves running code on different cores of the CPU.

What is an I/O bound task?- I/O bound tasks are those that wait for external operations such as disk I/O or network requests. These
tasks benefit from threading due to the idea that we can run other threads when one thread is waiting.

Finally, we discuss the idea of Synchronous execution vs Asynchronous execution

What is Synchronous Execution? - In Synchronous execution, code runs line by line. This is simple, but inefficient for I/O 
bound tasks due to the wait times. This is because in Synchronous execution, each operation must complete before the next one 
starts.

What is Asynchronous Execution? - In Asynchronous execution, tasks can pause and allow others to run when waiting. This is very
efficient for I/O bound tasks with many operations.

Asynchronous execution and threading is very important and expected when coding better doftware systems. This is because concurrency
allows us to save a lot of time by providing us the facility to run other tasks when a particular task is waiting for resources
or some other stimulus.

A note on parrelelism: Since python does not provide us with true parallelism, using threading for CPU bound tasks results in a minimal optimization of time.
It is better to use multiprocessing for such tasks as every process has its own GIL and will be allowed to run on different cores

'''
from threading import Thread
from time import sleep

# CASE 1: Creating threads with classes (NON PYTHONIC)


print("-------Threading with classes-------\n")

class Hello(Thread):

  def do(self):
    for i in range(5):
      print("Hello", i+1, "SYNC")

  def run(self):
    # The run method will be run asynchronously when it is called if the class inherits Thread and start() method is run on its object
    for i in range(5):
      print("Hello", i+1, "ASYNC")

class Hi(Thread):
  def do(self):
    for i in range(5):
      print("Hi", i+1, "SYNC")

  def run(self):
    for i in range(5):
      print("Hi", i+1, "ASYNC")

if __name__ == "__main__":
  print() # For formatting sake
  print('An example of Synchronous Execution:\n')
  t1 = Hello() # Creating hello object
  t2= Hi() # Creating hi object

  # Calling do() function on both
  t1.do()
  t2.do()
  # Above, Hello will be printed 5 times, then Hi will be printed 5 times (SYNCHRONOUS EXECUTION)
  print() # For formatting sake
  print('An example of Asynchronous Execution:\n')
  # These will execute asynchronously
  t1.start() # This will run the run() method (Yes, calling start() runs the run() method)
  t2.start()

# CASE 2: Threading with functions (PYTHONIC WAY)

print() # For formatting sake
print("-------Threading with functions-------\n")
 
def hi():
    for i in range(5):
      print("Hi", i+1, "ASYNC")
      sleep(5)

def hello():
    for i in range(5):
      print("Hello", i+1, "ASYNC")
      sleep(5)

def howdy():
    for i in range(5):
      print("Howdy", i+1, "ASYNC")
      sleep(5)

# Intialising threads
tf1 = Thread(target=hi) # You set the target of thread to be the function you want it to execute
tf2 = Thread(target=hello)
tf3 = Thread(target=howdy)

# Starting threads
tf1.start()
tf2.start()
tf3.start()

# Joining threads
tf1.join() # This will wait here until the execution of the t1 thread finishes before proceeding further. 
tf2.join()
tf3.join()

# It is convention to join all threads before finishing an application
# Without these, the main thread could exit before the other threads finish,
# which can cause incomplete execution or messy output


