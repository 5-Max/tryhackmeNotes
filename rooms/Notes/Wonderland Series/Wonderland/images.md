``` bash
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la                 
total 283252
drwxr-xr-x  4 kali kali      4096 Jul 12 15:53  .
drwxr-xr-x 35 kali kali      4096 Jul 12 15:43  ..
-rw-r--r--  1 kali kali   1556347 Jul 12 15:53  alice_door.jpg
-rw-r--r--  1 kali kali   1843670 Jul 12 15:53  alice_door.png
-rw-r--r--  1 kali kali 137120290 Apr 28 09:41  atom-amd64.deb
-rw-r--r--  1 kali kali     13353 Jun 25 16:43  backup.zip
-rw-r--r--  1 kali kali       939 Feb 26 16:28  cacert.der
-rwxr-xr-x  1 kali kali      7192 Jun 27 16:51  crackme1
-rwxr-xr-x  1 kali kali      5884 Jun 27 16:55  crackme2
-rwxr-xr-x  1 kali kali      9632 Jun 27 16:58  crackme3
-rwxr-xr-x  1 kali kali      8740 Jun 27 17:00  crackme4
-rwxr-xr-x  1 kali kali      8968 Jun 27 18:21  crackme5
-rwxr-xr-x  1 kali kali      8635 Jun 27 18:34  crackme6
-rwxr-xr-x  1 kali kali      6372 Jun 27 19:11  crackme7
-rwxr-xr-x  1 kali kali      5884 Jun 27 19:25  crackme8
-rw-r--r--  1 kali kali        65 Jul  9 12:41  hash.txt
drwxr-xr-x  8 kali kali      4096 May 20 20:30  Image-ExifTool-12.26
-rw-r--r--  1 kali kali   4933296 May 25 10:50  Image-ExifTool-12.26.tar.gz
-r-xr-xr-x  1 kali kali   8286607 Apr 29 08:41  kerbrute
-rw-r--r--  1 kali kali      8314 Apr 11 09:53 'max55005500(5).ovpn'
-rw-r--r--  1 kali kali  43603610 Feb 27 10:01  Nessus-8.13.1-debian6_amd64.deb
-rw-r--r--  1 kali kali     31999 Jul 10 12:31  nicBuff.jpeg
-rw-r--r--  1 kali kali     10475 Jul 10 13:04  nicSuit.jpeg
-rwxrwxrwx  1 kali kali  91039614 Jul  7 10:00  Obsidian-0.12.5.AppImage
-rw-r--r--  1 kali kali      1801 Mar  2 09:05  owasp_zap_root_ca.cer
drwxr-xr-x  2 root root      4096 Jul  6 18:58  _PI3T.png-0.extracted
-rw-r--r--  1 kali kali   1460806 May 13 20:34  rustScan.deb
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ binwalk -e alice_door.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1962 x 1942, 8-bit/color RGBA, non-interlaced
91            0x5B            Zlib compressed data, compressed

                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ ls    
 alice_door.jpg              crackme8
 alice_door.png              hash.txt
 _alice_door.png.extracted   Image-ExifTool-12.26
 atom-amd64.deb              Image-ExifTool-12.26.tar.gz
 backup.zip                  kerbrute
 cacert.der                 'max55005500(5).ovpn'
 crackme1                    Nessus-8.13.1-debian6_amd64.deb
 crackme2                    nicBuff.jpeg
 crackme3                    nicSuit.jpeg
 crackme4                    Obsidian-0.12.5.AppImage
 crackme5                    owasp_zap_root_ca.cer
 crackme6                    _PI3T.png-0.extracted
 crackme7                    rustScan.deb
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ cd _alice_door.png.extracted 
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ ls
5B  5B.zlib
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ cat 5B                      
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ cat 5B
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ unzip 5B.zlib > 5B
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of 5B.zlib or
        5B.zlib.zip, and cannot find 5B.zlib.ZIP, period.
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ cat 5B                                                                     9 ⨯
Archive:  5B.zlib
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ binwalk -e alice_door.jpg

General Error: Cannot open file alice_door.jpg (CWD: /home/kali/Downloads/_alice_door.png.extracted) : [Errno 2] No such file or directory: 'alice_door.jpg'

                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ ls                                                                         3 ⨯
5B  5B.zlib
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ cd ..                       
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ binwalk -e alice_door.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
332           0x14C           JPEG image data, JFIF standard 1.02
12721         0x31B1          XML document, version: "1.0"
21743         0x54EF          JPEG image data, JFIF standard 1.02

                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
 alice_door.jpg              crackme8
 alice_door.png              hash.txt
 _alice_door.png.extracted   Image-ExifTool-12.26
 atom-amd64.deb              Image-ExifTool-12.26.tar.gz
 backup.zip                  kerbrute
 cacert.der                 'max55005500(5).ovpn'
 crackme1                    Nessus-8.13.1-debian6_amd64.deb
 crackme2                    nicBuff.jpeg
 crackme3                    nicSuit.jpeg
 crackme4                    Obsidian-0.12.5.AppImage
 crackme5                    owasp_zap_root_ca.cer
 crackme6                    _PI3T.png-0.extracted
 crackme7                    rustScan.deb
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ _alice_door.png.extracted 
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ ls
5B  5B.zlib
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ unzip 5B.zlib > 5B       
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of 5B.zlib or
        5B.zlib.zip, and cannot find 5B.zlib.ZIP, period.
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ unzip --help                                                               9 ⨯
UnZip 6.00 of 20 April 2009, by Debian. Original by Info-ZIP.

Usage: unzip [-Z] [-opts[modifiers]] file[.zip] [list] [-x xlist] [-d exdir]
  Default action is to extract files in list, except those in xlist, to exdir;
  file[.zip] may be a wildcard.  -Z => ZipInfo mode ("unzip -Z" for usage).

  -p  extract files to pipe, no messages     -l  list files (short format)
  -f  freshen existing files, create none    -t  test compressed archive data
  -u  update files, create if necessary      -z  display archive comment only
  -v  list verbosely/show version info       -T  timestamp archive to latest
  -x  exclude files that follow (in xlist)   -d  extract files into exdir
modifiers:
  -n  never overwrite existing files         -q  quiet mode (-qq => quieter)
  -o  overwrite files WITHOUT prompting      -a  auto-convert any text files
  -j  junk paths (do not make directories)   -aa treat ALL files as text
  -U  use escapes for all non-ASCII Unicode  -UU ignore any Unicode fields
  -C  match filenames case-insensitively     -L  make (some) names lowercase
  -X  restore UID/GID info                   -V  retain VMS version numbers
  -K  keep setuid/setgid/tacky permissions   -M  pipe through "more" pager
See "unzip -hh" or unzip.txt for more help.  Examples:
  unzip data1 -x joe   => extract all files except joe from zipfile data1.zip
  unzip -p foo | more  => send contents of foo.zip via pipe into program more
  unzip -fo foo ReadMe => quietly replace existing ReadMe if archive file newer
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ sudo apt install zlib         
[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package zlib
                                                                                   
┌──(kali㉿kali)-[~/Downloads/_alice_door.png.extracted]
└─$ cd ..                                                                    100 ⨯
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
 alice_door.jpg              crackme8
 alice_door.png              hash.txt
 _alice_door.png.extracted   Image-ExifTool-12.26
 atom-amd64.deb              Image-ExifTool-12.26.tar.gz
 backup.zip                  kerbrute
 cacert.der                 'max55005500(5).ovpn'
 crackme1                    Nessus-8.13.1-debian6_amd64.deb
 crackme2                    nicBuff.jpeg
 crackme3                    nicSuit.jpeg
 crackme4                    Obsidian-0.12.5.AppImage
 crackme5                    owasp_zap_root_ca.cer
 crackme6                    _PI3T.png-0.extracted
 crackme7                    rustScan.deb
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ steghide extract -sf alice_door.jpg
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ steghide extract -sf alice_door.jpg                                        1 ⨯
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ cd Image-ExifTool-12.26                                                    1 ⨯
                                                                                   
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ ls          
arg_files     exiftool   lib          META.json                 README
Changes       fmt_files  Makefile.PL  META.yml                  t
config_files  html       MANIFEST     perl-Image-ExifTool.spec
                                                                                   
┌──(kali㉿kali)-[~/Downloads/Image-ExifTool-12.26]
└─$ ./exiftool /home/kali/Downloads/alice_door.jpg
ExifTool Version Number         : 12.26
File Name                       : alice_door.jpg
Directory                       : /home/kali/Downloads
File Size                       : 1520 KiB
File Modification Date/Time     : 2021:07:12 15:53:23-04:00
File Access Date/Time           : 2021:07:12 15:53:24-04:00
File Inode Change Date/Time     : 2021:07:12 15:53:24-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Exif Byte Order                 : Big-endian (Motorola, MM)
Orientation                     : Horizontal (normal)
X Resolution                    : 600
Y Resolution                    : 600
Resolution Unit                 : inches
Software                        : Adobe Photoshop CS3 Macintosh
Modify Date                     : 2008:01:20 01:49:10
Color Space                     : Uncalibrated
Exif Image Width                : 1962
Exif Image Height               : 1942
Compression                     : JPEG (old-style)
Thumbnail Offset                : 332
Thumbnail Length                : 12311
Current IPTC Digest             : 460cf28926b856dab09c01a1b0a79077
Application Record Version      : 2
IPTC Digest                     : 460cf28926b856dab09c01a1b0a79077
Displayed Units X               : inches
Displayed Units Y               : inches
Print Style                     : Centered
Print Position                  : 0 0
Print Scale                     : 1
Global Angle                    : 30
Global Altitude                 : 30
Copyright Flag                  : False
URL List                        : 
Slices Group Name               : De_Alice's_Abenteuer_im_Wunderland_Carroll_pic_03
Num Slices                      : 1
Pixel Aspect Ratio              : 1
Photoshop Thumbnail             : (Binary data 12311 bytes, use -b option to extract)
Has Real Merged Data            : Yes
Writer Name                     : Adobe Photoshop
Reader Name                     : Adobe Photoshop CS3
Photoshop Quality               : 12
Photoshop Format                : Progressive
Progressive Scans               : 3 Scans
XMP Toolkit                     : Adobe XMP Core 4.1-c036 46.276720, Mon Feb 19 2007 22:13:43
Create Date                     : 2008:01:20 01:47:53-05:00
Metadata Date                   : 2008:01:20 01:49:10-05:00
Creator Tool                    : Adobe Photoshop CS3 Macintosh
Format                          : image/jpeg
Color Mode                      : RGB
History                         : 
Instance ID                     : uuid:436B87178CC8DC11A35E97C268772518
Native Digest                   : 256,257,258,259,262,274,277,284,530,531,282,283,296,301,318,319,529,532,306,270,271,272,305,315,33432;75A2F56A7448AE47A140395308BA4302
DCT Encode Version              : 100
APP14 Flags 0                   : [14]
APP14 Flags 1                   : (none)
Color Transform                 : YCbCr
Image Width                     : 1962
Image Height                    : 1942
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 1962x1942
Megapixels                      : 3.8
Thumbnail Image                 : (Binary data 12311 bytes, use -b option to extract)
```