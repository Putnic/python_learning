import asyncio


async def main():
  print('hello')
  await asyncio.sleep(1)
  print('world')


# asyncio.run(main())

# ******************************************
# Awaiting on a coroutine. The following snippet of code will print “hello” after waiting for 1 second, and then print “world” after waiting for another 2 seconds:
import time


async def say_after(delay, what):
  await asyncio.sleep(delay)
  print(what)


async def main_1():
  print(f"started at {time.strftime('%X')}")

  # first will be executed, then the second
  await say_after(1, 'hello')
  await say_after(2, 'world')

  print(f"finished at {time.strftime('%X')}")


# asyncio.run(main_1())


# *****************************************
# The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# Let’s modify the above example and run two say_after coroutines concurrently:
# Note that expected output now shows that the snippet runs 1 second faster than before:
async def main_2():
  task1 = asyncio.create_task(say_after(1, 'hello'))

  task2 = asyncio.create_task(say_after(2, 'world'))

  print(f"started at {time.strftime('%X')}")

  # Wait until both tasks are completed (should take
  # around 2 seconds.)
  await task1
  await task2

  print(f"finished at {time.strftime('%X')}")


# **************************************
# Object is an awaitable object if it can be used in an await expression.
# There are three main types of awaitable objects: coroutines, Tasks, and Futures.
# Coroutines
# Python coroutines are awaitables and therefore can be awaited from other coroutines:
async def nested():
  return 42


async def main_3():
  # Nothing happens if we just call "nested()".
  # A coroutine object is created but not awaited,
  # so it *won't run at all*.
  nested()

  # Let's do it differently now and await it:
  print(await nested())  # will print "42".


# asyncio.run(main_3())


# *********************************************
# Tasks
# Tasks are used to schedule coroutines concurrently.
# When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:
async def nested_4():
  return 42


async def main_4():
  # Schedule nested() to run soon concurrently
  # with "main()".
  task = asyncio.create_task(nested_4())

  # "task" can now be used to cancel "nested()", or
  # can simply be awaited to wait until it is complete:
  print(await task)


# asyncio.run(main_4())


# ********************************
# Futures
# A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.
# When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.
async def function_that_returns_a_future_object():
  await asyncio.sleep(1)
  print('I promise to give results in the future')


async def some_python_coroutine():
  await asyncio.sleep(2)
  print('I also promise to give results in the future')


async def main_5():
  print(f"started at {time.strftime('%X')}")
  await function_that_returns_a_future_object()
  print(f"finished at {time.strftime('%X')}")

  print(f"started at {time.strftime('%X')}")
  # this is also valid:
  await asyncio.gather(function_that_returns_a_future_object(), some_python_coroutine())
  print(f"finished at {time.strftime('%X')}")


# ***********************************
# Example of coroutine displaying the current date every second for 5 seconds:
import datetime


async def display_date():
  loop = asyncio.get_running_loop()
  end_time = loop.time() + 5.0
  while True:
    print(datetime.datetime.now())
    print(f"Time: {time.strftime('%X')}")
    if (loop.time() + 1.0) >= end_time:
      break
    await asyncio.sleep(1)


# asyncio.run(display_date())


# **********************************************
async def factorial(name, number):
  f = 1
  for i in range(2, number + 1):
    print(f"Task {name}: Compute factorial({i})...")
    await asyncio.sleep(1)
    f *= i
  print(f"Task {name}: factorial({number}) = {f}")


async def main_6():
  # Schedule three calls *concurrently*:
  await asyncio.gather(
      factorial("A", 2),
      factorial("B", 3),
      factorial("C", 4),
  )


# asyncio.run(main_6())