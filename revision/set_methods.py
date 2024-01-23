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