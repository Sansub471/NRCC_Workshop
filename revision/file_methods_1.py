# File manipulation methods in python
source = '../data.txt'
source1 = '../datacp.txt'

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

# file.seekable()
# returns True if the file is seekable, False if not
# A file is seekable if it allows to the file stream, like seek() method.
fp = open(source, 'r')
print(fp.seekable())
fp.close()

# file.tell()
# returns the current file position in a file stream.
# you can change the current file position with the seek() method.
print("seek() and tell() function :")
fp = open(source, 'r')
print(fp.tell())
fp.seek(50)
print(fp.tell())
print('\n')
fp.close()

print("file.truncate() function : ")
# file.truncate(size)
# The size of the file(in bytes) after the truncate. Default None, which 
# means the current file stream position
fp = open(source1, 'a')
fp.truncate(40)
fp.close()

# The . truncate() file method allows the user to resize the file to a 
# given number of bytes when the file is accessed through the append mode.

# open and read the file after the truncate
fp = open(source1, 'r')
print(fp.read())
fp.close()

print("file.write() functions : ")
# file.writable()
# returns True if the file is writeable else False
# A file is writeable if it is opened using 'a' for append or 'w' for write
fp = open(source, 'r')
print(fp.writable())
print('\n')
fp.close()

fp = open(source, 'w')
print(fp.writable())
fp.close()

print("file.write() :")
# file.write(bytes)
# method writes a specified text to the file.
# where the specified text will be inserted depends on the file mode and stream positoin
# a : inserted at the end of file by default
# w : file empetied before the text will be inserted at the current file stream, default 0
fp = open(source, 'a')
fp.write('Hello! Today is WAFF Final without Samba, a tough game ahead.')
fp.close()

fp = open(source, 'r')
print(fp.read())
fp.close()