# Let's have a look into set methods
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
fruits.add('orange')
print(fruits)
print('')

fruits.clear() # removes all elements in a set
print(fruits)


fruits1 = {'mango', 'banana', 'pear', 'kiwi'}
fp = fruits.copy()
print(fp)

# set.difference(set)
# set : the set to check the difference in
# the returned set contains items that exists only in the first set,
# and not in both sets.
fruits = {'apple', 'banana', 'cherry'}
x = fruits.difference(fruits1)
print(x)

x = fruits1.difference(fruits)
print(x)
print('')

# set.difference_update(set)
# removes the items that exist in both sets
# new set not returned, items removed from original set 
fruits1.difference_update(fruits)
print(fruits1)

# set.discard(value)
# value : the item to search for and remove
# removes the specified item form the set
fruits.discard('cherry')
print(fruits)


# set.intersection(set1, set2, set3, ...)
# returns a new set
plate1 = {'rice','dal', 'vegetables', 'chicken', 'fish', 'mutton'}
plate2 = {'rice', 'dal', 'mutton', 'vegetables'}
plate3 = {'dal', 'vegetables', 'rice', 'fish'}
common  = plate1.intersection(plate2, plate3)
print(common)

# set.intersetion_update(set1, set2, ...)
# removes the item that is not present in both sets (or in all sets )
# items removed from original set
plate3.intersection_update(plate2, plate1)
print(plate3)
