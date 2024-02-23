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
x = txt.rindex("one", 8, -1)
print(x)

# string.rjust(length, character)
# returns the right justified string, space is the default character
txt = 'mango'
print(txt.rjust(20, '#'))

# string.rpartition(value)
# searches the last occurence of specified string, 'value'
# and split the string into a tuple having three elements.
# first : part before the specified string
# second : the specified string
# thirsd : the part after the string

txt = 'nepal is in south asia. nepal is next to india and china, nepal is my home'
print(txt.rpartition('nepal'))

# string.rsplit(separator, maxsplit)
# splits the string into a list, starting from the right
# separator : opt, default is space
# maxsplit : opt, how many splits, default is -1

print("rsplit() function : ")
txt = 'mango, apple, cherry, banana, pineapple, peach'
x = txt.rsplit(',', 2) # max length 2 + 1
print(x) # -1 is all, empty is also all
# If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
print(f'The lenght of split is : {len(x)}')

# string.rstrip(characters)
# remove trailing characters from a string
# characters : opt, default is space, set of characters to remove
txt = "         nepal is my country.    @@@@***$!!!!!%@#"
print(txt.rstrip('@!*$%#'))

# string.split(separator, maxsplit)
# splits a string into a list
txt = "hello, my name is Subash Mainali, I'm currently unemployed right now."
x = txt.split(",", 1) # the list will have maximum of maxsplit + 1 elements
# -1 or empty means all
print(x)