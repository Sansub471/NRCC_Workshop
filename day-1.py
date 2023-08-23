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
print('Tabsize 3:', str.expandtabs(3))
print('Tabsize 4:', str.expandtabs(4))
print('Tabsize 5:', str.expandtabs(5))
print('Tabsize 6:', str.expandtabs(6))

# https://www.programiz.com/python-programming/methods/string/expandtabs
print('\n')

# syntax : string.find(value, start, end)
# value : required value to search for in the string
print(string3.find('banana')) # -1 means not found
print(my_string.find('nepal')) # find the first occurence
print('\n')

# syntax : string.format(value1, value2...)
# The format() method formats the specified value(s) and insert them 
# inside the string's placeholder. The place holder defined by {}
price = 'For only {price:.2f} dollars!'
print(price.format(price=50)) 

txt1 = "My name is {fname}, I'm {age}".format(fname = "Subash", age = 24)
txt2 = "My name is {0}, I'm {1}".format("Subash", 24)
txt3 = "My name is {}, I'm {}".format("Subash", 24)

print(txt1)
print(txt2)
print(txt3)

# Formatting types : https://www.w3schools.com/python/ref_string_format.asp

# syntax: string.index(value, start, end)
# The index() method finds the first occurrence of the specified value.
print(my_string.index('my')) 
# Difference with find is -1 returned by find when not found
# but it raises a ValueError