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

(iii) using ASYNCIO - When you are managing multiple WAITING TASKS. This is a library that should be imported and is used widely in FastAPI

USING ASYNCIO

TO understand how ASYNCIO, one must first understand its EVENT LOOP. This is the core aspect of how ASYNCIO works

The EVENT LOOP in asyncio is essentially a schedule that managaes all the ASYNCHRONOUS TASKS and how they run.
It does this via multitasking in a single thread rather than running multiple concurrent threads.
Tasks that are waiting for a resource yield to waiting tasks through await.

'''
# EXAMPLES are taken from TechWithTim's video on asyncio

import asyncio # To use the functionality of asyncio, we must first import it

# COROUTINE FUNCTION
async def main(): 
  print("Start of main coroutine")
  task1 = fetch(2, 1)
  task2 = fetch(3, 2)
  # await the fetch routine, pausing the execution of main until fetch (task1) completes
  # Note here that execution of task1 als only starts after the below line as in asyncio coroutines have to be awaited before they can begin to run
  result1 = await task1 # Holds the return value of the first run coroutine 
  print(f"Received result: {result1}")

  result2 = await task2
  print(f"Received result: {result2}")

  print("End of main coroutine")

# Another coroutine
async def fetch(delay, id):
  print("Fetching data...")
  await asyncio.sleep(delay) # Simulate an I/O operation with sleep
  print("Data fetched")
  return {"Result id" : f"{id}"} # Return some data


# Running the main coroutine
# Here, asyncio.run() will run a coroutine. We pass main() which is a coroutine object
# The below code will also start the event loop
asyncio.run(main()) 

# We can't simply run the coroutine object by typing main() as this is a coroutine object
# When using asyncio, a coroutine needs to be "awaited" for it to run BE AWAITED BEFORE IT CAN BE RUN
 