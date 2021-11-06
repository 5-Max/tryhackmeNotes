## Top 5
https://medium.com/swlh/5-insecure-coding-practices-you-should-stop-today-99e85d8bdad5

1.  Hard-Coded Credentials (CWE-259, CWE-798) embedding data (id, passwd) directly into source code
	-  tools that check for this are Bandit (SAST tool for python) and Vault by Hashicorp
2.  Improper Exception Handling (CWE-396)
	-  stack traces and other error details

```py
from random import randint
from json import dumps
from flask import abort, Flask, request

app = Flask(__name__)

# username/password map
# really, really never do this
auth_dict = {
    "mark": "1234",
    "dave": "dragon"
}

@app.route("/login")
def new_session():
    try:
        if authenticate(**request.args):
            return dumps({"token": new_session_token()})
    except Exception as ex:
        raise Exception("Login Failed") from ex
    abort(401)

def new_session_token():
    return randint(1000,9999)

def authenticate(username=None, password=None):
    return auth_dict[username] == password

if __name__ == "__main__":
    app.run(debug=True)
```
```bash
# Using a valid login we get back a new session token
> curl "http://127.0.0.1:5000/login?username=mark&password=1234"
... {"token": 2166}

# Using a bad password we get a 401, nice
> curl "http://127.0.0.1:5000/login?username=mark&password=1235"
... <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>401 Unauthorized</title>
    <h1>Unauthorized</h1>
    <p>The server could not verify that you are authorized to access the URL requested. 
    You either supplied the wrong credentials (e.g. a bad password), 
    or your browser doesn't understand how to supply the credentials required.</p>
    
# But if we do something unexpected, like use a username that doesn't exist, boom
> curl "http://127.0.0.1:5000/login?username=marl&password=1234"
... Traceback (most recent call last):
      File "/Users/andrewscott/Dev/WIP/insecure_flask/app2.py", line 17, in new_session
        if authenticate(**request.args):
      File "/Users/andrewscott/Dev/WIP/insecure_flask/app2.py", line 27, in authenticate
        return auth_dict[username] == password
    KeyError: 'marl'

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "/Users/andrewscott/.local/share/virtualenvs/insecure_flask-tEvk0LMc/lib/python3.7/site-packages/flask/app.py", line 2463, in __call__
        return self.wsgi_app(environ, start_response)

      File "/Users/andrewscott/Dev/WIP/insecure_flask/app.py", line 20, in new_session
        raise Exception("Login Failed") from ex
    Exception: Login Failed
 # we see here that we did return the desired exception, but also returned a lot of details we would probably want to keep secret.

```

3.  Lack of Rate Limiting - common in SaaS applications 
	-  prevents DoS
	-  slow the the exfiltration of data if some kind of breach does occur
	-  rate limiting is best near the edge of app in a reverse proxy such as nginx or in a API gateway
4.  Single-Layered Defense - input sanitazion is great but inputs need to be escaped before being stored, executed, or returned.
5.  Improper Logging and Log handling - we want to log errors to help, but loging API keys is probably a bad idea. PII personal identifiable information

## cso online
https://www.csoonline.com/article/2115748/insecure-code--common-vulnerabilities.html

1. Buffer Overflow - not limiting amount of input
2. Format String Vulnerabilities - inputs rogue code into the format string, very similar to buffer overflow
3. Canonicalization - when Y program handles X program's data, it doesn't check for authentication
4. Inadequate privilege checking - program doesn't check every doorway to features
5. Script Injection - sqli
6. Information leakage - poor design, program exposes valuable information.
7. Error handling - subset of Information leakage, the way a program handles an error.  example - e-mail bounces back with type of server, ip, server names, etc. 

## Very sarcastic , trying to be funny
https://owasp.org/www-community/How_to_write_insecure_code
### General Principles
1.  Avoid the tools - false belief that automated tools can be solution
2.  Always use default deny - "Deny that your code can ever be broken"
3.  Be a shark - never stop, leave security problems to operations staff
### Complexity
1.  Distribute security mechanism -  creates inconsistent implementation of security
2.  Spread the wealth - spread out the holes to prevent anyone from finding them
3.  Use dynamic code 
		- reflection - make generic software libraries 
		   https://en.wikipedia.org/wiki/Reflective_programming
		- classloading
		- enable as many plugin's as possible
### Secure Languages
1.  Type safety - keyboard is safe
2.  Secure languages - programming languages that are completely safe
3.  Mix languages - more secure languages must be more secure
### Trust relationship
1.  Rely on security checks done elsewhere
2.  Trust insiders - malicious input only comes from the internet
3.  Code wants to be free - use a repositories to share code
### Logging
1.  debugging nonsense in your logs
2.  stdout
### Encryption
1.  Encryption scheme - who would figure out venigere to rot13,
2.  hard code your keys - same keys everywhere
3.  manuals, who needs them, copy and paste from popular coding site or keep adding bytes until the algorithm stops throwing exceptions.
4.  Pack up your sensitive payload - ,,,
5.  Encryption is hard - client side javascript 
6.  HTTPS - most secure
## Authentication
### Build your own
1.  weak passwords
2.  brute force
3.  session prediction
4.  hashing credentials
### hash
1.  Salt is for pigs
2.  session id in url, log files, 
### Authorization Vs. Authentication
1.  only nerds know the difference
2.  authorization scheme all over 
3.  privilege makes code just work
4.  each developer must decide where authorization decision is made
5.  trust the client - RIA clients and fat clients 
6.  volunteer to authorize access to other systems, 
### Policy
1.  Forget about it, 
2.  let automated tools take care of it
### Input Validation
1.  validation is for suckers - firewall will take care of it, 
2.  validate as many different ways as possible
3.  trust the client - 

### Documentation
1.  why write it, it works
2.  security is just another option, 
3.  don't document how security works
4.  freedom to innovate - 
5.  print is dead

### Coding
1.  Most APIs are safe to assume that they do proper validation, exception handling, logging, and thread safety
2.  Don't use security patterns, best to leave developers to express themselves
3.  Make sure the build process has lots of steps 

### Testing
1.  Testing is overrated
2.  Test with a browser why use a fancy tool like Zed Attack Proxy
3.  Test with only one browser , they all work the same
	1.  build test code in every module
	2.  security warnings are all false alarms

### Libraries
1.  use lots of precompiled libraries 
2.  don't worry about using the latest version of components, 

## DevOps
1.  Automation is enough security
2.  Automated Scanning , why? (Static Analysis, Dynamic Analysis)
3.  Access Control on DevOps system
	1.  IAM roles and how keys are managed don't matter, and make sure you put them in public repo for easy access
4.  Auditing is a waste of money
5.  We'll never lose control of our nodes
6.  CORS (cross-origin resource sharing)
7.  Logging Services, waste of time




