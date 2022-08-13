# Intro to x86-64 

 tryhackme and the password is reismyfavl33t. To access the machine, SSH into it on port 22. 
 
 
  people either use the AT&T syntax or the Intel Syntax(differences are highlighted here).
  http://web.mit.edu/rhel-doc/3/rhel-as-en-3/i386-syntax.html
  
  good cheat sheet for commands
  https://zachgrace.com/cheat_sheets/radare2/
  
  remember to enter e asm.syntax=att to ensure that you are using the AT&T syntax.
  
  --------------
  [good walkthrough](https://www.megabeets.net/a-journey-into-radare-2-part-1/)

  [The Book](https://book.rada.re/)
  ----------------

## basic workflow:
``` r2 <filename>  ```

i = info

ie = info **entrypoints**

  
```  r2 -d <filename>```
  
a?

e asm.syntax=att;e asm.describe=true

explains for dummies like me `e asm.describe = true`

afl = list all functions


## flags

fs <flagname>; f 
choose flag spage and prints flags it contains

fs * = go back to normal


## Strings

iz =  List strings in data sections

izz = Search for Strings in the whole binary 

where they’re used in the program

`axt @@ str.*`  

a analysis
x cross reference 
t to

The axt command is used to “find data/code references to this address” (see ax?). 

The special operator @@ is like a foreach iterator sign, used to repeat a command over a list of offsets (see @@?), 

and str.* is a wildcard for all the flags that start with str.

dcu main = continue until main function

## Visual

controls margins
`e scr.utf8=true; e scr.utf8.curvy=true`

R = changes color

To enter visual debugger mode use `Vpp`

p and P cycle through views

s to step over 

c to toggle cursor mode to mark byte range selection 

F2 to set breakpoint 

dr is used to read or write values of the target's general purpose registers. 

: = to input command in visual mode



pdf @main

db `<breakpoint>`

dc to move forward 

ood 'random'   // to turn register ????

endbra64 = NOP 

----------------

from writeup
https://www.goggleheadedhacker.com/blog/post/1

rabin2 -I `<filename>`    // look for arch and language 

rabin2 -z `<filename>`   // list all strings from data section

rabin2 -zz `<filename>`  // shows all strings

r2 `<filename>` 

aa  // analyze binary

s main  // seek main function

v  // visual mode

p  // change to disassembly view


part II

rabin2 -zqq `<filename>` 

r2 `<filename>` 

aaa

s main

VV  //  graph mode  navigate like Vim "HJKL"

==atoi function converts string into integer==

==strcmp function compares==
**if not equal is true (green)**

rax2 `<hexadecimal>`      // converts hexadecimal to integer 

-------------
good cheat sheet of commands
https://hydrasky.com/malware-analysis/reversing-with-radare2/

---------------
### To check for protection against buffer overflow
https://musyokaian.medium.com/dear-qa-tryhackme-walkthrough-1c0a76326f8e

gdb <./name_of_file>

then, `checksec`

--------------
https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture

The 8 GPRs are:
1. Accumulator register **(AX)**. Used in arithmetic operations
2. Counter register **(CX)**. Used in shift/rotate instructions and loops.
3. Data register **(DX)**. Used in arithmetic operations and I/O operations.
4. Base register **(BX)**. Used as a pointer to data (located in segment register DS, when in segmented mode).
5. Stack Pointer register **(SP)**. Pointer to the top of the stack.
6. Stack Base Pointer register **(BP)**. Used to point to the base of the stack.
7. Source Index register **(SI)**. Used as a pointer to a source in stream operations.
8. Destination Index register **(DI)**. Used as a pointer to a destination in stream operations.

Similarly, in the 64-bit version, the 'E' is replaced with an 'R' (register), so the 64-bit version of 'EAX' is called 'RAX'.


screenshot of conversion 


leaq source, destination: this instruction sets destination to the address denoted by the expression in source

addq source, destination: destination = destination + source

subq source, destination: destination = destination - source

imulq source, destination: destination = destination * source

salq source, destination: destination = destination << source where << is the left bit shifting operator

sarq source, destination: destination = destination >> source where >> is the right bit shifting operator

xorq source, destination: destination = destination XOR source

andq source, destination: destination = destination & source

orq source, destination: destination = destination | source


### if1

```
#include <stdio.h>

int main(void){
  int a = 3;
  int b = 4;
  if(a < b){
    a += 5;
  }
  else{
    b += 3;
  }
  return 0;
}
```

- set breakpoint ,,, remember 60   becomes 0x60 which is hexadecimal,,, 


https://www.rapidtables.com/convert/number/hex-to-decimal.html


### Loops
```
#include <stdio.h>

int main(void){
  int a = 4;
  int b = 9;
  int c = 10;
  while(a < 9){
    a = a + 2;
  }
return 0;
}
```


```
#include <stdio.h>

int main(void){
  int a = 4;	ch	
  int b = 9;	8
  int c = 10;	4
  while(a < 9){
    a = a + 2;
  }
return 0;
}
```

### crackme1
```
[0x7f6cf3746090]> pdf @main
/ (fcn) main 280
|   int main (int argc, char **argv, char **envp);
|           ; var int32_t var_54h @ rbp-0x54
|           ; var int32_t var_50h @ rbp-0x50
|           ; var int32_t var_4ch @ rbp-0x4c
|           ; var int32_t var_48h @ rbp-0x48
|           ; var int32_t var_40h @ rbp-0x40
|           ; var int32_t var_38h @ rbp-0x38
|           ; var int32_t var_30h @ rbp-0x30
|           ; var int32_t var_28h @ rbp-0x28
|           ; var int32_t var_12h @ rbp-0x12
|           ; var int32_t var_8h @ rbp-0x8
|           ; arg int32_t arg_40h @ rbp+0x40
|           ; DATA XREF from entry0 (0x55dc4fe1e70d)
|           0x55dc4fe1e7fa      55             pushq %rbp
|           0x55dc4fe1e7fb      4889e5         movq %rsp, %rbp
|           0x55dc4fe1e7fe      4883ec60       subq $0x60, %rsp        ; '`'
|           0x55dc4fe1e802      64488b042528.  movq %fs:0x28, %rax     ; [0x28:8]=-1 ; '(' ; 40
|           0x55dc4fe1e80b      488945f8       movq %rax, var_8h
|           0x55dc4fe1e80f      31c0           xorl %eax, %eax
|           0x55dc4fe1e811      488d3d900100.  leaq str.enter_your_password, %rdi ; 0x55dc4fe1e9a8 ; "enter your password"
|           0x55dc4fe1e818      e863feffff     callq sym.imp.puts      ; int puts(const char *s)
|           0x55dc4fe1e81d      488d45ee       leaq var_12h, %rax
|           0x55dc4fe1e821      4889c6         movq %rax, %rsi
|           0x55dc4fe1e824      488d3d910100.  leaq 0x55dc4fe1e9bc, %rdi ; "%s"
|           0x55dc4fe1e82b      b800000000     movl $0, %eax
|           0x55dc4fe1e830      e89bfeffff     callq sym.imp.__isoc99_scanf ; int scanf(const char *format)
|           0x55dc4fe1e835      c745ac000000.  movl $0, var_54h
|           0x55dc4fe1e83c      488d057c0100.  leaq 0x55dc4fe1e9bf, %rax ; "127"
|           0x55dc4fe1e843      488945c0       movq %rax, var_40h
|           0x55dc4fe1e847      488d05750100.  leaq str.01., %rax      ; 0x55dc4fe1e9c3 ; u"01.\u7257\u6e6f\u2067\u6150\u7373\u6f77\u6472\u5900\u756f\u7627\u2065\u6f67\u2074\u6874\u2065\u6f63\u7272\u6365\u2074\u6170\u7373\u6f77\u6472\u0100\u031b\u3c3b"
|           0x55dc4fe1e84e      488945c8       movq %rax, var_38h
|           0x55dc4fe1e852      488d056a0100.  leaq str.01., %rax      ; 0x55dc4fe1e9c3 ; u"01.\u7257\u6e6f\u2067\u6150\u7373\u6f77\u6472\u5900\u756f\u7627\u2065\u6f67\u2074\u6874\u2065\u6f63\u7272\u6365\u2074\u6170\u7373\u6f77\u6472\u0100\u031b\u3c3b"
|           0x55dc4fe1e859      488945d0       movq %rax, var_30h
|           0x55dc4fe1e85d      488d05610100.  leaq 0x55dc4fe1e9c5, %rax ; u"1.\u7257\u6e6f\u2067\u6150\u7373\u6f77\u6472\u5900\u756f\u7627\u2065\u6f67\u2074\u6874\u2065\u6f63\u7272\u6365\u2074\u6170\u7373\u6f77\u6472\u0100\u031b\u3c3b"
|           0x55dc4fe1e864      488945d8       movq %rax, var_28h
|           0x55dc4fe1e868      488d45ee       leaq var_12h, %rax
|           0x55dc4fe1e86c      4889c7         movq %rax, %rdi
|           0x55dc4fe1e86f      e81cfeffff     callq sym.imp.strlen    ; size_t strlen(const char *s)
|           0x55dc4fe1e874      8945b0         movl %eax, var_50h
|           0x55dc4fe1e877      488d45ee       leaq var_12h, %rax
|           0x55dc4fe1e87b      488d35450100.  leaq 0x55dc4fe1e9c7, %rsi ; "."
|           0x55dc4fe1e882      4889c7         movq %rax, %rdi
|           0x55dc4fe1e885      e836feffff     callq sym.imp.strtok    ; char *strtok(char *s1, const char *s2)
|           0x55dc4fe1e88a      488945b8       movq %rax, var_48h
|       ,=< 0x55dc4fe1e88e      eb4e           jmp 0x55dc4fe1e8de
|      .--> 0x55dc4fe1e890      8b45ac         movl var_54h, %eax
|      :|   0x55dc4fe1e893      4898           cltq
|      :|   0x55dc4fe1e895      488b54c5c0     movq -0x40(%rbp, %rax, 8), %rdx
|      :|   0x55dc4fe1e89a      488b45b8       movq var_48h, %rax
|      :|   0x55dc4fe1e89e      4889d6         movq %rdx, %rsi
|      :|   0x55dc4fe1e8a1      4889c7         movq %rax, %rdi
|      :|   0x55dc4fe1e8a4      e807feffff     callq sym.imp.strcmp    ; int strcmp(const char *s1, const char *s2)
|      :|   0x55dc4fe1e8a9      8945b4         movl %eax, var_4ch
|      :|   0x55dc4fe1e8ac      8345ac01       addl $1, var_54h
|      :|   0x55dc4fe1e8b0      837db400       cmpl $0, var_4ch
|     ,===< 0x55dc4fe1e8b4      7413           je 0x55dc4fe1e8c9
|     |:|   0x55dc4fe1e8b6      488d3d0c0100.  leaq 0x55dc4fe1e9c9, %rdi ; "Wrong Password"
|     |:|   0x55dc4fe1e8bd      e8befdffff     callq sym.imp.puts      ; int puts(const char *s)
|     |:|   0x55dc4fe1e8c2      b8ffffffff     movl $0xffffffff, %eax  ; -1
|    ,====< 0x55dc4fe1e8c7      eb33           jmp 0x55dc4fe1e8fc
|    |`---> 0x55dc4fe1e8c9      488d35f70000.  leaq 0x55dc4fe1e9c7, %rsi ; "."
|    | :|   0x55dc4fe1e8d0      bf00000000     movl $0, %edi
|    | :|   0x55dc4fe1e8d5      e8e6fdffff     callq sym.imp.strtok    ; char *strtok(char *s1, const char *s2)
|    | :|   0x55dc4fe1e8da      488945b8       movq %rax, var_48h
|    | :|   ; CODE XREF from main (0x55dc4fe1e88e)
|    | :`-> 0x55dc4fe1e8de      48837db800     cmpq $0, var_48h
|    | :,=< 0x55dc4fe1e8e3      7406           je 0x55dc4fe1e8eb
|    | :|   0x55dc4fe1e8e5      837dac03       cmpl $3, var_54h
|    | `==< 0x55dc4fe1e8e9      7ea5           jle 0x55dc4fe1e890
|    |  `-> 0x55dc4fe1e8eb      488d3de60000.  leaq str.You_ve_got_the_correct_password, %rdi ; 0x55dc4fe1e9d8 ; "You've got the correct password"
|    |      0x55dc4fe1e8f2      e889fdffff     callq sym.imp.puts      ; int puts(const char *s)
|    |      0x55dc4fe1e8f7      b800000000     movl $0, %eax
|    |      ; CODE XREF from main (0x55dc4fe1e8c7)
|    `----> 0x55dc4fe1e8fc      488b4df8       movq var_8h, %rcx
|           0x55dc4fe1e900      6448330c2528.  xorq %fs:0x28, %rcx
|       ,=< 0x55dc4fe1e909      7405           je 0x55dc4fe1e910
|       |   0x55dc4fe1e90b      e890fdffff     callq sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       `-> 0x55dc4fe1e910      c9             leave
\           0x55dc4fe1e911      c3             retq
[0x7f6cf3746090]> 

```

```
[0x7f3ed774f090]> pdf @sym.imp.puts
/ (fcn) sym.imp.puts 6
|   int sym.imp.puts (const char *s);			looks for s   10 's  is offset, 
| bp: 0 (vars 0, args 0)
| sp: 0 (vars 0, args 0)
| rg: 0 (vars 0, args 0)
|           ; CALL XREFS from main (0x5565ccf1f818, 0x5565ccf1f8bd, 0x5565ccf1f8f2)
\           0x5565ccf1f680      ff2522092000   jmpq 0x5565ccf1f686     ; reloc.puts ; [0x5565cd11ffa8:8]=0x686
```


is this code doing ROT? 

```
[0x559cf256c824]> pdf @sym.imp.__isoc99_scanf
/ (fcn) sym.imp.__isoc99_scanf 6
|   int sym.imp.__isoc99_scanf (const char *format);
| bp: 0 (vars 0, args 0)
| sp: 0 (vars 0, args 0)
| rg: 0 (vars 0, args 0)
|           ; CALL XREF from main (0x559cf256c830)
\           0x559cf256c6d0      ff25fa082000   jmpq 0x559cf256c6d6     ; reloc.__isoc99_scanf ; [0x559cf276cfd0:8]=0x7f0089d59ec0

```

0=0
