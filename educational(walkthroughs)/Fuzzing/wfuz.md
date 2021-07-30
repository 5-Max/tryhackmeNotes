```bash


wfuzz -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -H "Host: FUZZ.team.thm" --hw 977 --ip 10.10.120.63 -u "http://10.10.120.63:80"
 



```
