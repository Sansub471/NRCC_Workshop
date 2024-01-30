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
