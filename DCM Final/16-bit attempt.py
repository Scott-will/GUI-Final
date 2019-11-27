import struct

data = 300
value = struct.pack("<i", data)
print(value)
value2 = struct.unpack("<i", value)
print(value2)