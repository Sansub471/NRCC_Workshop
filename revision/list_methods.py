names = ['apple', 'banana', 'coconut', 'grapes']
print(names)
names.append('mango')
print(names)
fruits = ['banana', 'cherry']
names.extend(fruits)
print(names)
print(names.count('apple'))

print(names.index('grapes'))

print(names.insert(2, 'mulberry'))
print(names)

print(names.pop(3)) # removes the item at position and returns it 

names.reverse()
print(names)

def sort_func(elem):
    return len(elem)

names.sort(reverse=False, key=sort_func)
print(names)

# Make a list of list methods: 
# list.append() Add an element at the last
# list.extend(iterable)

print("Trying this from memory : ")

list1 = ['apple','oranges','mango']
list2 = ['banana', 'papaya', 'pear']
list1.extend(list2)
print(list1)


# list.insert(index, element)
# list.index(element) Find the index of first occurence of the element.
print(list1.index('pear'))

# list.reverse() Reverse a given list.
# list.sort(reverse=True/False, key=sort_logic) # sort logic is function, pass it, don't execute it.

def sort_logic(elem):
    return elem[0]

list1.sort(reverse=False, key=sort_logic)
print(list1)


