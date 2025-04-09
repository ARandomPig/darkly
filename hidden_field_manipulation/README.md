# Hidden Field Manipulation

## How We Found It
On the sign-in page, there is a I forgot my password. This page contains just a submit button.
when I open the html of the page, there is a hidden field, this hidden field contains an email.
when we change the email and click submit, we get a flag.

## Utility of It
- Lets an attacker change internal data (like an email) sent to the server.
- Can lead to unauthorized access, data leaks, or in this case, retrieving a flag.
- Highlights trust in client-side values, which should never be trusted.

## How Can We Patch It
- Never rely on hidden fields for sensitive logic (e.g., user identity, permissions).
- Always validate input server-side against the authenticated user/session.
- Use server-side state instead of hidden form values when possible.
- If form fields must be used, consider signing or encrypting them (with care).
