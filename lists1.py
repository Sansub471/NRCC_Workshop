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
names.extend(points)
print(names)

names.extend('nepal')
print(names)

# syntax : list.index(element)
# element: string, number, list, etc.
# returns position at the first occurence of the specified value
print(fruits.index('pear'))
print('\n')

# syntax : list.insert(pos, element)
print(fruits)
fruits.insert(1, 'pineapple')
print(fruits)
print('\n')

# syntax : list.pop(pos)
# removes an element at specified position
fruits.pop(2) # index 2, pos starts from zero
print(fruits)

# syntax  : list.remove(element)
# string, number, list, etc.
# removes the first occurence of the element with the specified value
fruits.remove('pear')
print(fruits)

# syntax : list.reverse()
fruits.reverse()
print(fruits)
print('\n')

# syntax : list.sort(reverse=True|False, key=myFunc)
# reverse : opt, True means descending and False means ascending
# default is False
# key : a functino to specify sorting criteria
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print(cars)
cars.sort(reverse=True, key=myFunc)
print(cars)

# Python does not have built-in support for Arrays, but Python Lists can be used instead.