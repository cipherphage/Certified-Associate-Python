# with open("xmen.txt", 'w+') as my_file:
my_file = open("xmen.txt", 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n',
])

# file object has a cursor so if we print the file
# right now we will print nothing because the cursor
# is at the end of the file:
print(my_file.read())

# so we can either close the file and re-open it or
# we can simply use the seek method and start from the position of 0:
my_file.seek(0)
print(my_file.read())

my_file.seek(0)
my_file.write('Morph')
my_file.seek(0)
for line in my_file.readlines():
    print(line)

my_file.close()

# my_file = open('xmen.txt', 'r')
# print(my_file.read())
# my_file.close()

# Using "with" automatically closes the file at the end:
my_file = open('xmen.txt', 'r')
with my_file:
  print(my_file.read())


# using bytes

# For bytes, indexing will return an integer; slicing will return a bytes object:
# >>> my_bytes
# b'This is a byte'
# >>> my_bytes[0]
# 84
# >>> my_bytes[0:2]
# b'Th'

# >>> bytearray()
# bytearray(b'')
# >>> bytearray(10)
# bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# >>> bytearray(range(10))
# bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')
# >>> bytearray(b'Bytes')
# bytearray(b'Bytes')

# Because bytearrays are mutable, we can use the same assignment operations that we 
# would normally with a list, except that we need to remember that when working with 
# an index, we need to pass in an integer value and when replacing a slice we need to 
# pass in a bytes object:
# >>> b_array = bytearray(10)
# >>> b_array[0] = b'T'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'bytes' object cannot be interpreted as an integer
# >>> b_array[0:1] = b'T'
# >>> b_array
# bytearray(b'T\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# >>> b_array[1] = 0x10
# >>> b_array
# bytearray(b'T\x10\x00\x00\x00\x00\x00\x00\x00\x00')

with open('xmen.txt', 'rb') as f:
    print(f.read())
    f.seek(0)
    print(f.readlines())
    b_array = bytearray(10)
    f.seek(0)
    f.readinto(b_array)
    print(b_array)
    new_b_array = bytearray(f.read(5))
    print(new_b_array)
    print(len(new_b_array))