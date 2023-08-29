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