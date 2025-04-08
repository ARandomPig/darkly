# Client side validation bypass

## How We Found It
On the home page, there is a link to a survey page. this page has a list of subject, an average score and a number of vote. We can give a grade between 0 and 10.  
But what if we change in the html page, the value of a score and put something bigger than 10, can we put a grade of 1000 ?  
Yes we can, and we get a flag.

## Utility of It
This allows an attacker to:
- Submit invalid or malicious data (e.g., score > 10).
- Manipulate application logic (e.g., gain unfair advantage or retrieve flags).
- Potentially exploit further vulnerabilities if the data is used insecurely elsewhere (e.g., SQL injection, XSS).


## How Can We Patch It
- Validate all input on the server side regardless of client-side checks.
- Enforce boundaries (e.g., score must be between 0 and 10) on the backend.
- Use a schema validation library or built-in mechanisms to reject bad data.
- Never trust client-side data blindly — browsers can be manipulated.
