# Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process voluntarily yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously. The difference between coroutine and subroutine is :
# Unlike subroutines, coroutines have many entry points for suspending and resuming execution. Coroutine can suspend its execution and transfer control to other coroutine and can resume again execution from the point it left off.
# Unlike subroutines, there is no main function to call coroutines in particular order and coordinate the results. Coroutines are cooperative that means they link together to form a pipeline. One coroutine may consume input data and send it to other which process it. Finally there may be a coroutine to display result.


# Python3 program for demonstrating
# closing a coroutine
def np(prefix):
  print("Searching prefix:{}".format(prefix))
  try:
    while True:
      print('Before')
      name = yield prefix
      print('After')
      if prefix in name:
        print(name)
  except GeneratorExit:
    print("Closing coroutine!!")


cc = np('Dear')

#  cc.send(None) or next(cc)
# cc.__next__()
# cc.send("Artur")
# cc.send("Dear Artur")
# cc.close()


# ************************************************
# Python3 program for demonstrating
# coroutine chaining
def producer(sentence, next_coroutine):
  ''' 
	Producer which just split strings and 
	feed it to pattern_filter coroutine 
	'''
  tokens = sentence.split(" ")
  for token in tokens:
    next_coroutine.send(token)
  next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
  ''' 
	Search for pattern in received token 
	and if pattern got matched, send it to 
	print_token() coroutine for printing 
	'''
  print("Searching for {}".format(pattern))
  try:
    while True:
      token = (yield)
      if pattern in token:
        next_coroutine.send(token)
  except GeneratorExit:
    print("Done with filtering!!")
    next_coroutine.close()


def print_token():
  ''' 
	Simply print the received tokens 
	'''
  print("I'll print tokens")
  try:
    while True:
      token = (yield)
      print(token)
  except GeneratorExit:
    print("Done with printing!")


pt = print_token()
# pt.__next__()
# pf = pattern_filter(next_coroutine=pt)
# pf.__next__()

sentence = "Bob is running behind a fast moving car"
# producer(sentence, pf)
