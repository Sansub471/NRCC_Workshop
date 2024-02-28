# File manipulation methods in python
source = '../data.txt'
fp = open(source, 'r')
print(fp.read())
fp.close()
print("\n")
# Closes an opened file

# file.read()
# returns the specified number of bytes from the file. Default is -1
# which means the whole file.

fp = open(source, 'r')
lines = fp.read() # Read the entire file
print(lines)
print("\n")
fp.close()

# Read 200 bytes from file
fp = open(source, 'r')
byte_size = 39
lines = fp.read(byte_size)
print(lines)
print('\n')

# file.readable()
# returns True is the file is readable, False is not.

fp = open(source, 'r')
print(fp.readable())
fp.close()

print("\nfile.readline() function : ")
# fp.readline()
# returns one line from the file
fp = open(source, 'r')
print(fp.readline())
fp.close()
print("\n")

# file.readlines(hint)
# hint: limit the number of lines returned.
# returns a list containing each line in the file as a list item.
fp = open(source, 'r')
print(fp.readlines())
print('\n')
print(fp.readlines(-1))
fp.close()
print('\n')

# file.seek(offset)
# A number representing the position to set the current file stream position.
# sets the current file position in a file stream and returns the new position
fp = open(source, 'r')
fp.seek(39) # number of byte
# set the current file stream in a file stream
print(fp.readline())
fp.close()
