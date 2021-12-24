import random
import time
from typing import List
import mem_profile

__debug__
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
  result = []
  for i in range(num_people):
    person = {
        'id': i,
        'name': random.choice(names),
        'major': random.choice(majors)
    }
    result.append(person)
  return result


def people_generator(num_people):
  for i in range(num_people):
    person = {
        'id': i,
        'name': random.choice(names),
        'major': random.choice(majors)
    }
    yield person


print('\npeople_list')
print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

# Start the stopwatch / counter
t1_start = time.perf_counter()
peoples = people_list(1000000)
t1_stop = time.perf_counter()

print('Took {} Seconds'.format(t1_stop - t1_start))
print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))

###########################################
print('\npeople_generator')
print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

# Start the stopwatch / counter
t1_start = time.perf_counter()
people_gen = people_generator(1000000)
t1_stop = time.perf_counter()

print('Took {} Seconds'.format(t1_stop - t1_start))
print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))

###########################################
print("\nlet's go through the whole generator people_generator")
print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

# Start the stopwatch / counter
t1_start = time.perf_counter()
for people in people_gen:
  pass
t1_stop = time.perf_counter()

print('Took {} Seconds'.format(t1_stop - t1_start))
print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))