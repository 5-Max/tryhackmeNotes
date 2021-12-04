**Aspurr:** You made it! Welcome to the safehouse!

There's not much time to celebrate. We need you to monitor for intercepted messages. The terminal is over there.

_Aspurr points to a dark corner of the room with a dusty laptop providing the only illumination_

**Aspurr:** The Nexxus riot teams use long-range, low-power communications to search large areas quickly. They commonly use weak encoding to obfuscate messages due to payload size limitations. Our interceptors are stationed around the city and will show messages as they are snooped.

We need you on that terminal decoding messages as fast as possible. There are some notes on the table next to the terminal if you need to brush up.

Don't mess this up.

`nc 18.222.113.93 7806`
```bash 
[Hax4Headz RF SNIFFER v3.5.6] Intercepting messages...
ZzZ~zzZ~ZZz~ tell St0ke we're closing in on them quickly ~ZzZ~zzZ~ZZz

[Hax4Headz RF SNIFFER v3.5.6] Captured a raw message encoded with three unique keys...
KEY1 = 01bc5208fa52c816e880df39a825070a8e7e9105228409cd73e7d07ada88fd430dbd7a
KEY2 ^ KEY1 = b4ff12a92f113607373d6b74093f7219aa3db9b1049115305568e988bf3b29b8b6bb85
KEY2 ^ KEY3 = 0c6a977a51c55b6284288ff1c63589d811bc4326283a61b119dada26cee58fe5c1cbe3
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 45828d09d3f8e12b04c92397077efab7eda7a15763d00f231a4f652c711f06cfa905e4
```

Hint: Use the prodided file to help you "undo" the XOR'd bytes you're given by the challenge server.

```py
import binascii

def xor_byte_string(str1, str2):
    return bytes(a ^ b for a, b in zip(str1, str2))

# Commutative: A ⊕ B = B ⊕ A
print(">> Checking Commutative property....", end=" ")
A = binascii.unhexlify("deadbeef")
B = binascii.unhexlify("cafebabe")
try:
    assert xor_byte_string(A, B) == xor_byte_string(B, A)
    print("Commutative property holds!")
except AssertionError:
    print("Commutative property does not hold!")

# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
print(">> Checking Associative property....", end=" ")
A = binascii.unhexlify("deadbeef")
B = binascii.unhexlify("cafebabe")
C = binascii.unhexlify("1337beef")
try:
    assert xor_byte_string(A, xor_byte_string(B, C)) ==  xor_byte_string(xor_byte_string(A, B), C)
    print("Associative property holds!")
except AssertionError:
    print("Associative property does not hold!")

# Identity: A ⊕ 0 = A
print(">> Checking Identity property.......", end=" ")
A = binascii.unhexlify("deadbeef")
B = binascii.unhexlify("00000000")
try:
    assert xor_byte_string(A, B) ==  A
    print("Identity property holds!")
except AssertionError:
    print("Identity property does not hold!")

# Self-Inverse: A ⊕ A = 0
print(">> Checking Self-Inverse property...", end=" ")
A = binascii.unhexlify("deadbeef")
try:
    assert xor_byte_string(A, A) == b'\x00\x00\x00\x00'
    print("Self-Inverse property holds!")
except AssertionError:
    print("Self-Inverse property does not hold!")
```
