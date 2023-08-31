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