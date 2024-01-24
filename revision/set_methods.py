# Revision of set data type in python
fruits = {'banana', 'apple', 'orange', 'banana', 'pear', 'orange'}
print(fruits)

# Elements cannot be repeated in a set

fruits.add('mango')
print(fruits)

fruits.clear() # Remove all elements in the set

prime = {13,2,3,3,5,13,7,11,3,7}
print(prime) # Repeated elements are removed

primeNumbers = prime.copy()
print(primeNumbers)

composite = {4,6,8,9,10,12}
mix = {2,3,4,5,6,7,8,9,12}

# Set difference
print("The difference between sets: ")
diff1 = mix.difference(prime)
print(diff1)

diff2 = mix.difference(composite)
print(diff2)

# set.difference_update(set)
# Removes the intersection elements from the original set, new set not returned.
print("set.difference_update(set)")
mix.difference_update(prime)
print(mix) # prime removed

mix.difference_update(composite)
print(mix) # composite removed

# mix is now empty

# set.union(set1, set2, set3)
newMix = prime.union(composite)
print("Union of prime and coposite: ", newMix)

# set.update(set or iterable)
numbers = [23,21]
print("Before update : ", prime)
prime.update(numbers)
print("Updated prime : ", prime)

