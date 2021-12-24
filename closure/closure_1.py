# Closures


def customize_msg(msg):
  def inner(name):
    return f'{msg} {name}'

  return inner


hi = customize_msg('Hi')
hello = customize_msg('Hello')

print(hi('frined'))
print(hello('my Lord'))


# ***************************************************
def outer(x):
  num_1 = x

  def inner(y):
    return num_1 + y

  return inner


my_func = outer(10)

print(my_func(20))


# ***************************************************
def html_tag(tag):
  def print_tag(text):
    return '<{0}>{1}</{0}>'.format(tag, text)

  return print_tag


h1_tag = html_tag('h1')
print(h1_tag)

h1_tag = html_tag('h1')
print(h1_tag('This is a headline!'))
