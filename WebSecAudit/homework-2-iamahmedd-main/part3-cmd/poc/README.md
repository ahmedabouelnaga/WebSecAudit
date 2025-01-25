
## Part3 Vulnerability Proof of Concept 

###Command Injection Vulnerability 

File Name:views.py

Line Numbers: 8,9, 24, 25-26, and 28

What the Vulernability is: 
The vulnerability is within the ping_host function where the getoutput function is being used to execute the ping command with the help of the user supplied input or ip without the proper sanitization. To be more specific, the command is made using string formatting"getoutput("ping -c1 '{}'".format(ip))". This methodoloy directly incorporates the user input into a system command which leads to it being vulnerable to command injection attacks. This vulnerability is very important to consider since it gives attackers the ability to run arbitrary commands on the server. They could gain unauthorized access to important files, system configurations, or environment variables.
Why it is vulnerable:
8. response = {"host": ip}. This line is vulnerable since it directly includes input that is provided by the user(ip) into a shell command(ping) without sanitization or validation. So if an attacker submits a malicious payload it can lead to execution of unintended ocmmands which can lead to many consequences. 

9. response["output"] = getoutput("ping -c1 '{}'".format(ip)). It is vulnerable since the user input or ip is directly inserted into the ping command without some sort of validation or sanitization. An attacker can inject malicious shell commands by submitting some sort of crafted IP.
24. ip = request.form.get("ip", None). This is vulnerable since the input ip isn't validated for being a proper IP address or hostname. Due to there being a lack of validation, this can lead to a command injection vulnerability that I mentioned earlier.
25-26. if ip: return ping_host(ip). This is vulnerable since if the ping_host function is called and returns its response, it can include sensitive system information from the ping output that a hacker or attacer can use for further exploits.

28. return "". It is vulnerable since when we return "", it isn't directly unsafe, it bypasses a chance to validate or handle any missing or invalid input..



### Instructions

There is a vulnerable instance of the part3 problem
hosted at the following URL:

https://localhost:8000/
 
Update the file `poc.sh` with a script
that displays the "flag" for this challenge.

The flag is located in the following path:
`/tmp/flag.txt`

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
	
