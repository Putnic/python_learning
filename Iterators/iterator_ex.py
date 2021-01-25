# Iterators in Python
# Iterator in python is any python type that can be used with a ‘for in loop’. Python lists, tuples, dicts and sets are all examples of inbuilt iterators.
# These types are iterators because they implement some methods.
# In fact, any object that wants to be an iterator must implement following methods:
# __iter__ method that is called on initialization of an iterator. This should return an object that has a __next__ method.
# __next__ The iterator next method should return the next value for the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() on the iterator object. This method should raise a StopIteration to signal the end of the iteration.


# An iterable user defined type
class MyRange:

  # Cosntructor
  def __init__(self, start, end):
    self.value = start
    self.end = end

  # Called when iteration is initialized
  def __iter__(self):
    return self

  def __next__(self):
    if self.value >= self.end:
      raise StopIteration
    current = self.value
    self.value += 1
    return current


nums = MyRange(1, 5)

for num in nums:
  print(num)


# Generator
# The yield statement suspends function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list.
def my_range(start, end):
  current = start
  # while True:
  while current < end:
    yield current
    current += 1


nums = my_range(1, 5)

for num in nums:
  print(num)