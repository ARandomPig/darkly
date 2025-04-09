# Headers manipulation 

## How We Found It
the page where this was, is a little bit hidden, to go to this page, you have to click on the copyright notice in the footer. this page has nothing weird but when we open the html of the page, there is a comment saying :
```
You must come from : "https://www.nsa.gov/".
```
and another comment saying : 
```
Let's use this browser : "ft_bornToSec". It will help you a lot.
```
so using curl, I changed the `Referer` and `User-Agent` headers with this command :
```
curl "http://10.12.248.155/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec"
```

## Utility of It
- Lets an attacker bypass access restrictions by faking headers like Referer or User-Agent.
- Can expose hidden or restricted content (like flags) without proper authentication.
- Shows over-reliance on easily spoofed client headers.

## How Can We Patch It
- Never trust client-controlled headers for access control.
- Use proper authentication and authorization mechanisms (e.g., sessions, tokens).
- If headers must be checked, combine them with server-side checks.
- Don’t leak hints or secrets in HTML comments.
