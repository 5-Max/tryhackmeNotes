### getent

Usage: `getent [OPTION...] database [key ...]`
Get entries from administrative database.

  -i, --no-idn               disable IDN encoding
  -s, --service=CONFIG       Service configuration to be used
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.

Supported databases:
ahosts ahostsv4 ahostsv6 aliases ethers group gshadow hosts initgroups
netgroup networks passwd protocols rpc services shadow

### create user:

Usage: `getent [OPTION...] database [key ...]`
Get entries from administrative database.

  -i, --no-idn               disable IDN encoding
  -s, --service=CONFIG       Service configuration to be used
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.

Supported databases:
ahosts ahostsv4 ahostsv6 aliases ethers group gshadow hosts initgroups
netgroup networks passwd protocols rpc services shadow

### modifying accounts:
- passwd—permits a regular user to change their password, which in turn, updates the /etc/shadow file.
- chfn—(CHange Full Name), reserved for the super-user (root), modifies the GECOS, or "general information" field.
 -chsh—(CHange SHell) changes the user's login shell. However, available choices will be limited to those listed in /etc/shells; the administrator, on the other hand, is not bound by this restriction and can set the shell to any program chosen.
- chage—(CHange AGE) allows the administrator to change the password expiration settings by passing the user name as an argument or list current settings using the -l user option. Alternatively, you can also force the expiration of a password using the passwd -e user command, which forces the user to change their password the next time they log in.
- 
### groups

The addgroup and delgroup commands add or delete a group, respectively. The groupmod command modifies a group's information (its gid or identifier). The command gpasswdgroup changes the password for the group, while the gpasswd -r group command deletes it.



