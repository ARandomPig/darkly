# XSS Vulnerability in the Clickable Image

## How We Found It  
On the homepage, we noticed a clickable image that led to a strange page at:  
`http://10.11.248.192/?page=media&src=nsa`  
At first, we suspected several issues, but then we saw our input was being injected inside an object's `data` attribute.  
We tried a simple `javascript:alert(1)` payload, but it was blocked by JavaScript sanitization. Next, we exploited the unsanitized `data:text/html` scheme by injecting HTML directly for example, using:

```html
data:text/html,<h1>salut</h1>
```

Finally, we went for a more sophisticated payload:  

```html
data:text/html,<script>alert("XSS");</script>
```
This worked and showed an alert but didn’t trigger the flag system. We then encoded the script payload in base64 to bypass a sort of hardcoded "script" detection:

```html
data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ+Cg==
```

Since the `+` character was being replaced by a space during URL encoding, we encoded the entire payload, resulting in:  

```html
data%3Atext%2Fhtml%3Bbase64%2CPHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ%2BCg%3D%3D
```

This final payload delivered the flag.

## Utility of It  
XSS vulnerabilities can be extremely dangerous in real-world scenarios. They allow attackers to inject and execute arbitrary HTML or JavaScript in the browsers of other users. This can lead to session hijacking, defacement, or even full account takeover, making them a critical issue in web security.

## How Can We Patch It  
To fix this vulnerability, ensure that all user inputs injected into the page are properly sanitized and encoded, especially when used in sensitive attributes like `data`. Using Content Security Policy (CSP) headers can also help mitigate the impact of any XSS attacks that slip through.
