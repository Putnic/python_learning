import psutil
import os


def memory_usage_psutil():
  # return the memory usage in MB
  process = psutil.Process(os.getpid())
  mem = process.memory_info()[0] / 2**20
  return mem


# ***************************************************
# Unix
# import resource
# import sys

# def memory_usage_resource():
#   rusage_denom = 1024.
#   if sys.platform == 'darwin':
#     # ... it seems that in OSX the output is different units ...
#     rusage_denom = rusage_denom * rusage_denom
#   mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
#   return mem
