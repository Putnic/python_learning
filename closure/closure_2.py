# Closures
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
  def log_func(*args):
    logging.info('Running function "{}" with arguments {}'.format(func.__name__, args))
    print(func(*args))

  return log_func


def add(x, y):
  return x + y


def multiply(x, y):
  return x - y


add_logger = logger(add)
multiply_logger = logger(multiply)

add_logger(3, 3)
add_logger(4, 5)

multiply_logger(10, 5)
multiply_logger(20, 10)
