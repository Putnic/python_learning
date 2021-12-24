class Open_File():

  def __init__(self, destination):
    pass

  def __enter__(self):
    pass

  def __exit__(self, exc_type, exc_val, traceback):
    pass


#### Using contextlib ####
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
  f = open(file, mode)
  yield f
  f.close()


with open_file('sample.txt', 'w') as f:
  f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)
