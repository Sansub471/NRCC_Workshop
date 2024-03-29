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
print('\n')

# syntax : dictionary.get(keyname, value)
# keyname : the keyname of the item you want to return the value from
# value : opt, a value to return if the specified key doesn't exist
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

# if the item doesn't exist
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)
print(x)
print('\n')

# syntax : dictionary.items()
# return view object. The view object contains the key-value pairs of the 
# dictionary, as tuples in a list
# The view object will reflect any changes done to the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)
print(type(x))

# When an item in the dictionary changes value, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
car["year"] = 2018
print(x)
print('\n')

# syntax : dictionary.keys()
# returns a view object, which contains the keys of the dictionary as a list

# When an item is added in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)
car["color"] = "white"
print(x)
print('\n')

# syntax : dictionary.pop(keyname, defaultvalue)
# removes the specified item from the dictionary
# the value of the removed item is the return value of the pop()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
x = car.pop("model")
print(x)
print(car)
print('\n')

# syntax : dictionary.popitem()
# removes the item that was last inserted into the dictionary
# poped item returned as tuple, key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
x = car.popitem()
print(x) # 
print(car)

# syntax : dictionary.setdefault(keyname, value)
# returns the value of the item with the specified key.
# keyname : the keyname item to return the value from
# value : if keyname doesn't exist, it becomes the 
# default value otherwise None is default.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)

x = car.setdefault("brand", "Tesla")
print(x)
print('\n')

# syntax : dictionary.update(iterable)
# any iterable object with key value pairs, will be inserted to the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

car.update([('country', 'Nepal'), ('price', '450K')])
print(car)

# syntax : dictionary.values()
# returns the list of all the values in the dictionary
# the returned value is a view object
x = car.values()
print(x)

# When a values is changed in the dictionary, the view object also gets updated:
x = car.values()
car["year"] = 2018
print(x)
