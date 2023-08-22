# Revison of string methods

my_string = "nepal is my country."
print(my_string.capitalize()) # Converts the first character to upper case

name = 'Subash'
print(my_string.casefold()) # converts string into lower case
print(name.casefold())

# string.center(length, character)
# length : The length of the required string
# character: optional, the character to fill the missing space on each side
# The center() method will center align the string, 
# using a specified character (space is default) as the fill character.

print(name.center(20, '*'))

# The count() method returns the number of times a specified 
# value appears in the string.
# syntax : string.count(value, start, end)
# value : the string to value to search for
# start : opt, pos. to start search
# end : opt, pos. to end search

string2 = 'apple is always apple, it is not mango'
print(string2.count('a', 5, 16))
print(string2.count('apple'))

with open('data.txt', 'r') as fp:
    string3 = fp.readlines()
    string3 = ''.join(string3)

print(f'The word apple in the following paragraph : \n {string3}\n')
print(string3.count('apple'))
print('\n')

# syntax : string.encode(encoding=encoding, errors = errors)
string4 = 'nepal'
print(string4.encode(encoding="ascii"))
txt = "My name is Ståle"
#txt = 'यो नेपाल हो।'
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
# https://www.w3schools.com/python/ref_string_encode.asp
