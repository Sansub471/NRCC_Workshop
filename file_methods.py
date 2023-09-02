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
fp.close()

# file.flush()
fp = open('data.txt', 'a')
#fp.write('\nThis is the new file.\n')
fp.flush()
#fp.write('This is the second new line from script.\n')
fp.close()

print('\n')

# file.isatty()
# returns True if the file stream is interactive, example: connected 
# to a terminal device
fp = open('data.txt', 'r')
print(fp.isatty())
print('')
fp.close()

# file.read()
# returns the specified number of bytes from the file. Default is -1 
# which means the whole file
fp = open('data.txt', 'r')
print(fp.read())
fp.close()
print('')

print('Reading given number of bytes: ')
fp = open('data.txt', 'r')
print(fp.read(50))
fp.close()
print('')

# file.readable()
# returns True if the file is readable, False if not.
f = open('data.txt', 'r')
print(f.readable())
f.close()

# file.readline()
# returns one line from the file
f = open("data.txt", 'r')
print(f.readline())
f.close()
print('')

# file.readlines(hint)
# hint: limit the number of lines returned.
# returns a list containing each line in the file as a list item.
fp = open('data.txt', 'r')
print(fp.readlines())
print('\n')
print(fp.readlines(5))
fp.close()
print('')

# file.seek(offset)
# A number representing the position to set the current file stream position.
# sets the current file position in a file stream and returns the new position
fp = open('data.txt','r')
fp.seek(40) # number of byte
# set the current file stream in a file stream
print(fp.readline())
fp.close()

fp = open('data.txt', 'r')
print(fp.seek(40))
print('')