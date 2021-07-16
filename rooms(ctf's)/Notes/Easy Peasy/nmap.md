```basic
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.133.159
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-08 08:51 EDT
Nmap scan report for 10.10.133.159
Host is up (0.10s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 11.93 seconds
```                                                    

```basic
┌──(kali㉿kali)-[~]
└─$ nmap -p- --open 10.10.133.159
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-08 08:52 EDT
Nmap scan report for 10.10.133.159
Host is up (0.11s latency).
Not shown: 64716 closed ports, 816 filtered ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
==80/tcp    open  http
6498/tcp  open  unknown
65524/tcp open  unknown==

Nmap done: 1 IP address (1 host up) scanned in 46.04 seconds
```                                                                                  

```basic
┌──(kali㉿kali)-[~]
└─$ nmap -p80 -sV 10.10.133.159  
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-08 08:53 EDT
Nmap scan report for 10.10.133.159
Host is up (0.098s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.16.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.69 seconds
```

```basic
┌──(kali㉿kali)-[~]
└─$ nmap -sCV -p- -Pn -T5 -v 10.10.133.159               
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-08 08:53 EDT
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 08:53
Completed NSE at 08:53, 0.00s elapsed
Initiating NSE at 08:53
Completed NSE at 08:53, 0.00s elapsed
Initiating NSE at 08:53
Completed NSE at 08:53, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 08:53
Completed Parallel DNS resolution of 1 host. at 08:53, 0.02s elapsed
Initiating Connect Scan at 08:53
Scanning 10.10.133.159 [65535 ports]
Discovered open port 80/tcp on 10.10.133.159
Warning: 10.10.133.159 giving up on port because retransmission cap hit (2).
Discovered open port 65524/tcp on 10.10.133.159
Connect Scan Timing: About 8.38% done; ETC: 08:59 (0:05:39 remaining)
Connect Scan Timing: About 17.46% done; ETC: 08:59 (0:04:48 remaining)
Connect Scan Timing: About 26.80% done; ETC: 08:58 (0:04:09 remaining)
Connect Scan Timing: About 35.45% done; ETC: 08:58 (0:03:40 remaining)
Connect Scan Timing: About 45.95% done; ETC: 08:58 (0:02:58 remaining)
Connect Scan Timing: About 53.26% done; ETC: 08:58 (0:02:39 remaining)
Connect Scan Timing: About 62.61% done; ETC: 08:58 (0:02:06 remaining)
Connect Scan Timing: About 69.50% done; ETC: 08:59 (0:01:46 remaining)
Connect Scan Timing: About 78.50% done; ETC: 08:59 (0:01:14 remaining)
Connect Scan Timing: About 86.58% done; ETC: 08:59 (0:00:47 remaining)
Discovered open port 6498/tcp on 10.10.133.159
Completed Connect Scan at 08:59, 379.82s elapsed (65535 total ports)
Initiating Service scan at 08:59
Scanning 3 services on 10.10.133.159
Completed Service scan at 08:59, 11.35s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.133.159.
Initiating NSE at 08:59
Completed NSE at 08:59, 4.19s elapsed
Initiating NSE at 08:59
Completed NSE at 08:59, 0.61s elapsed
Initiating NSE at 08:59
Completed NSE at 08:59, 0.03s elapsed
Nmap scan report for 10.10.133.159
Host is up (0.10s latency).
Not shown: 64138 closed ports, 1394 filtered ports
PORT      STATE SERVICE VERSION
80/tcp    open  http    nginx 1.16.1
| http-methods: 
|_  Supported Methods: GET HEAD
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: nginx/1.16.1
|_http-title: Welcome to nginx!
6498/tcp  open  ssh    OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 30:4a:2b:22:ac:d9:56:09:f2:da:12:20:57:f4:6c:d4 (RSA)
|   256 bf:86:c9:c7:b7:ef:8c:8b:b9:94:ae:01:88:c0:85:4d (ECDSA)
|_  256 a1:72:ef:6c:81:29:13:ef:5a:6c:24:03:4c:fe:3d:0b (ED25519)
65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.43 (Ubuntu)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 08:59
Completed NSE at 08:59, 0.00s elapsed
Initiating NSE at 08:59
Completed NSE at 08:59, 0.00s elapsed
Initiating NSE at 08:59
Completed NSE at 08:59, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 400.53 seconds
```

80
6498
65524