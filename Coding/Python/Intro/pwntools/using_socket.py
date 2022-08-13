
#!/bin/python2
import socket

target_host = "10.10.22.41"
target_port = 80

#create socket object
# AF_INET -> Say that we use IPv4 address or hostname
# SOCK_STREAM -> Indicate this will be a TCP connection.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((target_host, target_port))

if response = <p>That is wrong! Get outta here!</p>


#send Data
client.send("GET /th1s_1s_h1dd3n/?secret=0 HTTP/1.1\r\nHost:10.10.22.41\r\n\r\n")

#receive data
response = client.recv(4096) #recv 4096 bytes

else print response

print response