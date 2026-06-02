'''
As discussed in the notes in 7_threading.py in advanced python, Asynchronous programming provides us with multiple advantages.

The main reason to use asynchronous programming is that it helps us reduce the runtime of our programs by allowing us to do
multiple things concurrently (at the same time)

If we were using one synchronous program, we might have parts of our program that are wating for a resource or I/O (we call this EVENT WAIT)
and instead of letting our program idle, we would make more efficient use of our time if we could accomplish something else

There are three ways to do asynchronous programming in Python:

(i) using THREADS - threads are lightweight subprocesses that share data. These are useful for parallel tasks that don't demand much of the CPU
and share data. Python doesn't allow threads within the same program to access the CPU cores at the same time due to something known as
the GIL (Global Interpreter Lock), so they are a bad way of running multiple CPU bound tasks at the same time

(ii) using MULTIPROCESSING - if we have multiple CPU bound tasks that we want to accomplish at the same time, it is best to allot a separate
process for each of them. This way, they can access different cores of the CPU at the same time without having to worry about the GIL

(iii) using ASYNCIO -
'''