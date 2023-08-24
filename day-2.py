# This is the second part of string functions
# syntax : string.partition(value)
# value : The string to search for.
# The partition() method searches for a specified string, and splits 
# the string into a tuple containing three elements.
# This method searches for the first occurence of the specified string.

# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.

info = 'I could eat bananas all day.'
print(info.partition('bananas'))
print('\n')

# syntax : string.replace(oldvalue, newvalue, count)
# count : how many occurences to replace, default is all.

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

print(txt.replace('one', 'ten'))
print('\n')