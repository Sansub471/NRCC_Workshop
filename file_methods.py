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

# file.seekable()
# returns True if the file is seekable, False if not
# A file is seekable if it allows to the file stream, like the seek() method.
fp = open('data.txt', 'r')
print(fp.seekable())
fp.close()

# file.tell()
# returns the current file position in a file stream
# you can change the current file position with the seek() method.
fp = open('data.txt','r')
print(fp.tell())
fp.seek(50)
print(fp.tell())
print('')
fp.close()

# file.truncate(size)
# The size of the file(in bytes) after the truncate. Default None, which
# means the current file stream position.
fp = open('datacp.txt', 'a')
fp.truncate(40)
fp.close()

# The . truncate() file method allows the user to resize the file to a given
# number of bytes when the file is accessed through the append mode.

# open and read the file after the truncate
fp = open('datacp.txt', 'r')
print(fp.read())
fp.close()

# file.writable()
# returns True if the file is writable, False if not
# A file is writable if it is opened using 'a' for append or 'w' for write
fp = open('data.txt', 'r')
print(fp.writable())
print('')
fp.close()

# file.write(byte)
# method writes a specified text to the file.
# where the specified text will be inserted depends on the file mode and stream position
# "a" : text inserted by default at the end of the file
# "w" : file empitied before the text will be inserted at the current file strem, default 0
fp = open('data.txt', 'a')
fp.write('Hello world, this is the end of the file.')
fp.close()

# open and read the file after the appending 
fp = open('data.txt', 'r')
print(fp.read())
fp.close()

# Files have been completed.

