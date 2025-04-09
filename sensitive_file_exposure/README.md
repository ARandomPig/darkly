# Sensitive file exposure 

## How We Found It
in the `/robots.txt` page, there is a page called `/whatever` that is disallowed. when we go to `/whatever`, there is a file called htaccess that we can download. in this file there is just one line : 
```
root:437394baff5aa33daa618be47b75cb49
```
that looks like a user login and a password hashed using md5, so we decrypted it and got the password `qwerty123@`. This is intresting but where shoud we use it ?
there is a page called `/admin`, on this page, there is a login and password prompt, when we enter the username and password found earlier, we get a flag.

## Utility of It
- Leaks credentials that can be used to access restricted areas (like /admin).
- Can lead to full system compromise if reused elsewhere.
- Highlights bad practice of storing sensitive data in web-accessible paths.

## How Can We Patch It
- Never expose sensitive files like `.htaccess`, `.env`, `config.php`, etc.
- Properly configure the web server to deny access to such files.
- Avoid storing plaintext or weakly hashed passwords in accessible locations.
- Use strong hashing algorithms (e.g., bcrypt) and limit access to admin interfaces.
