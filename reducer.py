import operator
from functools import reduce

# def reducer(arr, operator):
#   if operator == "*":
#     print(reduce((lambda x, y: x * y), arr))
#   elif operator == "/":
#     print(reduce((lambda x, y: x / y), arr))
#   elif operator == "+":
#     print(reduce((lambda x, y: x + y), arr))
#   elif operator == "-":
#     print(reduce((lambda x, y: x - y), arr))


def reducer(collection, op):
  operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
  }
  return reduce((lambda total, element: operators[op](total, element)), collection)

print(reducer([1,2,3], "+"))
print(reducer([1,2,3], "-"))
print(reducer([1,2,3], "*"))
print(reducer([1,2,3], "/"))