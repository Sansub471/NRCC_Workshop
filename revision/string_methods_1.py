# Revision of string methods
my_string = "nepal is my country"
# string.capitalize() # Converts the first character to upper case
# string.casefold() # Converts string into lower case

country = 'NEPAL'
print(country)
print(country.casefold())
# string.center(length, character)
# length : the length of the required string
# character : opt, the character to fill the missing space on each side 
# using a specified character (default space) as the fill character
print(country.center(20, '*'))

# string.count(value, start, end)
print("string.count(value, start, end) : ")
print(country.count('N'))
print(my_string.count('y', 5))

# string.encode(encoding=encoding, errors = errors)

# string.endswith(value, start, end)
# returns true or false
ioe = 'https:://exam.ioe.edu.np'
tu = 'https:://tu.exam.edu.np'
print("string.endswith(value, start, end)")
print(ioe.endswith('.np'))
print(tu.endswith('.np'))

# string.find(value, start, end)
# value : required value to search for in the string. -1 means not found
my_string2 = 'Nepal is a small country in South Asia between two giants China and India.'
print("string.find(value, start, end) function : ")
print(my_string2.find('America')) # not found means -1
print(my_string2.find('China')) # finds the first occurence

# string.find(value, start, end)
# value : required value to search for in the string. -1 means not found
my_string2 = 'Nepal is a small country in South Asia between two giants China and India.'
print("string.find(value, start, end) function : ")
print(my_string2.find('America')) # not found means -1
print(my_string2.find('China')) # finds the first occurence

# syntax : string.format(value1, value2, ..)
# the format() method formats the specified value(s) and insert them 
# inside the string's placeholder. The place holder defined by {}
price = 'For only {p:.2f} dollars!'
print(price.format(p=50))

txt1 = "My name is {fname}, I'm {age}".format(fname = "Subash", age = 24)
txt2 = "My name is {0}, I'm {1}".format("Subash", 24)
txt3 = "My name is {}, I'm {}".format("Subash", 24)

print(txt1)
print(txt2)
print(txt3)

# Formatting types : https://www.w3schools.com/python/ref_string_format.asp

# string.index(value, start, end)
# Difference with find is -1 returned by find when not found 
# but is raises a ValueError
print('\n')
print(txt1.index('Subash', 10))

# string.isalnum()
# returns true is all characters are alpha numeric
txt = 'STRL8908jk'
print(txt.isalnum())
print('\n')

# Other similar methods
# string.isascii()
# string.isdecimal()
# string.isdigit()

# string.isidentifier()
# is alphanumeric and _ character only allowed.

# string.islower() True if all lowercase
# string.isnumeric()

# Python treats mathematical characters like numbers, subscripts, 
# superscripts, and characters having Unicode numeric value properties 
# (like a fraction, roman numerals, currency numerators) as numeric 
# characters.

# Example : 
print("string.isnumeric() function : ")
# string with superscript 
superscript_string = '²3455'
print(superscript_string.isnumeric())

# string with fraction value 
fraction_string = '½123'
print(fraction_string.isnumeric())

# -1 and 1.5 are not numeric because they have - and . which are not numeric.

# string.isprintable()
# True is all characters are printable, otherwise False
# Characters that occupy printing space on the screen are known as 
# printable characters. 
# For example letters and symbols, digits, punctuation, whitespace
# Characters that do not occupy a space and are used for formatting is 
# known as non-printable characters. For example line breaks, page breaks

# string.istitle()
# The istitle() method returns True if all words in a text start with a upper case letter, 
# AND the rest of the word are lower case letters, otherwise False.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
print('\n')

# string.isupper()
# True if all the characters are uppper case

## IMP 
print("string.join(iterables)")
## string.join(iterables)
# Converts elements of an iterable into a string.
fruits = ['banana', 'apple']
cars = {'T' : 'Tesla', 'A' : 'Audi'}
foods = ('burger', 'pizza')
country = 'NEPAL'
my_separator = '--'
x = my_separator.join(fruits)
print(x)
x = my_separator.join(cars)
print(x)
x = my_separator.join(foods)
print(x)
x = my_separator.join(country)
print(x)

print('\n')

# string.ljust(length, character)
# left align the string using a specified character
# space is the default fill character

name = 'Subash'
print(name.ljust(20, '%'))

# string.lower()
# converts a string to lower case

# string.lstrip()
# removes any leading characters (space is the default leading characters
#  to remove)

txt = ",,,,,ssaawwfgk...mango..banana"
x = txt.lstrip(",saw.") # characters to remove given
print(x)
print('\n')

print("string.maketrans(): ")
# Make trans function 
# string.maketrans(x, y, z)
# x : must be a dictionary if only this parameter is given otherwise a string.
# y : opt, string with same length as x, each character in the first parameter
# will be replaced with the corresponding character in this string.

# z : opt, a string describing which character to remove from the orignial string.

# Create a mapping table, and use it in the translate() method to replace any 
# "S" characters with a "P" characters

# The maketrans() method returns a translation table with a 1-to-1 mapping of a 
# Unicode ordinal to its translation/replacement.

txt = "Hello Subash!"
mytable = str.maketrans("S", "P") # create a mapping to replace "S" with "P"
print(mytable)
print(txt.translate(mytable)) # translate fuction applies it.

# create map with a dictionary
# The dictionary should contain a 1-to-1 mapping from a single character string to its 
# translation OR a Unicode number (97 for 'a') to its translation.
mapping = {'a':'NEPAL', 'b':'CHINA', 'c':'INDIA'}
mytable = str.maketrans(mapping)
print(mytable)

countries = 'a-b-c'
countries = countries.translate(mytable)
print(countries)

# passing x and y, both must be string of equal length
first = 'abc'
second = 'NCI'
mytable = str.maketrans(first, second)
print(mytable)

ctrs = 'a-b-c'
print(ctrs.translate(mytable))


# passing x, y and z
# The third parameter in the mapping table describes characters that you want to remove from the string.
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

# The maketrans() method itself returns a dictionary describing each replacement, in unicode: