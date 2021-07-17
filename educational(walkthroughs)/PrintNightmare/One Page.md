The Windows PrintNightmare vulnerability is an easy exploit to execute, like three minutes easy.  It uses the print spooler service, which is conveniently running by default.  And is a one shot ticket to root privilege.  So in three minutes (not counting the two minutes it takes metasploit to load), I could have access to your system.  What could possibly happen after that? For a personal user it could include denial of service, compromised credentials, and malware install to name a few.  For a corporation the risk would be compromised social security numbers of employees, or credit card numbers of customers.

For the personal user this service is running by default.  So since there is no fix, we need to turn the service off.  It is interesting that we are asking users to open a command prompt and run it as administrator and type commands into a big black screen.  The real question is, how am I going to hack into my neighbors print spooler? It's running locally, the user would have to click on a link.  So that goes more into a social engineering attack than a remote code execution of a service.  

For a small or big business that is running a domain control, the inbound remote printing feature needs to be disabled through a group policy and restart the service.  We will see in a few weeks what this causes, but my feeling is that there will be many IT tickets.  



