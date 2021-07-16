# unfinished  -rooms/Unfinished
room | 		tools used / initial access		| privesc |CVE
-----|--------------------------------------|---------|-----
CCT2019	|	impossible will be there a while, |
[[Fusion Corp]]	| got in, need to escalate	|
[[linuxModules]] |   educational
[[attacktiveDirect]] | go over again and make better notes
MAL: Malware Introductory |

# rooms(ctf's)
room | 		tools used / initial access	| privesc | CVE
------|----------|---------------
[[Lian_Yu]]	| fuzz => ftp => exiftool steghide => ssh  |gtfo pkexec
bountyhacker |ftp => hydra => ssh |gtfo tar   where is this file?
[[cyborg]]		|borg backup => ssh | gtfo bash
[[startup]]		|ftp (writable directory) | ssh (writable cronjob)
brute it	|hydra login => ssh2john | cat 
[[wgel]]	|	ssh2john => sudo wget | sudoers file
[[charlie's factory]]| rce => ssh | reading code
osint|

# rooms(ctf's)/Notes
room | 		tools used / initial access	| privesc | CVE
------|----------|---------------
Cage	| [nmap](rooms(ctf's)/Notes/Cage/nmap) - [ftp](rooms(ctf's)/Notes/Cage/21) => vignere => [22](rooms(ctf's)/Notes/Cage/22) Cookie Rev Shell => vigeniere  | su rootab
Easy Peasy   | [nmap](rooms(ctf's)/Notes/Easy%20Peasy/nmap) - [80](rooms(ctf's)/Notes/Easy%20Peasy/80) - [6498](rooms(ctf's)/Notes/Easy%20Peasy/6498) - [65524](rooms(ctf's)/Notes/Easy%20Peasy/65524) |cronjob
Kiba  		| [nmap](rooms(ctf's)/Notes/Kiba/NMAP) - [80](rooms(ctf's)/Notes/Kiba/80) - [5601](rooms(ctf's)/Notes/Kiba/)	Kibana 6.5     |components
Madeye's Castle|
Marketplace  | cookie stealing // sqli |docker mnt
Node	|very messed up room  // room vuln-net series
Year of the Rabbit|	encryption | sudo -l
Brooklin99	|
couchdb|
for buisness reasons|
lazy admin|
gaming server|
Nax	|	nagios | msf
res|
gitCrumpets|
gitHappens|
wonderland	|	html digging  | pivoting 
Year of the Rabbit|

Source|


# Ubuntu-Apache
room | 		tools used / initial access	| privesc | CVE
------|----------|---------------
Daily bugle |	joombla  //  reverse.php  |  SSH  
Gamezone |	sqlmap injecting searchbar  // reverse ssh port | escalation with msf (never worked) // url manipulation we get flag 
Internal	|Wordpress  | SSH 
Kenobi	|	Samba  // smbclient  //  SSH  (access) |  SUID (escalating)
Skynet	|	smbclient // squirrelmail  //  hidden directory that leads to Cuppa CMS  //  upload shell to cuppa | escalate with cronjobs running
Vulnversity	|smbclient |GTFO SUID 
Mr. Robot	|Wordpress hydra // SSH | nmap escalate
Basic Pen Test	|smbclient // Hydra | SSH
tomghost	|tomcat jserv (ajp13)// msf // gpg and asc | gtfo sudo
agentSudo|	hydra // steghide / binwalk | ssh
easyctf		|hydra |ssh 
rootme		|dirsearch // upload php | gtfo  (python and bash)



# Windows
room | 		tools used / initial access	| privesc | CVE
------|----------|---------------

Alfred		Jenkins (admin:admin) // Invoke-PowerShellTct (reverse shell) // incognito (add user/privilage escalation) //  			rmdesktop windows 7

Blue		eternal blue  msf  ///  print spooler to escalate and hashdump (john) 

Hackpark	hydra // BlogEngine.net edit post with reverse shell //  escalate with msf 

Ice		MSF // Kiwi  

Relevant	eternal blue  smb client

Steel Mountain	HTTP File Server (HFS)  Rejetto Vuln  //  MSF

		NO-MSF   //  python 

		powerup.ps1  //  winPEAS 

		AdvancedSystemCareService9


retro		rpd with remmina //  CVE-2019-1388  (opening browser as admin and then opening prompt as admin)  







# Educational
room | 		tools used / initial access	| privesc | CVE
------|----------|---------------



Capture the Flag 		encryption 

Hashing

Networks
Overpass Series


MSF

Privesc

Shellz

XSS

sqli

lfi

tmux  like terminator but more command base

overpass series 1,2,3|




# educational/webapps
room | 		tools used / initial access	| privesc | CVE
------|----------|---------------
authenticate|
avengers|
lfi|
ssrf|
XXE and XXS|
zth|SSTI - CSRF - IDOR - 
toolrus	|	dirsearch // hydra | msf (tomcat)
ignite	|	phpbash // |
dogcat| 		lfi  log poisoning |
toolsrus|	tomcat manager upload |

# Buffer Overflow
room | 		exploit language | CVE
------|----------
buffer overeflow | mona
Intro X86|r2
Gate Keeper| rb
Brainstorm| mona
Binex| py in ssh 
Reversing Elf| r2 

