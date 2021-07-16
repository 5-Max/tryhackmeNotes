```
┌──(kali㉿kali)-[~]
└─$ sudo echo "ObsJmP173N2X6dOrAgEAL0Vu" > hash.txt
[sudo] password for kali: 
                                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ john hash.txt --format=crypt             
Using default input encoding: UTF-8
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) is 1 for all loaded hashes
Cost 2 (algorithm specific iterations) is 1 for all loaded hashes
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
Warning: Only 78 candidates left, minimum 96 needed for performance.
Proceeding with incremental:ASCII
0g 0:00:00:20  3/3 0g/s 119157p/s 119157c/s 119157C/s somej15..sompann
Session aborted
                                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ john hash.txt --format=crypt -w /home/kali/Downloads/easypeasy.txt         1 ⨯
Warning: hash encoding string length 15, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 14, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 17, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 38, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 20, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 16, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 18, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 25, type id #0
appears to be unsupported on this system; will not load such hashes.
Using default input encoding: UTF-8
Loaded 28 password hashes with 14 different salts (crypt, generic crypt(3) [?/64])
Cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) is 1 for all loaded hashes
Cost 2 (algorithm specific iterations) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 90 candidates left, minimum 96 needed for performance.
0g 0:00:00:00 DONE (2021-07-08 17:30) 0g/s 12227p/s 171186c/s 342372C/s !@#$%..sss
Session completed
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt --format=crypt --show                               
0 password hashes cracked, 1 left
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt -w /home/kali/Downloads/easypeasy.txt 
Warning: only loading hashes of type "descrypt", but also saw type "tripcode"
Use the "--format=tripcode" option to force loading hashes of that type instead
Warning: only loading hashes of type "descrypt", but also saw type "pix-md5"
Use the "--format=pix-md5" option to force loading hashes of that type instead
Using default input encoding: UTF-8
Loaded 6 password hashes with 4 different salts (descrypt, traditional crypt(3) [DES 256/256 AVX2])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:00 DONE (2021-07-08 17:30) 0g/s 354200p/s 1416Kc/s 2125KC/s 123456..sss
Session completed
                                                                                   
┌──(kali㉿kali)-[~]
└─$ sudo echo "ba/ObsJmP173N2X6dOrAgEAL0Vu" > hash.txt                
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt -w /home/kali/Downloads/easypeasy.txt
Warning: only loading hashes of type "descrypt", but also saw type "tripcode"
Use the "--format=tripcode" option to force loading hashes of that type instead
Warning: only loading hashes of type "descrypt", but also saw type "pix-md5"
Use the "--format=pix-md5" option to force loading hashes of that type instead
Using default input encoding: UTF-8
Loaded 6 password hashes with 4 different salts (descrypt, traditional crypt(3) [DES 256/256 AVX2])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:00 DONE (2021-07-08 17:31) 0g/s 354200p/s 1416Kc/s 2125KC/s 123456..sss
Session completed
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt --format=crypt --show                
Warning: hash encoding string length 27, type id #0
appears to be unsupported on this system; will not load such hashes.
0 password hashes cracked, 0 left
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt --fromat=crypt -w /home/kali/Downloads/easypeasy.txt
Unknown option: "--fromat=crypt"
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt --format=crypt -w /home/kali/Downloads/easypeasy.txt         1 ⨯
Warning: hash encoding string length 27, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 15, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 14, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 17, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 38, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 20, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 16, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 18, type id #0
appears to be unsupported on this system; will not load such hashes.
Warning: hash encoding string length 25, type id #0
appears to be unsupported on this system; will not load such hashes.
Using default input encoding: UTF-8
Loaded 27 password hashes with 13 different salts (crypt, generic crypt(3) [?/64])
Cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) is 1 for all loaded hashes
Cost 2 (algorithm specific iterations) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 90 candidates left, minimum 96 needed for performance.
0g 0:00:00:00 DONE (2021-07-08 17:32) 0g/s 10429p/s 135582c/s 281594C/s !@#$%..sss
Session completed
                                                                                   
┌──(kali㉿kali)-[~]
└─$ john hash.txt --format=crypt --show                               
Warning: hash encoding string length 27, type id #0
appears to be unsupported on this system; will not load such hashes.
0 password hashes cracked, 0 left
```
 