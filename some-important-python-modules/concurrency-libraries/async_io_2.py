'''

While the first example illustrated an example on how async io works, our second example now will illustrate a means to actually
optimise code using asyncio

While we were using asyncio in our code in the last example, our program was still synchronous in the fact that we waited for task1
to complete before running task2

Here, we will examine the create_task() function and see how it impacts the performance of our code

'''

import asyncio 

async def fetch_data(delay, id):
  print(f"Coroutine with id : {id} is beginning to fetch data")
  await asyncio.sleep(delay)
  return f"Sample data from coroutine {id}"

async def main():

  # Creating tasks allows us to run coroutines concurrently
  # This means that the moment that a coroutine idles on an await operation, another coroutine begins execution
  # Note that these task still don't execute parallely: they share the same cpu core; however when one task idles or waits, we don't let our program idle
  task_1 = asyncio.create_task(fetch_data(2,1)) # We pass coroutine objects to the create_task() function
  task_2 = asyncio.create_task(fetch_data(2,2))
  task_3 = asyncio.create_task(fetch_data(2,3))

  # awaiting tasks for them to start and subsequently finish
  result_1 = await task_1
  result_2 = await task_2
  result_3 = await task_3

  # Another way to do all this in one line of code would be with the gather function
  # THe gather() function takes multiple coroutine objects as arguments an allows us to run multiple tasks concurrently
  # The above tasks will all run concurrently
  # Instead of the above six lines of code we can sy something like: results = await asyncio.gather(fetch_data(2,1), fetch_data(2,2), fetch_data(2,3))
  # it will then gather all their return values in a list
  # We can retrieve them by iterating through said list like below
  '''
  for result in results:
    print(result)
  
  '''
  # However, gather() is not very good at error handling and may still run other coroutines if one fails


  print(result_1)
  print(result_2)
  print(result_3)

asyncio.run(main())
