# list methods
fruits = ['apple', 'banana', 'mango', 'pear']
print(fruits)
fruits.append('orange')
print(fruits)

# syntax : list.append(element)
# returns None

names = ['nepal', 'china', 'india']
names.clear()
print(names)

fruits1 = fruits.copy()
print(fruits1)

# syntax : list.count(value)
fruits.append('apple')
fruits.append('apple')
print(fruits)
# The count() method returns the number of elements with the specified value.
print(fruits.count('apple'))
print('\n')

# syntax : list.extend(iterable)
# any iterable, list, set, tuple, etc.
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
points = (1,4,7,8)
fruits.extend(points)
print(fruits)

fruits.extend('nepal')
print(fruits)

