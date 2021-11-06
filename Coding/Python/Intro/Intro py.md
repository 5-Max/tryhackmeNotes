
# Intro
Throughout this room, we will touch on subjects such as:

-   Variables
-   Loops
-   Functions
-   Data Structures
-   Libraries (PIP)
-   Files

# Hello World
```py

#hello world   //this is how you comment in py, and there is no multi-comment
print("hello world")    echo, console.log, 

input("Please input you credit card number")


```
# Math stuff
**Operator**   |  **Syntax**
---------------|-------------
Addition  | +  
Subtraction  | -  
Multiplication  | *  
Division  | /  
Modulus  | %  
Exponent  | **  
Floor Division   |//


**Operator**   |  **Syntax**
---------------|-------------
Greater than | >
Less than | <
Equal to | ==
Not Equal to | !=
Greater or equal to | >=
Less than or equal | <=
# Logic
**Operator**   |  **Syntax**
---------------|-------------
and | and
or | or
not | not 
is | is
in | in
# Data type & var
**Data Type** | ex
boolean | t / f
string | "hello world"
Integer |32
Float | 4.3
List | 	`[1,2,3,4]`  // array  python will take both integers and strings
Dictionary | `{1:"one", 2:"two", 3:"three"}`

Global and Local Variables

input 
`name = input("whats your name?")`

input as integer
`age = int(input("how old are you?"))`
# functions
Functions play a massive part when it comes to Python and many other languages, Python has a unique way of creating them as instead of them being called functions they are known as definitions, we would create one as follows:
```py
def username():
  name = input("what's your name?")
  return name
  
print(username())
  
```

```python
#passing data into variables

def tryhackme(creator, assigment):
  print(creator, assigment)
  return
  
name = input("input creators name here: ")
assigment = input("input room assigment here: ")

tryhackme(name, assigment)
```

example returns all sorts of errors,,, 
# if statements
```py
if a == 1:
  do something
else:
  do this
```

```py

name = "optional"

if name == "optional":
  print("optional is here")
elif name == "not optional":
  print("whatever")
else:
  print("blue is my favorite color")
```

```py
name = "pars"
role = "cactus"

if name == "pars and role == "cactus":
  print("the one true cactus")
else:
  print("imposter")
```
# loops
while this is true keep doing

```py
while True:
  print("spam")
```

```py
i = 0 
while i <= 10:
  print(i)
  i +=1
```

for loops 
iterating through an array
```py
admins = ["joe", "mike", "randy"]

for i in admins:
  print(i)
```

# loops x amount of times
```py

(start point, end point, increment)

for i in range(0,20,2):
  print(i)
else:
  print("Done")

```

# files
```

var = arg("filename.txt", "mode")

file = open("test.txt", "w")

.read()
.write()
file.close()
```
# Virtual Env
couldn't get virtual env to install , 

`sudo apt install virtualenv`

run	     				what version 				name of env
`virtualenv --python=python3 introduction`

activate env
`source introduction/bin/activate`

type `deactivate` to exit

# lib pip

`pip3 install -r requirements.txt`

*os*
https://docs.python.org/3/library/os.html

*base64*
https://docs.python.org/3/library/base64.html

# final challenge 
- 5 times encoded using base 64
- 5 times encoded using base 32
- 5 times encoded using base 16!

[my super failed attempt](decode.py)

[the actual soludion](finalSolution.py)

https://docs.python.org/3/library/base64.html

