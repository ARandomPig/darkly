# Local File Inclusion to Get the Flag

## How We Found It  
There was a Local File Inclusion (LFI) vulnerability in the `page` parameter. By messing with the URL and using a bunch of `../`, we can directly go at the root 
of the machine and manage to access `/etc/passwd`.
The flag was hidden in that file and popped up in an alert when we accessed it with the payload:
```
http://10.12.248.148/?page=../../../../../../../../../../../../../../../../../../../../etc/passwd`
```
## Utility of It  
LFI is actually a serious vulnerability in real-world applications. It can let attackers read sensitive files on the server (like config files, database credentials, or even source code), and sometimes it can be chained with other exploits to get full system access.

## How Can We Patch It  
Make sure to sanitize user input and avoid directly including files based on URL parameters. Only allow expected, whitelisted files to be loaded.