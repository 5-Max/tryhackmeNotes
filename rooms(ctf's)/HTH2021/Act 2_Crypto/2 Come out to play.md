**Aspurr:** Dammit! They're hunting the safehouse. We need to hold them off as long as we can.

_Aspurr paces back and forth between the rows of computers in the makeshift SOC as hax members tap furiously at their terminals_

**Aspurr:** We need to~_CRRRSSSHHH_

_Static breaks the squelch noise floor of several radios in the room_

**St0ke:** Haaaax, come out to plaaeeay!

Oh you didn't think you could hide from us, did you?

**Aspurr:** Sh-t! Get back on that terminal, they'll be rolling keys but still using low power, likely just encoded messages again. This will get harder as they get closer. Go, now!

**St0ke:** Come on hax, don't make this easy on us. At least KROM put up a fight.

**Aspurr:** We'll show you a fight, you mother~_mumbles_

`nc 18.222.113.93 7807`
```bash
┌──(max㉿kali)-[~/Downloads]
└─$ nc 18.222.113.93 7807                                                      1 ⨯


Level 1: {"type": "utf-8", "encoded": [99, 111, 110, 99, 111, 110, 95, 109, 111, 110, 107, 101, 121, 56, 95, 100, 101, 109, 111, 110]}
Response: 
```


Hint:
This one should be scripted. You have to decode 100 challenges in a row to solve it! Please don't try this manually!

```bash
                                                                                  
┌──(max㉿kali)-[~/Downloads]
└─$ nc 18.222.113.93 7807

Level 1: {"type": "base64", "encoded": "aXJpc2hfbHluc2V5X2FuaW1hbA=="}
Response: 
Level 1 of 100 failed. Hanging up.
```

script
connect

```py
from socket import *
    
s = socket(AF_INET, SOCK_STREAM)
ip = "10.10.10.10"
port = 8888
    
s.connect((ip, port))
rec = s.recv(1024)
print(rec)
 ```

connect X
read
type: ?;
-  base64 -d
-  hex
-  rot13 to base 64
-  utf-8 (take comma out )
encoded: hash
decode
response

getflag ??

```bash
Level 1: {"type": "base64", "encoded": "c3VtbWVyX21hY2tlbnppZTFfYW5nZWw0"}
Response: summer_mackenzie1_angel4
Level 2: {"type": "base64", "encoded": "c3RyaWRlcl9jYXJyb3RzX2xlbm5vbg=="}
Response: strider_carrots_lennon
Level 3: {"type": "hex", "encoded": "4c4f5645594f555f6a756c69656e5f313031303837"}
Response: LOVEYOU_julien_101087
Level 4: {"type": "base64", "encoded": "bWFuY2l0eV9vc2l0b19DaGFybGll"}
Response: mancity_osito_Charlie
Level 5: {"type": "utf-8", "encoded": [97, 110, 103, 101, 108, 49, 50, 95, 99, 97, 110, 97, 100, 97, 95, 99, 97, 115, 101, 121, 49]}
```

```py
bytes.fromhex('41').decode('utf-8')
```

```py
from socket import * 
import base64 
import time 
import string 

s = socket(AF_INET, SOCK_STREAM) ip = "18.222.113.93" port = 7807 s.connect((ip, port)) 
rq = '"' 
rec = s.recv(1024) 
a = rec.replace("encoded", "") 
b = a.replace(":", "") 
c = b.replace("Level", "") 
d = c[3:] e = d.replace("type", "") 
f = e.replace("{", "") 
g = f.replace("}", "") 
z = g.replace(",", "") 

if 'base64' in z: 
    level = b[:8] 
    p = z[16:] 
    k = p.replace('"', '') 
    l = base64.decodestring(k) 
    print(level + "" + l) 
    print("[BASE64]") 
    
    elif 'rot13' in z: 
        rot13Table = string.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm") 
        omg = z.replace('"', '') 
        ff = omg.replace(" ", "") 
        fff = ff.replace("rot13", "") 
        level_rot = b[:8] 
        rot13 = lambda s : 
        string.translate(s, rot13Table) 
        print(level_rot + rot13(fff))
        print("[ROT-13]") 
    elif 'hex' in z: 
        ohhhhh = z.replace('"', '') 
        okee = ohhhhh.replace("hex", "") 
        animm = okee[3:] levelll = b[:8] 
        hex = bytes.fromhex(animm) 
        hex = hex.decode("ASCII") 
        print(levelll + "" + hex) 
    elif 'utf-8' in z: print(z)
python2
```