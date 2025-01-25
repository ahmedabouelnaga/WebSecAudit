## Part2 Vulnerability Proof of Concept 
## SQL Injection Vulnerability
File Name:views.py
Lines: 12, 46, and 70 
12. insert_db(app, 'insert into log (username,action,user_agent) values ("{}","{}","{}")'.format(username, action, user_agent))
46. user = query_db(app, 'select * from users where username = "{}" LIMIT 1'.format(username))[0]
70. user = query_db(app, 'select * from users where username = ? limit 1', [username])
Why it is vulunerable:
12. This line directly injects inputs controlled by the user such as username, action, and user_agent into the SQL query using python's .format. If any of the inputs are malicious, it could lead to an SQL injection attack.
46. This line is vilnerable since the value of username is directly supplied by the user. It is formatted into the SQL query without sanitization. This makes the application vulnerable to SQL injection if the username input is malicious SQL code.Moreover, this line is vulnerable since if no user is nfound in the database then accessing [0] on the result will throw an IndexError. This can lead to the internal stack traces being exposed to the user or crash the app.
70. This line is vulnerable since any non parameterized query that involves unsatinized inputs is vulnerable to SQL injection. This function checks if a username exists and is vulnerable to malicious input.

File Name: __init__.py:
Lines: 8 , 25-30, 39, 38-42
8.flag = environ.get("CHALLENGE_FLAG","{the_flag_is_undefined_?ax?d7e?fp?2?8?0}")
25-30. 
    def create_random_string(str_len=8):
    keyspace = ascii_lowercase + digits
    random_string = ""
    for c in range(str_len):
        random_string += choice(keyspace)
    return random_string

Why it is vulnerable:
8. The ? characters in the flag are replaced with random values, however this methodology utilizes a predictable fallback pattern. Therefore, an attacker is able to guess or brute force the flag due to this predictability.It helps the hacker have an easier time to find what the hidden flag is. 
25-30. It is vulnerable due to the fact that the implementation uses a weak method to generate random strings for important security purposes. The choice function isn't cryptographically secure which makes it easier for attackers to guess the generated keys.
39. statement = "INSERT INTO {}({}) VALUES ('{}');".format(app.flag_table,app.flag_column,app.flag). The flag value here is directly injected into the SQL query utilizing the .format(). If the flag has malicious input it can lead to a compromised database. Moreover, this line incorporates variables controlled by the user such as app.flag_table, app.flag_column, and app.flag into the SQL query string using python string formatting. If any of these variables come from sources that can't be trusted then an attacker can make a malicious payload which injects SQL commands which can be harmful.

38-42.It is vulnerable because The app.flag_table, app.flag_column, and app.flag variables are inserted directly into the SQL query string without any sanitization or escaping. If an attacker gets conmtrol over any of these variables through the user input or some sort of tampering with the configuration then it can lead to the attacker being able to craft a malicious input to manipulate the SQL query.If app.flag contains malicious input, it could alter the structure of the SQL query.There is a lack of parameterization.



### Instructions

There is a vulnerable instance of the part2 problem
hosted at the following URL:

http://localhost:8000/
 
Update the file `poc.sh` with a script
that displays the "flag" for this challenge.

The flag is stored in the `flag` field 
in the table titled `flag`. 

The flag is also stored
as the User-Agent of the admin user, which
is visible to anyone who is successfully
logged in as admin. 

### Additional Guidance

If your script requires any dependencies, add the
commands to install these dependencies to the script.
Assume you are running in a base install of
Ubuntu 20.04 operating system with python3 installed when
planning for dependencies. 

When grading, the script will be executed
from the current directory. 
If you want to write your proof of concept in 
python or a different language, place the
python script in this same folder and
execute them directly. For example, if your
script is labeled `myscript.py`, place that
file in this folder, and then update
`poc.sh` with:

```
python3 myscript.py
```

