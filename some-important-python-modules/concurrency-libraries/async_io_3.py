'''
This section of my notes on asyncio covers TaskGroups()

These are another fundamental aspect of using asyncio and provide better error and exception handling 

We do this with the help of an async context manager
'''

import asyncio

async def fetch_data(delay, id):
  print(f"Coroutine with id : {id} is beginning to fetch data")
  await asyncio.sleep(delay)
  return f"Sample data from corutine {id}"

async def main():
  tasks = []

  async with asyncio.TaskGroup() as tg:
    # async with works exactly like with, but the setup and cleanup can be awaited
    # This means that if setup and cleanup take time, your program will not idle
    # instead, other tasks will be executed
    # The same can be said about async for
    # If the next iterable in the sequence cannot be immediately accessed and requires waiting
    # async for allows other tasks to be executed while it waits

    # enumerate() wraps any iterable and yields (index, value) pairs as you loop. Instead of manually tracking a counter, you get both the position and the item together
    for delay, id in enumerate([2, 1, 3], start=1):
      task = tg.create_task(fetch_data(delay, id)) # creating tasks within the task group
      tasks.append(task)

  # After the Task Group block, all tasks have completed
  results = [task.result() for task in tasks]

  for result in results:
    print(f" Received result: {result}")