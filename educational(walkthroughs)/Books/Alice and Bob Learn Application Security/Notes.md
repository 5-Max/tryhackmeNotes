# 1.  Security Fundamentals
  
### CIA Triad
**Confidentiality** 
Do you have curtains in your bedroom?

**Integrity**
correct and accurate , un-altered, precise , factual (crucial in life support systems)

**Availability** 
Cloud is very reliable on this one

### Assume Breach
preparation and design to ensure that if someone gains access you would be able to detect and respond quickly

### Insider Threats
individual has approved access and can be malicious or accidental which can negatively affect one or more of the CIA aspects of your system

### Defense in Depth
multiple layers of security
Software: 
-  having security requirements
-  threat modeling
-  secure coding

Network:
-  monitoring
-  having a SIEM (Security information and event management)
-  IPS / IDS (prevention and detection)
-  tools to find and stop intruders (maybe honeypot to attract and detect)
-  firewalls

Physical:
-  locks
-  video cameras
-  gates
-  guard dogs
-  motion sensors
-  alarms

### Least Privilege
"Giving users exactly how much access and control they need to do their jobs, but nothing more"
-  Software developers and system administrators are attractive targets

### Supply Chain Security
-  frameworks
-  libraries we call
-  APIs
-  verify that dependencies are safe to use

2018 Node.js module called event-stream stole bitcoin from copay wallets

### Security by Obscurity
Out of sight, out of mind

Obfuscation - hard to understand or read 
-  encoding
-  XOR
-  deploying a server with no domain name

### Security by being Open
not very efficient, more eyes, maybe someone will report for bounty, can go south quick

### Attack Surface Reduction
-  remove anything that is un required 
-  don't publish features that are not fully implemented

### Hard Coding
-  programming values into code rather than getting from user input
-  values are sensitive in nature (passwords, api keys, hashes, )
-  if you find one example, need to search entire app, 

### Never trust, Always Verify
-  verify api is the api is supposed to be
-  api sending data, well sanitize it or validate data is what you expect it to be
-  every single page should have re authentication not one time authentication
-  session management, continue to validate it's the same user
-  internal data also needs to be validated to prevent XSS
-  when an api #1 calls api #2 that second call needs to be authenticated,

### Usable Security
-  so secure I can't log in, 
-  examples fingerprint, facial recognition make security easy and accessible 
-  passphrase password  1L0v3P@st@ 
-  password managers

### Factors of Authentication
1.  You have (computer, phone, youbi key)
2.  You are (fingerprint, DNA)
3.  You know (password, security questions, SS number)

One Factor
-  username:password

Multi Factor
- username:password
- token (code sent to phone) , Thumb print, 

reccomended authentication app over sms text message 

# Exercises
1.  If Bob sets the settings in his pacemaker to not broadcast SSID, that would be an example of Security by Obscurity
2.  Really don't get it , 
3.  Captcha is for bot and not humans, it avoids span in the website, polluting blogs with advertisement.  
It definitely is a nuisance and apparently can be bypassed a number of ways.  I sometimes have a hard time spotting the palm tress.
4.  Face recognition was a very good implementation of usable security before covid-19, then with a mask on this 
technology became hard to use, and fingerprint makes sense more sense now.
5.  url parameters would be input from a search bar, and most definitely needs to be sanitized.
6.  Confidentiality - employee steals and sell trade secret 
7.  Integrity - smart refrigerator gets hacked and milk goes bad 
8.  Availability - A/C thermostat gets hacked and turned off 
9.  

