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
