OWASP 10

#1	Injection

1-  Sql Injection - query

2-  Command Injection (OS)- system commands

4-  email injection - send email , 


' or 1=1--:a

' will close the brackets
or  either side must be true
1=1 is true
-- comment out data, restrictions, error will be interpreted as comments







#2	Broken Authentication

brute force (weak passwords)
used ZAP to fuzz, different wordlist, best1050.txt from seclists

/usr/share/seclists

cookie manipulation


Reset Password 

with some social engineering we get jim's brother's name and reset password




Sensisitive Data Exposure


SQL (db usually use SQL or NoSQL)

Stored on servers or files "flat-file" i.e. sqlite



sqlite3 <databse-name>


.table 		to see tables

dump whole db or:

PRAGMA table_info(customers);

SELECT * FROM customers;




FTP
while hovering over a link we see an ftp path

gets around 403 Error
Posion Null Byte = NULL terminator %00
url encoded = %2500


#4 XML External Entity


XXE
1-  in band	(immediate response)
2-  out of band (blind XXE) 

XML - example

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







#5	Broken Access Control


using debugger on firefox or sources on chrome we can see paths

you would need admin privilages to access, 


view someone elses shopping basked
change header to different basket

GET /rest/basket/1 HTTP/1.1
to
GET /rest/basket/2 HTTP/1.1








#6 	Security Misconfiguration

S3 buckets , unnecessary features , weak passwords, Error messagages, not using HTTP security headars


can lead to other vuln = sensitive data, XXE , command injection








#7	Cross-site Scripting (XSS)

1-  DOM <script></script>
2-  Persistent (Server not sanitising uploaded data) 
2-  Reflected (Client not sanitising search data)


types:

popup's

document.write

keylogger

port scanning



http://www.xss-payloads.com



XFS (cross-frame scripting)

<iframe src="javascript:alert(`xss`)"></iframe>

True-Client-IP: <iframe src="javascript:alert(`xss`)">







#8	Insecure Deserialization


Serialisation is the process of converting objects used in programming into simpler, compatible formatting for transmitting between systems or networks for further processing or storage.

Alternatively, deserialisation is the reverse of this; converting serialised information into their complex form - an object that the application will understand.



cookies in plaintext 


to create cookie payload for reverse shell use rce.py


#9	Components with know vulnerabilites


missed updates



#10	Insufficient logging and monitoring


no IDS program







































