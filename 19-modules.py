#modules
import sys
print(sys.path)

import re
text = 'Mi number 311, el codigo es 54, mi numero de la suerte es 2'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections
numbers = [1,1,1,1,2,3,3,4,5]
counter = collections.Counter(numbers)
print(counter)