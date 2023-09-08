# syntax : tuple.count(value)
# value : the item to search for
# returns the number of times a specified value appears in the tuple.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 6, 7)
x = numbers.count(7)
print(x)

# syntax : tuple.index(value)
# finds the first occurence of the specified value
# raise exception if the value is not found.
x = numbers.index(8)
print(x)

# x = numbers.index(20) # Exception
# print(x)
# tuple file closed.
