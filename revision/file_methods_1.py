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

