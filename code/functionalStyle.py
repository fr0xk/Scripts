import operator

from itertools import starmap, product

from functools import reduce

data = [1, 2, 3, 4, 5]

squares = list(starmap(operator.mul, product(data, repeat=2)))

evens = list(filter(lambda x: x % 2 == 0, data))

odds = list(filter(lambda x: x % 2 != 0, data))

product = reduce(lambda x, y: x * y, data)

print("Squares:", squares)

print("Evens:", evens)

print("Odds:", odds)

print("Product:", product)

