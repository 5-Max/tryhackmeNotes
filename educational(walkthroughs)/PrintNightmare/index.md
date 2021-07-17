PrintNightmare rce

so you have to confirm that the update worked, that seems odd.  who is going to do that?

we have to confirm in the registry keys that 

[[microsoftDocs]] explains it very high above, so what is in the RCE, saw a video where the guy did it in like 2 minutes, 

ok so we upload a reverse shell as root, lovely [[exploit]]

### Why is this a big deal? 
The PrintNightmare vulnerability is a very easy exploit to execute, like three minutes easy.  It uses the print spooler service, which is conveniently running by default.  So in three minutes, I could have access to your system.  What could possibly happen after that? Denial of service is interesting, but let's look for those personal files.  Do I get a bank account login information or very personal pictures and blackmail you.  Execute a fork bomb and watch your system fry, as I look at all your information, and decided what each folder will cost you to get it back.  The cloud backup, "you say", well already went there and deleted your cloud back up.  

### personal user
https://www.computerweekly.com/news/252503494/Should-I-be-worried-about-PrintNightmare
If you are a personal user make sure you update your windows, 

I did find an account unknown user with read and write permission, so clicked deny.


### For the Small Business (what is small, I guess under 5 million in revenue)

Where is print spooler running? as400 , 
https://www.blackhat.com/presentations/bh-europe-06/bh-eu-06-Carmel/bh-eu-06-Carmel.pdf
Interesting, 

Are there computers that don't need to print? if so, then disable them 

`Stop-Service -Name Spooler -Force`

`Set-Service -Name Spooler -StartupType Disabled`

go into group policy and disable client connections, then restart service. 

this will change it to local network traffic, shouldn't this be the default? 


### big corporations 

This one is trickier because of permissions.   First all the groups and users have to have appropriate privilege settings.  The amount of users and groups are at the overwhelming capacity with several group admins.  Yet we are looking for a specific driver.  

Make sure the group policy settings for the Point and Print Restrictions Group Policy is enabled and select show warning and elevation prompt for installing drivers and updating drivers.  







