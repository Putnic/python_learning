class ContextManager(object):

  def __init__(self):
    print('__init__ method called')

  def __enter__(self):
    print('__enter__ method called')
    return self

  def __exit__(self, type, value, traceback):
    print(
        f'__exit__ method called: \ntype: {type} \nvalue: {value} \ntraceback: {traceback}'
    )
    return True  # suppress the exception

  def __del__(self):
    print('__del__ method called', self)


with ContextManager() as c:
  print('Doing something with c:', c)
  raise RuntimeError()

print('Completing the action')

print('Done')