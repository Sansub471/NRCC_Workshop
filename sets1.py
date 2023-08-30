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
# error not raised if not found
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

# set.isdisjoint(set)
# returns True or False
z = fruits.isdisjoint(fruits1)
print(z)

# set.issubset(set)
# set : the set to search for equal items in 
z = plate1.issubset(plate2)
print(z)

# set.issuperset(set)
z = plate1.issuperset(plate2)
# returns True if all items in the specified set exists in the original
# set, otherwise it returns False
print(z)
print('')

# set.pop()
# removes a random item from the set
print(fruits)
y = fruits.pop()
print(y)
print(fruits)

# set.remove(item)
# removes the specified element from the set
# raises an error if not found
print(plate3)
plate3.remove('dal')
print(plate3)
print('')

# set.symmetric_difference(set)
# returns a set that contains all items from both set, but not the items
# that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print('')

# set.symmetric_difference_update(set)
# method updates the original set by removing items that are present 
# in both sets, and inserting the other items.
x = {"apple", "banana", "cherry", "yahoo"}
y = {"google", "microsoft", "apple", "yahoo", "oracle"}
x.symmetric_difference_update(y)
print(x)
print('')