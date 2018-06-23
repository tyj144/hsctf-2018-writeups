# Jumper
**Binary**, 150pts

We will take advantage of the `gets()` call in `jumper()` to perform a buffer overflow. This attack will end up forcing the program to call the `lol()` function, which we know will print out the flag. 

We will take advantage of the fact that after `gets(dest)` is called on line 13, a return address will be pushed onto the stack so that once the `gets()` function finishes, it returns back to the `jumper()` function. We can exploit the fact the `gets()` function is unsafe, because it does not know when to stop writing user input into the buffer and will thus overwrite the places in the stack after the buffer, including the return address. Our job is to find some input that can overwrite that return address to the address of the `lol()` function, which will then print us the flag.

To do this, we will follow a similar procedure as the one found in:
https://ehsandev.com/pico2014/binary_exploitation/overflow_2.html

First, we run `gdb jumper` to open up the GDB debugger. Inside GDB, we can type `run` to run the program. 
Next, we want to find an input that can fill the buffer enough to overwrite part of the return address. Inputting a string of 46 “A”s tells us that the program crashed at the address 0x08004141, which is a great sign because the last two “41”s are actually two of the “A”s we inputted (“A” = 0x41). This means that we filled the entire buffer with 44 “A”s, and then the remaining two “A”s overwrote half of the return address. 

Thus, if we fill the buffer with 44 “A”s and then tack on the return address for the `lol()` function, the `gets()` method will take our input, fill the entire buffer with “A”s, and then move to the next part of the stack and overwrite the return address to be the address of the `lol()` function. 

To figure out the address of the `lol()` function, we can simply type `print lol` in GDB, which gives us a memory address of “0x804852b”.

To generate our input string, we can use Python to get:
``` 	#jumper.py
import struct

def pack(p):
    return struct.pack('<I', p)

payload = b'A'*44
payload += pack(0x804852b)

print(payload)
```

We can then pipe this output into the netcat connection by running `python jumper.py | nc shell.hsctf.com 10001`, which gives us our flag.

**Flag**: flag{keith_has_no_hops}