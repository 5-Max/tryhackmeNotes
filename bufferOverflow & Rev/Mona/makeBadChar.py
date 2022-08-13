

from __future__ import print_function

listRem = "\\x00\\x04\\x3e\\xe1".split("\\x")
for x in range(1, 256):
    if "{:02x}".format(x) not in listRem:
        print("\\x" + "{:02x}".format(x), end='')
print()
