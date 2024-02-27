# File manipulation methods in python
source = '../data.txt'
fp = open(source, 'r')
print(fp.read())
fp.close()
print("\n")
# Closes an opened file