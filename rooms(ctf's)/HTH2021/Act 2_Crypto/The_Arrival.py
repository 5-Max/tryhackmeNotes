import binascii

def xor_byte_string(str1, str2):
    return bytes(a ^ b for a, b in zip(str1, str2))

# # Commutative: A ⊕ B = B ⊕ A
# print(">> Checking Commutative property....", end=" ")
# A = binascii.unhexlify("deadbeef")
# B = binascii.unhexlify("cafebabe")
# try:
#     assert xor_byte_string(A, B) == xor_byte_string(B, A)
#     print("Commutative property holds!")
# except AssertionError:
#     print("Commutative property does not hold!")

# # Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# print(">> Checking Associative property....", end=" ")
# A = binascii.unhexlify("deadbeef")
# B = binascii.unhexlify("cafebabe")
# C = binascii.unhexlify("1337beef")
# try:
#     assert xor_byte_string(A, xor_byte_string(B, C)) ==  xor_byte_string(xor_byte_string(A, B), C)
#     print("Associative property holds!")
# except AssertionError:
#     print("Associative property does not hold!")

# # Identity: A ⊕ 0 = A
# print(">> Checking Identity property.......", end=" ")
# A = binascii.unhexlify("deadbeef")
# B = binascii.unhexlify("00000000")
# try:
#     assert xor_byte_string(A, B) ==  A
#     print("Identity property holds!")
# except AssertionError:
#     print("Identity property does not hold!")

# # Self-Inverse: A ⊕ A = 0
# print(">> Checking Self-Inverse property...", end=" ")
# A = binascii.unhexlify("deadbeef")
# try:
#     assert xor_byte_string(A, A) == b'\x00\x00\x00\x00'
#     print("Self-Inverse property holds!")
# except AssertionError:
#     print("Self-Inverse property does not hold!")

# KEY1 = "639049d9d672d49b1426e091cb3ee657848f51fe99383fe2ab6652487b18ab0ca04659"
# KEY2 ^ KEY1 = "6710200805a3ca301379a915576389935e84bf0e4b2826a6b87b3511505a6e4e4a132a"
# KEY2 ^ KEY3 = "d410297dd17282c66cfeed5aae973ff5d0f407e905609de008b5043e58d88d1610254d"
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = "ffd428df7f6f240210b97e940cc7adc7261e2563f536c55dd3a1390646b25273d51069"

key1 = binascii.unhexlify("639049d9d672d49b1426e091cb3ee657848f51fe99383fe2ab6652487b18ab0ca04659")
key2_key1 = binascii.unhexlify("6710200805a3ca301379a915576389935e84bf0e4b2826a6b87b3511505a6e4e4a132a")
key2_key3 = binascii.unhexlify("d410297dd17282c66cfeed5aae973ff5d0f407e905609de008b5043e58d88d1610254d")
flag_key1_key3_key2 = binascii.unhexlify("ffd428df7f6f240210b97e940cc7adc7261e2563f536c55dd3a1390646b25273d51069")

key2 = xor_byte_string(key1, key2_key1)
key3 = xor_byte_string(key2_key3, key2)
flag_key3_key2 = xor_byte_string(flag_key1_key3_key2, key1)
flag_key3 = xor_byte_string(flag_key3_key2, key2)
flag = xor_byte_string(flag_key3, key3)
print(flag)
