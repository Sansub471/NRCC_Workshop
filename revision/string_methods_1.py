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