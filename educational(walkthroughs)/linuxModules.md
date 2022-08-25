Just a short intro on what's coming ahead:

-  [du](#du)
-  [grep, egrep, fgrep](#grep)
-  [tr](#tr-translate-command)
-  [awk](#awk)
-  sed
-  xargs
-  curl
-  wget
-  xxd
    
    
### du

what files/directories are consuming how much space.

Examples

`du -a /home/ `			will list every file in the /home/ directory with their sizes in KB.

If there's a lot of output you can surely use grep...

`du -a /home/ | grep user `	will list any file/directory whose name is containing the string "user" in it.




### grep

`grep "PATTERN" file.txt`

egrep and fgrep are no different from grep(other than 2 flags that can be used with grep to function as both). 

In simple words, egrep matches the regular expressions in a string, and fgrep searches for a fixed string inside text. 
Now grep can do both their jobs by using -E and -F flag, respectively.


In other terms, grep -E functions same as egrep and grep -F functions same as fgrep.


### Flags Description

`-R`	Does a recursive grep search for the files inside the folders(if found in the specified path for pattern search; else grep won't traverse diretory for searching 		the pattern you specify)

`-h` If you're grepping recursively in a directory, this flag disables the prefixing of filenames in the results.

`-c` This flag won't list you the pattern only list an integer value, that how many times the pattern was found in the file/folder.

`-i` I prefer to use this flag most of the time, this is what specifies grep to search for the PATTERN while IGNORING the case 

`-l` 	will only list the filename instead of pattern found in it.

`-n` It will list the lines with their line number in the file containing the pattern.

`-v` This flag prints all the lines that are NOT containing the pattern

`-E` This flag we already read above... will consider the PATTERN as a regular expression to find the matching strings. 

`-e` The official documentation says, it can be used to specify multiple patterns and if any string matches with the pattern(s) it will list it.

### String Manipulations (STRing OPerationS)


For strops, we have the following tools that I always keep in my arsenal and you should too:

    tr	translate command
    awk	
    sed
    xargs

Other commands to be familiar with:

    sort
    uniq
    
#### tr	translate command
    
```bash
tr [flags] [source]/[find]/[select] [destination]/[replace]/[change]
```


Flags Description
-d	To delete a given set of characters
-t	To concat source set with destination set(destination set comes first; t stands for truncate)
-s	To replace the source set with the destination set(s stands for squeeze)
-c	This is the REVERSE card in this game, for eg. If you specify -c with -d to delete a set of characters then it will delete the rest of the characters leaving the source set which we specified (c stands for complement; as in doing reverse of something)

https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/

` echo "Welcome    To    GeeksforGeeks" | tr -s [:space:] ' '`
 
 Welcome To GeeksforGeeks
 
 

#### awk

awk [flags] [select pattern/find(sort)/commands] [input file]


Note: The `$0` variable points to the whole line.  Also, make sure to use single quotes('') to specify patterns, awk treats double quotes("") as a raw string. To use double quotes make sure that you escape the ($) sign(s) with a backslash (\) each, to make it work properly.

Flags	Description
-F	With this flag you can specify FIELD SEPARATOR (FS), and thus don't need to use the BEGIN rule
-v	Can be used to specify variables(like we did in BEGIN{OFS=":"}
-D	

You can debug your .awk scripts specifying this flag(awk -D script.awk) 
-o	To specify the output file (if no name is given after the flag, the output is defaulted to awkprof.out)

```bash                                            
┌──(kali㉿kali)-[~/Downloads]
└─$ cat awk.txt 
ippsec youtube hackthebox 34024
john youtube ctf 50024
thecybermentor tcmsec courses 25923
liveoverflow youtube ctf 45345
nahamsec hackerone bughunting 12365
stok hackerone bughunting 1234


awk 'BEGIN{FS="" OFS=":"} {print $1,$4}' awk.txt

ippsec:34024
john:50024
thecybermentor:25923
liveoverflow:45345
nahamsec:12365
stok:1234

awk 'BEGIN{ORS=","} {print $1}' awk.txt 

ippsec,john,thecybermentor,liveoverflow,nahamsec,stok,  
```



















