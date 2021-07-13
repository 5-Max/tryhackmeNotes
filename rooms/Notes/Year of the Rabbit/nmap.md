```
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.18.211                                    
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-09 17:25 EDT
Nmap scan report for 10.10.18.211
Host is up (0.10s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 13.23 seconds
```

```
└─$ nmap -sCV -p- -Pn -T5 -v 10.10.18.211                
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-09 17:34 EDT
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 17:35
Completed NSE at 17:35, 0.00s elapsed
Initiating NSE at 17:35
Completed NSE at 17:35, 0.00s elapsed
Initiating NSE at 17:35
Completed NSE at 17:35, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 17:35
Completed Parallel DNS resolution of 1 host. at 17:35, 0.03s elapsed
Initiating Connect Scan at 17:35
Scanning 10.10.18.211 [65535 ports]
Discovered open port 21/tcp on 10.10.18.211
Discovered open port 80/tcp on 10.10.18.211
Discovered open port 22/tcp on 10.10.18.211
Warning: 10.10.18.211 giving up on port because retransmission cap hit (2).
Connect Scan Timing: About 3.89% done; ETC: 17:48 (0:12:46 remaining)
Connect Scan Timing: About 12.35% done; ETC: 17:48 (0:11:50 remaining)
Connect Scan Timing: About 17.54% done; ETC: 17:47 (0:10:11 remaining)
Connect Scan Timing: About 22.30% done; ETC: 17:47 (0:09:18 remaining)
Connect Scan Timing: About 28.00% done; ETC: 17:46 (0:08:09 remaining)
Connect Scan Timing: About 35.21% done; ETC: 17:45 (0:06:45 remaining)
Connect Scan Timing: About 42.38% done; ETC: 17:45 (0:05:40 remaining)
Connect Scan Timing: About 51.19% done; ETC: 17:44 (0:04:27 remaining)
Connect Scan Timing: About 58.40% done; ETC: 17:44 (0:03:41 remaining)
Connect Scan Timing: About 66.54% done; ETC: 17:43 (0:02:51 remaining)
Connect Scan Timing: About 72.20% done; ETC: 17:43 (0:02:22 remaining)
Connect Scan Timing: About 78.85% done; ETC: 17:43 (0:01:47 remaining)
Connect Scan Timing: About 85.21% done; ETC: 17:43 (0:01:15 remaining)
Connect Scan Timing: About 90.33% done; ETC: 17:43 (0:00:49 remaining)
Completed Connect Scan at 17:44, 544.68s elapsed (65535 total ports)
Initiating Service scan at 17:44
Scanning 3 services on 10.10.18.211
Completed Service scan at 17:44, 6.85s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.18.211.
Initiating NSE at 17:44
Completed NSE at 17:44, 7.95s elapsed
Initiating NSE at 17:44
Completed NSE at 17:44, 1.14s elapsed
Initiating NSE at 17:44
Completed NSE at 17:44, 0.15s elapsed
Nmap scan report for 10.10.18.211
Host is up (0.14s latency).
Not shown: 62003 closed ports, 3529 filtered ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   1024 a0:8b:6b:78:09:39:03:32:ea:52:4c:20:3e:82:ad:60 (DSA)
|   2048 df:25:d0:47:1f:37:d9:18:81:87:38:76:30:92:65:1f (RSA)
|   256 be:9f:4f:01:4a:44:c8:ad:f5:03:cb:00:ac:8f:49:44 (ECDSA)
|_  256 db:b1:c1:b9:cd:8c:9d:60:4f:f1:98:e2:99:fe:08:03 (ED25519)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 17:44
Completed NSE at 17:44, 0.00s elapsed
Initiating NSE at 17:44
Completed NSE at 17:44, 0.00s elapsed
Initiating NSE at 17:44
Completed NSE at 17:44, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 588.92 seconds
 ```
 