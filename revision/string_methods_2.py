# syntax : string.partition(value)
# value : first occurence of string to search for

# splits the string into a tuple containing three elements.

# part before the 'value' string, the 'value' string and the part after 
# the 'value' string.

info = "I could eat mangos all day."
print(info.partition('mangos'))
print('\n')

# string.replace(oldvalue, newvalue, count)
# count : how many occurence to replace, default is all.

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

# string.rfind(value, start, end)
# finds the last occurence of the specified value
# returns -1 if the value is not found


x = txt.rfind("one", 8, -1)
print(x)

# string.rindex(value, start, end)
# find the last occurence of the specified value. 
# an exception is raised if not found
x = txt.index("one", 8, -1)
print(x)



