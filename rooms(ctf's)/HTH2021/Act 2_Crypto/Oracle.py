import telnetlib
import binascii

HOST = "18.222.113.93"
PORT = 7808

tn = telnetlib.Telnet(HOST, PORT)

def recive_prompt():
    return tn.read_until(b"\n", timeout=1)

print(recive_prompt())
def receive_awnser():
    line = ""
    try:
        line = tn.read_until(b"\n")
        receive_prompt() # read and drop the "Response:"" prompt on the floor
    except EOFError as e:
        return line
    return line.decode("utf8")

def send_line(line):
    tn.write(line)

received = receive_awnser()

guess = "1111111111111"

while received:
    if 'Enter' not in received:
        print(f"flag: {received}")
        break
    elif received.startswith("Enter"):
        send_line(bytes(guess + "\n", encoding='utf-8'))
        print(guess)
