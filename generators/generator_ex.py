from sys import getsizeof
from typing import List

# Generator Expressions
gen_exp = (x * x for x in [1, 2, 3, 4, 5])

print('Generator Expressions', gen_exp)
print('gen_exp:', getsizeof(gen_exp))

# gen_exp = (x * x for x in [1, 2, 3, 4, 5])

# [1, 4, 9, 16, 25]
# print(list(gen_exp))


# ****************************************************
# Generator
# Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
# A generator function
def simpleGeneratorFun():
  yield 1
  yield 2
  yield 3


for value in simpleGeneratorFun():
  print(value)


def square_numbers(nums: List[int | float]):
  for i in nums:
    yield (i * i)


# Generator-Object : Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).

# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(next(x))
print(x.__next__())
print(x.__next__())

#################################################
gen = square_numbers([1, 2, 3, 4, 5])
print('generator: ', gen)
print('gen:', getsizeof(gen))

# calculate at each iteration
for num in gen:
  print(num)


# **************************************************
# several yields
def testgen(index: int):
  weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
  yield weekdays[index]
  yield weekdays[index + 1]
  return 'End'


day = testgen(0)

# print(next(day))