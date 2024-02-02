# Revisoin of dictionaries
# dict.clear() removes all the elements from the dictionary
# dict.copy() make a copy of the dictionary

# dict.fromkeys(keys, value)
# keys : an iterable specyfing the keys of the new dictionary
# value : opt, the value for all keys, default is None

country = 'NEPAL'
values = [13, 7, 77]
countryDict = dict.fromkeys(country, values)
print(countryDict)

keys = ('k1', 'k2')
keysDict = dict.fromkeys(keys, values)
print(keysDict)

names = ['orange', 'banana', 'mango']
namesDict = dict.fromkeys(names) # value for each key will be None
print(namesDict)
print("\n")

# syntax : dictionary.get(keyname, value)
# keyname : the keyname of the item you want to return the valur from
# value : optional, a value to return if the specified key doesn't exist
# returned None is key not found and no value is given

car = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year'  : 2000
}

x = car.get('brand')
print(x)

x = car.get('price')
print(x)

x = car.get('price', 40000)
print(x)

# syntax : dictionary.items()
# returns view object. The view object contains key-value pairs of the 
# dictionary as tuples in a list.
# The view object will reflect any changes done to the dictionary.

x = car.items()
print(x)
print(type(x))

# dictionary.keys()
# returns a view object, which contains the keys of the dictionary as a list
# When an item is added in the dictionary, the view object also gets updated.
y = car.keys()
print(y)

car['price'] = 45000 # New key added
print(y) # view object is also updated.

# dictionary.pop(keyname, defaultvalue)
# remove the specified item from the dictionary
# returns: the value of the removed item.

z = car.pop('price')
print(car)

# dictionary.popitem()
# removes the item that was inserted last into the dictionary
# returns : key, value pair of the removed item.
car['price'] = 45000
print(f'Checking the popitem function : {car}')
z = car.popitem()
print(car)
print(z)

# dictionary.setdefault(keyname, value)
# returns the value of the item with the specified key.
# keyname : the keyname item to return the value from
# value : if keyname doesn't exist, it becomes the 
# default value otherwise None is default
print("setdefault method :")
print(car)
x = car.setdefault("brand", "Tesla")
print(x)

x = car.setdefault("price", 50000)
print(x)


# dictionary.update(iterable)
# Any iterable with key value pairs, will be inserted
# to the dictionary
print("Dictionary update:")
iter1 = {'color' : 'White'}
iter2 = [('country', 'USA'), ('type', 'EV')]
car.update(iter1)
print(car)
car.update(iter2)
print(car)

# dictionary.values()
# returns the list of all the values of the dictionary
# the returned value is a view object

print("Dictionary values")
x = car.values() # view object
car['availability'] = 'No'
print(x)





