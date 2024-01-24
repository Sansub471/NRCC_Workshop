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

# set.discard(value)
# Remove the value from the set, no error if not found in the set

print("Before discarding 7 : ", prime)
prime.discard(7)
print("After discarding 7 : ", prime)
print("\n")

# set.intersection(set1, set2, ...) returns a new set
tens = {10,20,30,40,50,60}
fives = {5,15,25,35,45,90,20,30,40}
multiples = {5,10,30,40}
newSet = multiples.intersection(tens, fives)
print("Intersection : ", newSet)
print("\n")

# set.isdisjoint(set) True or false
answer = prime.isdisjoint(composite)
print(f"Is {prime} and {composite} disjoint? : {answer}\n")

# set.issubset(set)
num1 = {1,2,3,4,5,6}
num2 = {1,4,6}
print(f'Is {num2} subset of {num1}? : {num2.issubset(num1)}\n')

# Return True if all items in set x are present in set y:

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# z = x.issubset(y)

# print(z)

# set.issuperset(set)
print(f'Is {num1} superset of {num2}? : {num1.issuperset(num2)}\n')


# set.pop() Remove a random item
# Popped item is returned
print(f"Set {num1}, poped item: {num1.pop()}\n")
print(f"Set {num1}, poped item: {num1.pop()}\n")


# set.remove(item)
# raise an erroe if the item is not found

# set.symmetric_difference(set)
# All items excet the intesection items between two sets.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
result = A.symmetric_difference(B)
print(result)


# set.symmetric_difference_update()
# method updates the original set by removing items that are present 
# in both sets, and inserting the other items.
x = {"apple", "banana", "cherry", "yahoo"}
y = {"google", "microsoft", "apple", "yahoo", "oracle"}
x.symmetric_difference_update(y)
print(x)

# set.union(set1, set2, set3)
newMix = prime.union(composite)
print("Union of prime and coposite: ", newMix)

# set.update(set or iterable)
numbers = [23,21]
print("Before update : ", prime)
prime.update(numbers)
print("Updated prime : ", prime)

