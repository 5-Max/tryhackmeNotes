https://wiki.wireshark.org/CaptureFilters

### operators 
-   and - operator: and / &&
-   or - operator: or / ||
-   equals - operator: eq / ==
-   not equal - operator: ne / !=
-   greater than - operator: gt /  >
-   less than - operator: lt / <

### ARP 
layer 2 
request =1  and reply = 2

`arp.opcope == 1` to search for request

### ICMP (Internet Control Message Protocol)

A type that equals 8 means that it is a request packet, if it is equal to 0 it is a reply packet. When these codes are altered or do not seem correct that is typically a sign of suspicious activity.

The timestamp can be useful for identifying the time the ping was requested it can also be useful to identify suspicious activity in some cases.

### TCP (Transmission Control Protocol)

The main thing that we want to look for when looking at a TCP packet is the sequence number and acknowledgment number.

Within Wireshark, we can also see the original sequence number by navigating to edit > preferences > protocols > TCP > relative sequence numbers (uncheck boxes).

### DNS (Domain Name Service Protocol)

There are a couple of things outlined below that you should keep in the back of your mind when analyzing DNS packets.

-   Query-Response
-   DNS-Servers Only
-   UDP

If anyone of these is out of place then the packets should be looked at further and should be considered suspicious.

### HTTP (Hypertext Transfer Protocol)

Statistics > Protocol Hierarchy  

file > Export Objects > HTTP

Statistics > Endpoints.

 