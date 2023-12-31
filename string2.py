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

# syntax : string.rfind(value, start, end)
#  finds the last occurrence of the specified value.
# returns -1 if the value is not found.

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10) # try changing start and end values
print(x)

# syntax  : string.rindex(value, start, end)
#The rindex() method finds the last occurrence of the specified value.
#The rindex() method raises an exception if the value is not found.

txt = 'nepali are good people'
print(txt.rindex("l"))
print('\n')

# syntax : string.rjust(length, character)
# returns the right justified string, space character is default

txt = 'mango'
print(txt.rjust(20, '*'))

# syntax : string.rpartition(value)
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.

txt = 'nepa is in south asia, nepal is next to india, nepal is my home'
print(txt.rpartition('nepal'))

# syntax: string.rsplit(separator, maxsplit)
# The rsplit() method splits a string into a list, starting from the right.
# separator : opt, default is space
# maxsplit : opt, how many splits, default is -1 all

txt = 'mango, apple, cherry, banana, pineapple'
print(txt.rsplit(',')) # -1 all, empty is also all

# syntax : string.rstrip(characters)
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# characters : opt, set of characters to remove as trailing characters

txt = "     nepal is my country   **********    "
print(txt.rstrip('*'))
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(".wsq,") # look at it carefully
print(x)
print('\n')

# syntax : string.split(separator, maxsplit)
# The split() method splits a string into a list.
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ", 1)
print(x)

# syntax : string.splitlines(keeplinebreaks)
# keeplinebreaks : opt, bool, default false, '\n' keep in list or not

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

print(txt.splitlines(False))
# observe the difference

# syntax : string.startswith(value, start, end)
# value required, others optional, default value is all string

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
print('\n')

# syntax : string.strip(characters)
# characters : to be removed
# The strip() method removes any leading, and trailing whitespaces.
# or the character specified
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",grt.")
print(x)
print('\n')

# syntax : string.swapcase()
# upper case letters to lower case and vice versa
txt = 'STRLgtkSpiron177'
print(txt.swapcase())

# syntax : string.title()
# returns a string where first character in each word is capitalized
txt = 'welcome to nepal'
print(txt.title())

# syntax : string.upper()
print(txt.upper())

# syntax : string.zfill(len)
# desired length of the string
# adds zeros (0) at the beginning of the string, until it reaches the specified length.
print(txt.zfill(20))

# Note : All string methods returns new values. They do not change the original string.
