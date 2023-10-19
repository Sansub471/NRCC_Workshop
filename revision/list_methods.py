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

# I have removed the comment
# This is the new line of comment.


