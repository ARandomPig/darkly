# bypassable xss filter  

## How We Found It
there is a page to leave a feedback at the bottom of the home page.
on this page, there is two fields, name and message, in the message we can't input html, the tags get removed, however in the name field , we can put html.
maybe we can put a script. let's write 
```
<script> alert("hello") </script>
```
There is a limit on the number of chars in the name field, but it's just a html limit, we can just modify it.
it accepted the message but it removed the `<script>` and `</script>` of my message and my name is now `alert("hello")`.  
so it does have some verification but not on everything. Maybe I can put a script on another tag.
let's try this : 
```
<img src="javascript:alert("hello")>
```
It didn't work. the word javascript has been removed from the name. 
let's try without the word javascript : 
```
<img src="a" onerror="alert('hello')">
```
it worked but we didn't get any flag
after asking someone, we found out that this page has a problem.
to get the flag, we have to just enter `script` or just any one of these leters `alertscript`

## Utility of It
- Allows attackers to inject JavaScript into the page.
- Can be used to steal cookies, spoof content, or trigger flags in CTFs.
- Shows how weak or naive filters can be bypassed with creative input

## How Can We Patch It
- Use proper HTML escaping/sanitization libraries (e.g., DOMPurify) instead of blacklists.
- Never trust user input — encode everything before rendering.
- Apply Content Security Policy (CSP) headers to block inline scripts.
- Avoid inserting user input directly into the DOM without sanitizing it.
