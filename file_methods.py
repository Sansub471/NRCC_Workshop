# File methods
# file.close()
fp = open("data.txt", "r")
print(fp.read())
fp.close()
print('\n')
# closes an open file

# detach() : returns the separated raw stream from the buffer
# file.fileno()
# returns the file description of the stream, as a number
# an error will occur if the operator system does not use file descriptor

fp = open('data.txt', 'r')
print(fp.fileno())

# file.flush()
fp = open('data.txt', 'a')
fp.write('This is the new file.\n')
fp.flush()
fp.write('This is the second new line from script\n')

print('\n')

# file.isatty()
# returns True if the file stream is interactive, example: connected 
# to a terminal device
fp = open('data.txt', 'r')
print(fp.isatty())
print('')

# file.read()
# returns the specified number of bytes from the file. Default is -1 
# which means the whole file
fp = open('data.txt', 'r')
print(fp.read())
print('')

print('Reading given number of bytes: ')
fp = open('data.txt', 'r')
print(fp.read(50))
print('')