# unfinished  -rooms/Unfinished
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
CCT2019	|	impossible will be there a while, |
 [Fusion Corp](rooms(ctf's)/Unfinished/Fusion%20Corp) | kerbrute - impacket - evil-winrm| got in, need to escalate	|
[linuxModules](educational(walkthroughs)/linuxModules) |   educational
[attacktiveDirect](rooms(ctf's)/Unfinished/attacktiveDirect) | go over again and make better notes
MAL: Malware Introductory |
ffuz | 
Intro to Python |
Mustaccio 

# rooms(ctf's)
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
[Lian Yu](rooms(ctf's)/Lian_Yu)	| fuzz => ftp => exiftool steghide => ssh  |gtfo pkexec
bountyhacker |ftp => hydra => ssh |gtfo tar   Lost?
[Cyborg](rooms(ctf's)/cyborg)	|borg backup => ssh | gtfo bash
[Startup](rooms(ctf's)/startup)		|ftp (writable directory) | ssh (writable cronjob)
brute it	|hydra login => ssh2john | cat Lost?
[Wgel](rooms(ctf's)/wgel)	|	ssh2john => sudo wget | sudoers file
[Charlie's Factory](rooms(ctf's)/charlie's%20factory)| rce => ssh | reading code
[Brooklin99](rooms(ctf's)/brooklyn99)	| easy box quick hydra | gtfo sudo less |
[couchdb](rooms(ctf's)/couchdb)| nosql | running docker |CVE-2017-12636
[for buisness reasons](rooms(ctf's)/forBusinessReasons)| wp rev shell plugin - pivot with msf | mount alpine |

osint|

# rooms(ctf's)/Notes
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
Cage| [nmap](rooms(ctf's)/Notes/Cage/nmap) - [ftp](rooms(ctf's)/Notes/Cage/21) => vigenere => [22](rooms(ctf's)/Notes/Cage/22) Cookie Rev Shell => vigenere  | su rootab
Easy Peasy  | [nmap](rooms(ctf's)/Notes/Easy%20Peasy/nmap) - [80](rooms(ctf's)/Notes/Easy%20Peasy/80) - [6498](rooms(ctf's)/Notes/Easy%20Peasy/6498) - [65524](rooms(ctf's)/Notes/Easy%20Peasy/65524) |cronjob
Kiba  		| [nmap](rooms(ctf's)/Notes/Kiba/NMAP) - [80](rooms(ctf's)/Notes/Kiba/80) - [5601](rooms(ctf's)/Notes/Kiba/5601)	Kibana 6.5     |components
Madeye's Castle| [nmap](rooms(ctf's)/Notes/Madeye's%20Castle/nmap) - [juicy sqlite(i)](rooms(ctf's)/Notes/Madeye's%20Castle/80) - [22](rooms(ctf's)/Notes/Madeye's%20Castle/22) | gtfo pico(horz) path variable 
Marketplace  | [nmap](rooms(ctf's)/Notes/Marketplace/Nmap) - [80](rooms(ctf's)/Notes/Marketplace/80) - [22](rooms(ctf's)/Notes/Marketplace/22) - cookie stealing(JWT) - sqli mysql |docker mnt
Node	| [nmap](rooms(ctf's)/Notes/Node/nmap)-[deserialization rce](rooms(ctf's)/Notes/Node/8080) | gtfo sudo systemctl|
Year of the Rabbit|	[nmap](rooms(ctf's)/Notes/Year%20of%20the%20Rabbit/nmap) - [80](rooms(ctf's)/Notes/Year%20of%20the%20Rabbit/80) - [21](rooms(ctf's)/Notes/Year%20of%20the%20Rabbit/21) - [22](rooms(ctf's)/Notes/Year%20of%20the%20Rabbit/22)| gtfo sudo vi |CVE-2019-14287-l
Overpass Series| [1](overpass1.md) [2](rooms(ctf's)/Notes/Overpass/overpass2) [3](overpass3.md) 
Tony the tiger | [nmap](rooms(ctf's)/Notes/Tony%20the%20tiger/nmap)-[80](rooms(ctf's)/Notes/Tony%20the%20tiger/80) [8080](rooms(ctf's)/Notes/Tony%20the%20tiger/8080) [22](rooms(ctf's)/Notes/Tony%20the%20tiger/22) |gtfo sudo find|CVE-2015-7501
lazy admin| 
gaming server|
Nax	|	nagios | msf
res|
gitCrumpets|
gitHappens|
wonderland	|	html digging  | pivoting 
Source|
fowsniff |  [nmap](rooms(ctf's)/Notes/Fowsniff/nmap) - [80](rooms(ctf's)/Notes/Fowsniff/80) - [110](rooms(ctf's)/Notes/Fowsniff/110) - [22](rooms(ctf's)/Notes/Fowsniff/22)| **/etc/update-motd.d/**

# Ubuntu-Apache
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
[Daily bugle](rooms(ctf's)/ubuntu-apache/dailybugle/report) |	[[joombla.py]] - john - wp(404) |  gtfo sudo yum
Gamezone    |	sqlmap injecting searchbar | escalation with msf (never worked) // url manipulation we get flag 
Internal	|  Wordpress  | SSH 
Kenobi	|	Samba  // smbclient  //  SSH  (access) |  gtfo SUID
Skynet	|	smbclient // squirrelmail  //  hidden directory that leads to Cuppa CMS  //  upload shell to cuppa | escalate with cronjobs running
Vulnversity	|smbclient |GTFO SUID 
Mr. Robot	|Wordpress hydra // SSH | nmap escalate
Basic Pen Test	|smbclient // Hydra | SSH
tomghost	|tomcat jserv (ajp13)// msf // gpg and asc | gtfo sudo
agentSudo|	hydra // steghide / binwalk | ssh
easyctf		|hydra |ssh 
rootme		|dirsearch // upload php | gtfo  (python and bash)

# Windows
room | 	tools used / initial access	| privesc| CVE   						 
-----|-----------------------------|---------|---
Alfred	|Jenkins (admin:admin) // Invoke-PowerShellTct (reverse shell) | incognito (add user/privilage escalation) 
[Blue](rooms(ctf's)/windows/blue/report)| eternal blue  msf - migrate to print spooler |hashdump - john | CVE-2017-0143
Hackpark | hydra // BlogEngine.net edit post with reverse shell |  escalate with msf 
Ice		|MSF | Kiwi  
Relevant | eternal blue  smb client |
Steel Mountain	|HTTP File Server (HFS)  Rejetto Vuln  |  MSF
		||NO-MSF   //  python ||
		||powerup.ps1  //  winPEAS 
		||AdvancedSystemCareService9
retro	|	rpd with remmina  |(opening browser as admin and then opening prompt as admin)  |CVE-2019-1388

# Educational
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
Capture the Flag 	|	encryption 
Hashing|
Networks|
[Metasploit](educational(walkthroughs)/msf) |
[Privilege Escalation](educational(walkthroughs)/privesc) | linux privesc
[Shells](educational(walkthroughs)/shellz)| nc rlwrap socat msf
[SQL i ](educational(walkthroughs)/sqli) | sqlite
[tmux](educational(walkthroughs)/tmux.png)  |like terminator but more command base
[PrintNightmare](educational(walkthroughs)/PrintNightmare/One%20Page)	|  | |CVE-2021-34527, CVE-2021-1675
[ffuf](ffuf.md) | fuzzer ||
OWASP 10 |||
| |[Owasp and Juice Shop](owaspJuiceShop.md) |
|| [Remediation](Remidiation.md) |

# educational/webapps
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
[authenticate](educational(walkthroughs)/webApps/authenticate)|re register - JWT - no authorization
[avengers](educational(walkthroughs)/webApps/avengers)| flags cookie - ftp - rce 
[lfi](educational(walkthroughs)/webApps/lfi) | lfi => ssh key | gtfo sudo journalctl 
[ssrf](educational(walkthroughs)/webApps/ssrf) | ip2dh.py |  | https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=ssrf
[XXE and XSS](educational(walkthroughs)/webApps/XXEandXSS) | xml refresher - XXE payload  | stored - reflected - DOM | key-logger XSS   
[zth](educational(walkthroughs)/webApps/zth)|SSTI - CSRF - JWT | using public keys | IDOR - API 
[toolrus](toolsrus.md)|dirsearch - hydra | msf (tomcat/Coyote ajp13)
[ignite](educational(walkthroughs)/webApps/Ignite/ignite)	| Fuel CMS 1.4 |  | CVE 2018-16763 RCE
[dogcat](educational(walkthroughs)/webApps/dogcat)| lfi  log poisoning | gtfo sudo env
[toolsrus](educational(walkthroughs)/webApps/toolrus)|	tomcat 7.0 ajp13 manager upload | | CVE-2009-3843 \| CVE-2009-4189 \| CVE-2009-4188 \| CVE-2010-0557

# Buffer Overflow
room | 		exploit language | CVE
-----|-----------------------|-------
buffer overflow | mona
Intro X86|r2
Gate Keeper| rb
Brainstorm| mona
Binex| py in ssh 
Reversing Elf| r2 

