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


