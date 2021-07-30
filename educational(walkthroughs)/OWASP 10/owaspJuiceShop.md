# OWASP 10
https://owasp.org/www-project-top-ten/
1- Injection
2- Broken Authentication
3- Sensitive Data Exposure
4- XXE
5- Broken Access Control
6- Security Misconfiguration
7- XSS
8- Insecure Deserialization
9- Using Components with Known Vulnerabilites
10- Insufficient Logging & Monitoring


## 1	Injection

1-  Sql Injection - query

2-  Command Injection (OS)- system commands

3-  email injection - send email , 


' or 1=1--:a

' will close the brackets
or  either side must be true
1=1 is true
-- comment out data, restrictions, error will be interpreted as comments

has the big 4
https://portswigger.net/web-security/sql-injection/cheat-sheet





## 2	Broken Authentication

brute force (weak passwords)
used ZAP to fuzz, different wordlist, best1050.txt from seclists

/usr/share/seclists

cookie manipulation


Reset Password 

with some social engineering we get jim's brother's name and reset password




## 3 Sensitive Data Exposure

if file is underneath root directory of web app, we can download it. 

SQL (db usually use SQL or NoSQL)

Stored on servers or files "flat-file" i.e. sqlite



sqlite3 `<databse-name>`

.table 		(to see tables)

dump whole db or:

PRAGMA table_info(customers);  (to see colums)

SELECT * FROM customers;




FTP
while hovering over a link we see an ftp path

gets around 403 Error
Posion Null Byte = NULL terminator %00
url encoded = %2500


## 4 XML External Entity XXE
Two types:

1-  in band	(immediate response)
	- retrieve files
	- SSRF attack

2-  out of band (blind XXE) 
	- exfiltrate data
	-  retrieve data via error message
	
XML - example
```xml
<?xml version="1.0" encoding="UTF-8"?>
<mail>
   <to>falcon</to>
   <from>feast</from>
   <subject>About XXE</subject>
   <text>Teach about XXE</text>
</mail>


XML  - payload 

<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

```

## 5 Broken Access Control

IDOR - insecure direct object reference

using debugger on firefox or sources on chrome we can see paths

you would need admin privileges to access, 


view someone else's shopping basked
change header to different basket

GET /rest/basket/1 HTTP/1.1
to
GET /rest/basket/2 HTTP/1.1

## 6 Security Misconfiguration

S3 buckets , unnecessary features , weak passwords, Error messages, not using [HTTP security](https://owasp.org/www-project-secure-headers/) headers


can lead to other vulnerability = sensitive data, XXE , command injection

## 7	Cross-site Scripting (XSS)

1-  DOM `<script></script>`
2-  Persistent (Server not sanitizing uploaded data) 
2-  Reflected (Client not sanitizing search data)


types of xss payloads:

popup's

document.write

keylogger

port scanning


http://www.xss-payloads.com



XFS (cross-frame scripting)

`<iframe src="javascript:alert(`xss`)"></iframe>`

True-Client-IP: `<iframe src="javascript:alert(`xss`)">`


## 8 Insecure Deserialization

Serialization is the process of converting objects used in programming into simpler, compatible formatting for transmitting between systems or networks for further processing or storage.

Alternatively, deserialization is the reverse of this; converting serialized information into their complex form - an object that the application will understand.

Tourist map example

> A Tourist approaches you in the street asking for directions. They're looking for a local landmark and got lost. Unfortunately, English isn't their strong point and nor do you speak their dialect either. What do you do? You draw a map of the route to the landmark because pictures cross language barriers, they were able to find the landmark. Nice! You've just serialised some information, where the tourist then deserialised it to find the landmark.

#### objects
made up of two things, lamp example
	- State - type of bulb
	- Behavior - On/Off 
	
#### cookies

cookies in plaintext 

#### code execution
python pickle vuln 
to create cookie payload for reverse shell use [rce.py](scripts/rce.py)



---
## 9	Components with know vulnerabilites

- updating
- migrating

## 10	Insufficient logging and monitoring


no IDS program







































