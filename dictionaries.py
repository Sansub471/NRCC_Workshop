# syntax : dictionary.clear()
# removes all the elements from a dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car.clear()
print(car)

# syntax  : dictionary.copy()
# returns a copy of the specified dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)

# syntax : dict.fromkeys(keys, value)
# keys : an iterable specifying the keys of the new dictionary
# value : opt, the value for all keys, default is None

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)
print('\n')

# with values
values = [12, 45, 'Nepal']
thisdict = dict.fromkeys(x, values)
print(thisdict)
print('\n')

# another
values = 'Nepal'
thisdict = dict.fromkeys(x, values)
print(thisdict)
