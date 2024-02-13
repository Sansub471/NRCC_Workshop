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