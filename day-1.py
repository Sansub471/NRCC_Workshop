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

# syntax : string.endswith(value, start, end)
# returns true or false
filename = 'computer.jpg'
print(filename.endswith('.jpg'))

ioe = 'https://exam.ioe.edu.np'
print(ioe.endswith('.np'))

# syntax : string.expandtabs(tabsize)
str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))

# https://www.programiz.com/python-programming/methods/string/expandtabs
