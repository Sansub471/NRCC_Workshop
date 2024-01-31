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

