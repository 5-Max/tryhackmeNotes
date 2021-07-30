import base64

file = open("encodedflag.txt","r")

flag = file.read()


code = ""

for i in range(0,5):
	code = base64.b16decode(flag)
	flag = code

for i in range(0,5):
	code = base64.b32decode(flag)
	flag = code

for i in range(0,5):
	code = base64.b64decode(code)
	flag = code

print(flag)
file.close()
