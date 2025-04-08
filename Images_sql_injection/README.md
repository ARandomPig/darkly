# SQL Injection to Retrieve the Flag

## How We Found It  
The vulnerable page was:  
`http://10.12.248.148/?page=searchimg`  
It asked for an image ID and displayed the corresponding title and url. We guessed that the backend was using a SQL query like:  
```sql
SELECT title, url FROM list_images WHERE id = $user_input;
```

Since the user input wasn’t sanitized, we tried injecting:
```sql
1 OR 1=1
```
Which made the `WHERE` clause always true and listed all images. That’s when we noticed a suspicious image titled "Hack me ?".

We then injected another query to list all columns in the list_images table, something like:

```sql
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=CHAR(108, 105, 115, 116, 95, 105, 109, 97, 103, 101, 115)
```

Here we can use the `UNION` to show totally different sql result from the hardcoded one in the remote machine. We also needed to add a `, NULL` because both `SELECT` of an `UNION` needs to have the same amount of columns shown.

Among the columns, we found `comment`. So we targeted the image with `title='Hack me ?'` and dumped their comment.

Final SQL Payload:
```sql
1 UNION SELECT title, comment FROM list_images WHERE id=5
```

Here’s what we got:

- **Comment**: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

We followed the instructions, decrypted the password, lowercased it, hashed it with SHA256… and boom: we got the flag.

## Utility of It

SQL injection is extremely dangerous in real-world apps. It can let attackers access, modify, or delete database content. In our case, we used it to explore the DB structure and steal sensitive info (the flag), but in the wild, it could mean full data leaks or even remote code execution.

## How Can We Patch It

Never trust user input. Always use prepared statements or parameterized queries, and validate the type and format of incoming data. Don’t build SQL queries by directly concatenating user-provided values.