```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.78.249         
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-19 16:11 EDT
Nmap scan report for 10.10.78.249
Host is up (0.10s latency).
Not shown: 989 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
1090/tcp open  ff-fms
1091/tcp open  ff-sm
1098/tcp open  rmiactivation
1099/tcp open  rmiregistry
4446/tcp open  n1-fwp
5500/tcp open  hotline
8009/tcp open  ajp13
8080/tcp open  http-proxy
8083/tcp open  us-srv

Nmap done: 1 IP address (1 host up) scanned in 16.56 seconds
``` 

```bash      
┌──(kali㉿kali)-[~]
└─$ nmap -A -sV -p8080 10.10.78.249                
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-19 16:12 EDT
Nmap scan report for 10.10.78.249
Host is up (0.10s latency).

PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
| http-methods: 
|_  Potentially risky methods: PUT DELETE TRACE
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache-Coyote/1.1
|_http-title: Welcome to JBoss AS

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.98 seconds
```

```bash
┌──(kali㉿kali)-[~]
└─$ nmap -A -sV -p80 10.10.78.249 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-19 17:14 EDT
Nmap scan report for 10.10.78.249
Host is up (0.12s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-generator: Hugo 0.66.0
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Tony&#39;s Blog

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.80 seconds
```