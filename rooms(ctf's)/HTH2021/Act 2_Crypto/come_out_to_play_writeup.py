import base64
import binascii
import codecs
import json
import telnetlib

HOST = "18.222.113.93"
PORT = 7807

tn = telnetlib.Telnet(HOST, PORT)

def receive_prompt():
    return tn.read_until(b"Response: ", timeout=1)

def receive_level():
    line = ""
    try:
        line = tn.read_until(b"\n")
        receive_prompt() # read and drop the "Response:"" prompt on the floor
    except EOFError as e:
        return line
    return line.decode("utf8")

def send_line(line):
    tn.write(line)

# get first level
received = receive_level()
print("\n>> Received - {}".format(received.replace("\n", "")))

# continue process while we keep receiving new valid lines
while received:
    if 'type' not in received:
        print(f"flag: {received}")
        break
    elif received.startswith("Level"):
        received = received[received.find("{"):]
        received = json.loads(received)
    
    print(f"Received type: {received['type']}")
    print(f"Encoded Value: {received['encoded']}")

    decoded = ""
    if received["type"] == "base64":
        decoded = base64.b64decode(received["encoded"]).decode('utf-8')
    elif received["type"] == 'utf-8':
        for x in received["encoded"]:
            decoded += chr(x)
    elif received["type"] == "rot13":
        decoded = codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "hex":
        decoded = binascii.unhexlify(received["encoded"]).decode('utf-8')
    else:
        break
    # send response
    print(f"Sending: {decoded}")
    send_line(bytes(decoded + "\n", encoding='utf-8'))

    # get next level
    received = receive_level()
    print("\n>> Received - {}".format(received.replace("\n", "")))
































