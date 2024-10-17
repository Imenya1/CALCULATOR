# # opent the file in read mode
# file = open('new.txt', 'r')
# # read the entire content of the file
# content = file.read()
# print(content)
# file.close()

# # opent the file in read mode
# file = open('new.txt', 'r')
# # read the entire content of the file
# content = file.readlines()
# print(content)
# file.close()

import struct

# # Open the file in binary read mode
# with open('test.bin', 'rb') as f:
#    # Read the binary data from the file
#    data = f.read()
    
#    # Unpack the binary data to retrieve the float
#    x = struct.unpack('f', data)[0]
    
#    # Print the float value
#    print(x)

# import struct

# # Define a floating-point number
# x = 23.50

# # Pack the float into a binary format
# data = struct.pack('f', x)

# # Open the file in binary write mode and write the packed data
# with open('test.bin', 'wb') as f:
#    f.write(data)

# # Open a file in read-write mode
# fo = open("new.txt", "w+")

# # Write initial data to the file
# fo.write("This is a rat race")

# # Seek to a specific position in the file
# fo.seek(10, 0)

# # Read a few bytes from the current position
# data = fo.read(3)
# print("Data read from position 10:", data)

# # Seek back to the same position
# fo.seek(10, 0)

# # Overwrite the earlier contents with new text
# fo.write("cat")

# # Rewind to the beginning of the file
# fo.seek(0, 0)

# # Read the entire file content
# data = fo.read()
# print("Updated file content:", data)

# Close the file
# fo.close()


# Open the file in read-write mode
with open("new.txt", "r+") as fo:
   # Move the read/write pointer to the 10th byte position
   fo.seek(10, 0)
    
   # Read 3 bytes from the current position
   data = fo.read(3)
    
   # Print the read data
   print(data)