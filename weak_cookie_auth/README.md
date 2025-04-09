# Weak auth via cookie

## How We Found It
On all the pages, if we have no cookies, the website gives us a cookie. the cookie is called `i_am_admin` and has this value : 
```
68934a3e9455fa72420237eb05902327
```
That look like a md5 hash. what if I decrypt it.  
this is a hash of `false`.   
what if I hash `true` and set it as the cookie.  
when I do this. on all pages, there is an alert that gives me the flag

## Utility of It
- Allows an attacker to forge an admin session by reverse-engineering or guessing cookie values.
- No need to log in or brute-force credentials — just manipulate a hash.
- Can lead to privilege escalation, access to admin features, or flag retrieval in CTFs.

## How Can We Patch It
- Never rely on easily reversible or guessable values (like md5("true")) for auth.
- Use secure session tokens, randomly generated and validated server-side.
- Store roles (like admin/user) in a server-side session — not in a modifiable cookie.
- Avoid using MD5 for any security-related checks; it's outdated and weak.
- Sign cookies with a HMAC or encrypt them if you must store data client-side.

