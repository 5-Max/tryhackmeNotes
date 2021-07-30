**Fuzz Faster U Fool**

using seclists

-s  silent




```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.238.246/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.238.246/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

favicon.ico             [Status: 200, Size: 1406, Words: 5, Lines: 2]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
.htaccess               [Status: 403, Size: 289, Words: 21, Lines: 11]
robots.txt              [Status: 200, Size: 26, Words: 3, Lines: 2]
phpinfo.php             [Status: 302, Size: 0, Words: 1, Lines: 1]
index.php               [Status: 302, Size: 0, Words: 1, Lines: 1]
.                       [Status: 302, Size: 0, Words: 1, Lines: 1]
php.ini                 [Status: 200, Size: 148, Words: 17, Lines: 5]
about.php               [Status: 200, Size: 4840, Words: 331, Lines: 109]
.html                   [Status: 403, Size: 285, Words: 21, Lines: 11]
login.php               [Status: 200, Size: 1523, Words: 89, Lines: 77]
.php                    [Status: 403, Size: 284, Words: 21, Lines: 11]
setup.php               [Status: 200, Size: 4067, Words: 308, Lines: 123]
.htpasswd               [Status: 403, Size: 289, Words: 21, Lines: 11]
security.php            [Status: 302, Size: 0, Words: 1, Lines: 1]
.htm                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.htpasswds              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htgroup                [Status: 403, Size: 288, Words: 21, Lines: 11]
wp-forum.phps           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htaccess.bak           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htuser                 [Status: 403, Size: 287, Words: 21, Lines: 11]
.ht                     [Status: 403, Size: 283, Words: 21, Lines: 11]
.htc                    [Status: 403, Size: 284, Words: 21, Lines: 11]
:: Progress: [16243/16243] :: Job [1/1] :: 309 req/sec :: Duration: [0:00:47] :: Errors: 0 ::
```

extension fuzz

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.238.246/indexFUZZ -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt



        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.238.246/indexFUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.phps                   [Status: 403, Size: 290, Words: 21, Lines: 11]
.php                    [Status: 302, Size: 0, Words: 1, Lines: 1]
:: Progress: [39/39] :: Job [1/1] :: 12 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

exclude extensions 

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.238.246/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.238.246/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt
 :: Extensions       : .php .txt 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.html.txt               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.html.php               [Status: 403, Size: 289, Words: 21, Lines: 11]
login.php               [Status: 200, Size: 1523, Words: 89, Lines: 77]
index.php               [Status: 302, Size: 0, Words: 1, Lines: 1]
.htm                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.htm.php                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htm.txt                [Status: 403, Size: 288, Words: 21, Lines: 11]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
config                  [Status: 301, Size: 314, Words: 20, Lines: 10]
docs                    [Status: 301, Size: 312, Words: 20, Lines: 10]
.php                    [Status: 403, Size: 284, Words: 21, Lines: 11]
about.php               [Status: 200, Size: 4840, Words: 331, Lines: 109]
.                       [Status: 302, Size: 0, Words: 1, Lines: 1]
external                [Status: 301, Size: 316, Words: 20, Lines: 10]
.htaccess.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htaccess               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htaccess.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
setup.php               [Status: 200, Size: 4067, Words: 308, Lines: 123]
robots.txt              [Status: 200, Size: 26, Words: 3, Lines: 2]
security.php            [Status: 302, Size: 0, Words: 1, Lines: 1]
phpinfo.php             [Status: 302, Size: 0, Words: 1, Lines: 1]
.php3                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.phtml                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.htc.php                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htc                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.htc.txt                [Status: 403, Size: 288, Words: 21, Lines: 11]
instructions.php        [Status: 200, Size: 14014, Words: 1484, Lines: 263]
.php5                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.html_var_de            [Status: 403, Size: 292, Words: 21, Lines: 11]
.html_var_de.php        [Status: 403, Size: 296, Words: 21, Lines: 11]
.html_var_de.txt        [Status: 403, Size: 296, Words: 21, Lines: 11]
.php4                   [Status: 403, Size: 285, Words: 21, Lines: 11]
server-status           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htpasswd               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htpasswd.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htpasswd.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.html..php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.html..txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.html.html.txt          [Status: 403, Size: 294, Words: 21, Lines: 11]
.html.html.php          [Status: 403, Size: 294, Words: 21, Lines: 11]
.html.html              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htpasswds              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htpasswds.php          [Status: 403, Size: 294, Words: 21, Lines: 11]
.htpasswds.txt          [Status: 403, Size: 294, Words: 21, Lines: 11]
.htm.                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.htm..php               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htm..txt               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htmll                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.htmll.php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htmll.txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.phps                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.html.old.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.old               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html.old.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.ht                     [Status: 403, Size: 283, Words: 21, Lines: 11]
.ht.txt                 [Status: 403, Size: 287, Words: 21, Lines: 11]
.ht.php                 [Status: 403, Size: 287, Words: 21, Lines: 11]
.html.bak.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.bak.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.bak               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htm.htm                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htm.htm.txt            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htm.htm.php            [Status: 403, Size: 292, Words: 21, Lines: 11]
.hta.php                [Status: 403, Size: 288, Words: 21, Lines: 11]
.hta.txt                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htgroup.php            [Status: 403, Size: 292, Words: 21, Lines: 11]
.html1.txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htgroup                [Status: 403, Size: 288, Words: 21, Lines: 11]
.html1                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.htgroup.txt            [Status: 403, Size: 292, Words: 21, Lines: 11]
.hta                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.html1.php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.html.lck               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html.lck.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.lck.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.printable         [Status: 403, Size: 295, Words: 21, Lines: 11]
.html.printable.php     [Status: 403, Size: 299, Words: 21, Lines: 11]
.html.printable.txt     [Status: 403, Size: 299, Words: 21, Lines: 11]
.htm.lck                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htm.lck.txt            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htm.lck.php            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htaccess.bak           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htaccess.bak.php       [Status: 403, Size: 297, Words: 21, Lines: 11]
.htaccess.bak.txt       [Status: 403, Size: 297, Words: 21, Lines: 11]
.html.php               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html.php.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htmls.txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htmls                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.html.php.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htmls.php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htx                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.htx.php                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htx.txt                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htlm                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.htlm.php               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htlm.txt               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htm2                   [Status: 403, Size: 285, Words: 21, Lines: 11]
.htm2.php               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html-.php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htuser.txt             [Status: 403, Size: 291, Words: 21, Lines: 11]
.htuser                 [Status: 403, Size: 287, Words: 21, Lines: 11]
.htuser.php             [Status: 403, Size: 291, Words: 21, Lines: 11]
.html-.txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htm2.txt               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html-                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.htacess                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htacess.txt            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htacess.php            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htm.d                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.htm.d.php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htm.html.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htm.html               [Status: 403, Size: 289, Words: 21, Lines: 11]
.htm.html.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htm.old                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htm.old.php            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htm.old.txt            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htm.d.txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.html-1                 [Status: 403, Size: 287, Words: 21, Lines: 11]
.html-1.txt             [Status: 403, Size: 291, Words: 21, Lines: 11]
.html-1.php             [Status: 403, Size: 291, Words: 21, Lines: 11]
.html.orig.php          [Status: 403, Size: 294, Words: 21, Lines: 11]
.html.orig              [Status: 403, Size: 290, Words: 21, Lines: 11]
.html.orig.txt          [Status: 403, Size: 294, Words: 21, Lines: 11]
.html.sav               [Status: 403, Size: 289, Words: 21, Lines: 11]
.html.sav.php           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html.sav.txt           [Status: 403, Size: 293, Words: 21, Lines: 11]
.html_.php              [Status: 403, Size: 290, Words: 21, Lines: 11]
.html_                  [Status: 403, Size: 286, Words: 21, Lines: 11]
.html_files.php         [Status: 403, Size: 295, Words: 21, Lines: 11]
.html_files             [Status: 403, Size: 291, Words: 21, Lines: 11]
.html_.txt              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htmlpar                [Status: 403, Size: 288, Words: 21, Lines: 11]
.html_files.txt         [Status: 403, Size: 295, Words: 21, Lines: 11]
.htmlpar.php            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htmlpar.txt            [Status: 403, Size: 292, Words: 21, Lines: 11]
.htmlprint              [Status: 403, Size: 290, Words: 21, Lines: 11]
.htmlprint.php          [Status: 403, Size: 294, Words: 21, Lines: 11]
.hts.txt                [Status: 403, Size: 288, Words: 21, Lines: 11]
.htmlprint.txt          [Status: 403, Size: 294, Words: 21, Lines: 11]
.hts                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.hts.php                [Status: 403, Size: 288, Words: 21, Lines: 11]
:: Progress: [168879/168879] :: Job [1/1] :: 374 req/sec :: Duration: [0:07:40] :: Errors: 0 ::
```