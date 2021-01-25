
# example is a case of file descriptor leakage
# It happens because there are too many open files and they are not closed. 
file_descriptors = []
for x in range(100000):
  file_descriptors.append(open('test.txt', 'w'))
