# Finding the Hidden Flag

This is a quick rundown of our school project where we hacked a website (in a controlled lab environment) to find a hidden flag.

## What We Did

- **Starting Point:**  
  We began at the `.hidden` directory, which was kept out of search engines by the `robots.txt` file.

- **How It Worked:**  
  We built a script that went through each subdirectory looking for a README file. It checked the last byte of the file to spot any unusual values. If the byte didn't match the normal pattern, we knew we had found the flag.

- **Speeding Things Up:**  
  We used multi-threading so that multiple pages could be checked at once, which made the process much faster.

## Takeaway

This project taught us how to combine directory traversal with threading and basic HTML parsing to uncover hidden information. Check out the repo for the full code!
