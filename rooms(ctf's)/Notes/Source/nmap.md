┌──(kali㉿kali)-[~]
└─$ nmap 10.10.5.99
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-14 14:41 EDT
Nmap scan report for 10.10.5.99
Host is up (0.15s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
10000/tcp open  snet-sensor-mgmt

Nmap done: 1 IP address (1 host up) scanned in 30.24 seconds
 




┌──(kali㉿kali)-[~]
└─$ nmap -Pn -p- --open 10.10.5.99 
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-14 14:42 EDT
Nmap scan report for 10.10.5.99
Host is up (0.12s latency).
Not shown: 45892 closed ports, 19642 filtered ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 346.39 seconds



sudo nmap -sV -sC -p 22,10000

lost it , 