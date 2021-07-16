```
└─$ nmap 10.10.4.21                                  
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-12 11:45 EDT
Nmap scan report for 10.10.4.21
Host is up (0.11s latency).
Not shown: 975 closed ports
PORT      STATE SERVICE
9001/tcp  open  tor-orport
9003/tcp  open  unknown
9009/tcp  open  pichat
9071/tcp  open  unknown
9080/tcp  open  glrpc
9081/tcp  open  cisco-aqos
9090/tcp  open  zeus-admin
9099/tcp  open  unknown
9101/tcp  open  jetdirect
9103/tcp  open  jetdirect
9110/tcp  open  unknown
9200/tcp  open  wap-wsp
9290/tcp  open  unknown
9415/tcp  open  unknown
9418/tcp  open  git
9485/tcp  open  unknown
9500/tcp  open  ismserver
9502/tcp  open  unknown
9503/tcp  open  unknown
9594/tcp  open  msgsys
9595/tcp  open  pds
9878/tcp  open  kca-service
9898/tcp  open  monkeycom
13782/tcp open  netbackup
13783/tcp open  netbackup

Nmap done: 1 IP address (1 host up) scanned in 9.29 seconds
```

[[manual nc]]

```
└─$ nmap 10.10.4.21
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-12 12:43 EDT
Nmap scan report for 10.10.4.21
Host is up (0.099s latency).
Not shown: 916 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
9000/tcp  open  cslistener
9001/tcp  open  tor-orport
9002/tcp  open  dynamid
9003/tcp  open  unknown
9009/tcp  open  pichat
9010/tcp  open  sdr
9011/tcp  open  d-star
9040/tcp  open  tor-trans
9050/tcp  open  tor-socks
9071/tcp  open  unknown
9080/tcp  open  glrpc
9081/tcp  open  cisco-aqos
9090/tcp  open  zeus-admin
9091/tcp  open  xmltec-xmlmail
9099/tcp  open  unknown
9100/tcp  open  jetdirect
9101/tcp  open  jetdirect
9102/tcp  open  jetdirect
9103/tcp  open  jetdirect
9110/tcp  open  unknown
9111/tcp  open  DragonIDSConsole
9200/tcp  open  wap-wsp
9207/tcp  open  wap-vcal-s
9220/tcp  open  unknown
9290/tcp  open  unknown
9415/tcp  open  unknown
9418/tcp  open  git
9485/tcp  open  unknown
9500/tcp  open  ismserver
9502/tcp  open  unknown
9503/tcp  open  unknown
9535/tcp  open  man
9575/tcp  open  unknown
9593/tcp  open  cba8
9594/tcp  open  msgsys
9595/tcp  open  pds
9618/tcp  open  condor
9666/tcp  open  zoomcp
9876/tcp  open  sd
9877/tcp  open  x510
9878/tcp  open  kca-service
9898/tcp  open  monkeycom
9900/tcp  open  iua
9917/tcp  open  unknown
9929/tcp  open  nping-echo
9943/tcp  open  unknown
9944/tcp  open  unknown
9968/tcp  open  unknown
9998/tcp  open  distinct32
9999/tcp  open  abyss
10000/tcp open  snet-sensor-mgmt
10001/tcp open  scp-config
10002/tcp open  documentum
10003/tcp open  documentum_s
10004/tcp open  emcrmirccd
10009/tcp open  swdtp-sv
10010/tcp open  rxapi
10012/tcp open  unknown
10024/tcp open  unknown
10025/tcp open  unknown
10082/tcp open  amandaidx
10180/tcp open  unknown
10215/tcp open  unknown
10243/tcp open  unknown
10566/tcp open  unknown
10616/tcp open  unknown
10617/tcp open  unknown
10621/tcp open  unknown
10626/tcp open  unknown
10628/tcp open  unknown
10629/tcp open  unknown
10778/tcp open  unknown
11110/tcp open  sgi-soap
11111/tcp open  vce
11967/tcp open  sysinfo-sp
12000/tcp open  cce4x
12174/tcp open  unknown
12265/tcp open  unknown
12345/tcp open  netbus
13456/tcp open  unknown
13722/tcp open  netbackup
13782/tcp open  netbackup
13783/tcp open  netbackup

Nmap done: 1 IP address (1 host up) scanned in 22.99 seconds
```


```
┌──(kali㉿kali)-[/hackme/rooms/Notes/Wonderland/Looking Glass]
└─$ nmap -A -sC -T5 --script=vuln 10.10.4.21         
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-12 13:11 EDT
Warning: 10.10.4.21 giving up on port because retransmission cap hit (2).
Nmap scan report for 10.10.4.21
Host is up (0.11s latency).
Not shown: 899 closed ports
PORT      STATE    SERVICE        VERSION
22/tcp    open     ssh            OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| vulners: 
|   cpe:/a:openbsd:openssh:7.6p1: 
|     	EDB-ID:21018	10.0	https://vulners.com/exploitdb/EDB-ID:21018	*EXPLOIT*
|     	CVE-2001-0554	10.0	https://vulners.com/cve/CVE-2001-0554
|     	MSF:ILITIES/UBUNTU-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/SUSE-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/SUSE-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/SUSE-CVE-2019-25017/	5.8	https://vulners.com/metasploit/MSF:ILITIES/SUSE-CVE-2019-25017/	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/REDHAT-OPENSHIFT-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/REDHAT-OPENSHIFT-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/OPENBSD-OPENSSH-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/OPENBSD-OPENSSH-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/IBM-AIX-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/IBM-AIX-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/GENTOO-LINUX-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/GENTOO-LINUX-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/F5-BIG-IP-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/F5-BIG-IP-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/DEBIAN-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/AMAZON_LINUX-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/AMAZON_LINUX-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/AMAZON-LINUX-AMI-2-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/AMAZON-LINUX-AMI-2-CVE-2019-6111/	*EXPLOIT*
|     	MSF:ILITIES/ALPINE-LINUX-CVE-2019-6111/	5.8	https://vulners.com/metasploit/MSF:ILITIES/ALPINE-LINUX-CVE-2019-6111/	*EXPLOIT*
|     	EXPLOITPACK:98FE96309F9524B8C84C508837551A19	5.8	https://vulners.com/exploitpack/EXPLOITPACK:98FE96309F9524B8C84C508837551A19	*EXPLOIT*
|     	EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97	5.8	https://vulners.com/exploitpack/EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97	*EXPLOIT*
|     	EDB-ID:46516	5.8	https://vulners.com/exploitdb/EDB-ID:46516	*EXPLOIT*
|     	CVE-2019-6111	5.8	https://vulners.com/cve/CVE-2019-6111
|     	SSH_ENUM	5.0	https://vulners.com/canvas/SSH_ENUM	*EXPLOIT*
|     	PACKETSTORM:150621	5.0	https://vulners.com/packetstorm/PACKETSTORM:150621	*EXPLOIT*
|     	MSF:AUXILIARY/SCANNER/SSH/SSH_ENUMUSERS	5.0	https://vulners.com/metasploit/MSF:AUXILIARY/SCANNER/SSH/SSH_ENUMUSERS	*EXPLOIT*
|     	EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0	5.0	https://vulners.com/exploitpack/EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0	*EXPLOIT*
|     	EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283	5.0	https://vulners.com/exploitpack/EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283	*EXPLOIT*
|     	EDB-ID:45939	5.0	https://vulners.com/exploitdb/EDB-ID:45939	*EXPLOIT*
|     	CVE-2018-15919	5.0	https://vulners.com/cve/CVE-2018-15919
|     	CVE-2018-15473	5.0	https://vulners.com/cve/CVE-2018-15473
|     	1337DAY-ID-31730	5.0	https://vulners.com/zdt/1337DAY-ID-31730	*EXPLOIT*
|     	EDB-ID:45233	4.6	https://vulners.com/exploitdb/EDB-ID:45233	*EXPLOIT*
|     	MSF:ILITIES/OPENBSD-OPENSSH-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/OPENBSD-OPENSSH-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP9-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP8-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP5-CVE-2020-14145/	*EXPLOIT*
|     	MSF:ILITIES/F5-BIG-IP-CVE-2020-14145/	4.3	https://vulners.com/metasploit/MSF:ILITIES/F5-BIG-IP-CVE-2020-14145/	*EXPLOIT*
|     	CVE-2020-14145	4.3	https://vulners.com/cve/CVE-2020-14145
|     	CVE-2007-2768	4.3	https://vulners.com/cve/CVE-2007-2768
|     	CVE-2019-6110	4.0	https://vulners.com/cve/CVE-2019-6110
|     	CVE-2019-6109	4.0	https://vulners.com/cve/CVE-2019-6109
|     	CVE-2018-20685	2.6	https://vulners.com/cve/CVE-2018-20685
|     	PACKETSTORM:151227	0.0	https://vulners.com/packetstorm/PACKETSTORM:151227	*EXPLOIT*
|     	EDB-ID:46193	0.0	https://vulners.com/exploitdb/EDB-ID:46193	*EXPLOIT*
|     	1337DAY-ID-32009	0.0	https://vulners.com/zdt/1337DAY-ID-32009	*EXPLOIT*
|_    	1337DAY-ID-30937	0.0	https://vulners.com/zdt/1337DAY-ID-30937	*EXPLOIT*
311/tcp   filtered asip-webadmin
2190/tcp  filtered tivoconnect
2909/tcp  filtered funk-dialout
3011/tcp  filtered trusted-web
3370/tcp  filtered satvid-datalnk
3659/tcp  filtered apple-sasl
3827/tcp  filtered netmpi
5718/tcp  filtered dpm
5910/tcp  filtered cm
8011/tcp  filtered unknown
8085/tcp  filtered unknown
8290/tcp  filtered unknown
9000/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9001/tcp  open     ssh            Dropbear sshd (protocol 2.0)
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_sslv2-drown: 
9002/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9003/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9009/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9010/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9011/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9040/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9050/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9071/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9080/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9081/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9090/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9091/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9099/tcp  filtered unknown
9100/tcp  filtered jetdirect
9101/tcp  open     jetdirect?
9102/tcp  open     jetdirect?
9103/tcp  open     jetdirect?
9110/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9111/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9200/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9207/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9220/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9290/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9415/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9418/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9485/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9500/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9502/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9503/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9535/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9575/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9593/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9594/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9595/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9618/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9666/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9876/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9877/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9878/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9898/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9900/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9917/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9929/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9943/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9944/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9968/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9998/tcp  open     ssh            Dropbear sshd (protocol 2.0)
9999/tcp  open     ssh            Dropbear sshd (protocol 2.0)
10000/tcp open     ssh            Dropbear sshd (protocol 2.0)
|_http-vuln-cve2006-3392: ERROR: Script execution failed (use -d to debug)
10001/tcp open     ssh            Dropbear sshd (protocol 2.0)
10002/tcp open     ssh            Dropbear sshd (protocol 2.0)
10003/tcp open     ssh            Dropbear sshd (protocol 2.0)
10004/tcp open     ssh            Dropbear sshd (protocol 2.0)
10009/tcp open     ssh            Dropbear sshd (protocol 2.0)
10010/tcp open     ssh            Dropbear sshd (protocol 2.0)
10012/tcp open     ssh            Dropbear sshd (protocol 2.0)
10024/tcp open     ssh            Dropbear sshd (protocol 2.0)
10025/tcp open     ssh            Dropbear sshd (protocol 2.0)
10082/tcp open     ssh            Dropbear sshd (protocol 2.0)
10180/tcp open     ssh            Dropbear sshd (protocol 2.0)
10215/tcp open     ssh            Dropbear sshd (protocol 2.0)
10243/tcp open     ssh            Dropbear sshd (protocol 2.0)
10566/tcp filtered unknown
10616/tcp open     ssh            Dropbear sshd (protocol 2.0)
10617/tcp open     ssh            Dropbear sshd (protocol 2.0)
10621/tcp open     ssh            Dropbear sshd (protocol 2.0)
10626/tcp open     ssh            Dropbear sshd (protocol 2.0)
10628/tcp filtered unknown
10629/tcp open     ssh            Dropbear sshd (protocol 2.0)
10778/tcp open     ssh            Dropbear sshd (protocol 2.0)
11110/tcp open     ssh            Dropbear sshd (protocol 2.0)
11111/tcp open     ssh            Dropbear sshd (protocol 2.0)
11967/tcp open     ssh            Dropbear sshd (protocol 2.0)
12000/tcp open     ssh            Dropbear sshd (protocol 2.0)
12174/tcp open     ssh            Dropbear sshd (protocol 2.0)
12265/tcp open     ssh            Dropbear sshd (protocol 2.0)
12345/tcp open     ssh            Dropbear sshd (protocol 2.0)
13456/tcp open     ssh            Dropbear sshd (protocol 2.0)
13722/tcp open     ssh            Dropbear sshd (protocol 2.0)
13782/tcp open     ssh            Dropbear sshd (protocol 2.0)
13783/tcp open     ssh            Dropbear sshd (protocol 2.0)
14000/tcp filtered scotty-ft
20828/tcp filtered unknown
35500/tcp filtered unknown
48080/tcp filtered unknown
50636/tcp filtered unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 69.23 seconds
                                                                                   
┌──(kali㉿kali)-[/hackme/rooms/Notes/Wonderland/Looking Glass]
```