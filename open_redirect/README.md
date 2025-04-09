# Open redirect

## How We Found It
On the footer, there is buttons to go to the twitter, instagram and facebook page of 42. to redirect the links in the href are `?page=redirect&site=<service>`. so we tried changing the site to something else and got a flag

## Utility of It
- Allows attackers to redirect users to arbitrary URLs.
- Can be used for phishing, token theft, or triggering unexpected behavior (like flag reveals in CTFs).
- Often underestimated but can be chained with other bugs.

## How Can We Patch It
- Only allow redirects to a whitelisted set of domains.
- Don’t take the redirect target directly from user input.
- Consider showing a confirmation page before redirecting.
