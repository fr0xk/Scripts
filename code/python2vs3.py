# Python 2 vs Python 3 script

# Basic Differences

# Print statement

print "Hello, World!"     # Python 2

print("Hello, World!")   # Python 3

# Division

print 7 / 2              # Python 2 (integer division)

print 7 // 2             # Python 3 (floor division)

# Unicode strings

print type(u"hello")     # Python 2 (unicode string)

print(type("hello"))     # Python 3 (unicode string)

# xrange

for i in xrange(5):      # Python 2

    print i

for i in range(5):       # Python 3

    print(i)

# Advanced Differences

# Exception handling

try:

    # Some code that raises an exception

    raise IOError("An error occurred")

except IOError as e:

    print(e)             # Python 2 and 3 (exception handling syntax is the same)

# Unicode literals

s = "café"

print len(s)             # Python 2 (prints 4)

print(len(s))            # Python 3 (prints 5)

# Function arguments

def foo(a, b, c=0):

    print(a, b, c)

foo(1, 2, 3)             # Python 2 and 3 (prints 1, 2, 3)

foo(1, 2, c=3)           # Python 3 only (prints 1, 2, 3)

# Iteration

items = [1, 2, 3]

for item in items:

    print(item)

else:

    print("Finished")    # Python 2 and 3 (prints "Finished")

# Unicode file names

import io

with io.open("café.txt", "w", encoding="utf-8") as f:

    f.write("Hello, World!")

# Other Differences

# Integer Division

print(7 / 2)             # Python 3 (float division)

print(7 // 2)            # Python 2 (integer division)

# Ordering Comparisons

print(1 < 'a')           # Python 2 (prints True)

# print(1 < 'a')          # Python 3 (throws TypeError)

# Division by zero

print(1 / 0)             # Python 2 (prints "ZeroDivisionError")

# print(1 / 0)            # Python 3 (throws ZeroDivisionError)

# Strings and bytes

s = "hello"

print(type(s))           # Python 2 (prints "str")

print(type(s.encode()))  # Python 3 (prints "bytes")

# Input function

# name = raw_input("What is your name? ")  # Python 2

name = input("What is your name? ")       # Python 3

# Handling exceptions

# raise Exception, "An error occurred"  # Python 2

raise Exception("An error occurred")    # Python 3

# Print function

# print "Hello, World!",   # Python 2

print("Hello, World!", end='')          # Python 3

# xrange vs range

# print xrange(5)          # Python 2

# print range(5)           # Python 3

# Handling of Unicode characters

s = u'Hello, \u0107'

print(s)                 # Python 2 (prints "Hello, ć")

# print(s)                # Python 3 (throws UnicodeEncodeError)

# Byte literals

b = b"hello"

print(b)                

