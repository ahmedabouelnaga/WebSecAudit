[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/u2FDNj6O)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17057191&assignment_repo_type=AssignmentRepo)
# HW 2: Web Security

In this homework you will audit source code of three Python3 Flask
web applications for web
security vulnerabilities. You will update the source code
to remove the vulnerabilities you find. 

Finally, you will write proof of concept exploits for
the vulnerabilities to help illustrate the significance
of the vulnerability. 

Please read the README in its entirety before starting this homework. 

## UNI: N/A

Please create a file called `UNI.txt`. Inside this file, store your UNI and nothing else. 

This will help us identify your project more quickly and resolve issues in which a student
uses a different GitHub account than they used in the first homework. 

## Overview

This homework is broken into three parts. Each part is worth 1/3 of the overall homework grade. In each part, you should:

1) 20%: Identify the vulnerabilities in writing. You should clearly identify the vulnerability by line number in writing and state why the line number is vulnerable. Place this writeup in a file called README.md for that part. You should therefore submit three writeups, located in `part1-xss/README.md`, 
`part2-sqli/README.md`, and `part3-cmd/README.md`.

2) 30%: write a proof of concept exploit for the vulnerability. In each part, follow the README instructions to document your proof of concept in
the subfolder `poc` for each part. You should therefore submit three
proofs of concept,  located in `part1-xss/poc`, 
`part2-sqli/poc`, and `part3-cmd/poc`.

For part1, we will validate the POC by pasting the URL into a chromium web browser and looking for a javascript alert.

For part2 and part3, we will validate the POC by running the following command from the `poc` directory:

```
bash poc.sh
```
We expect to see the flag printed to the console in stdout. 

3) 50%: fix the code so that the vulnerability no longer exists. The general functionality of the website in question should remain unchanged from your fix. These changes should be committed directly to the main branch. 

Observe here that in each part, identifying the vulnerability is worth 20%, fixing the vulnearbility is worth 50%, and writing a functional proof of concept is worth 30%. 

Note: there may be more than one vulnerability in the code base for each part. Be thorough in your assessment. 

Flask being in debug mode is *not* considered a vulnerability for this homework. 

## Relevant Code

In each part, when auditing the source 
code for vulnerabilities, 
you should focus your attention on the source code for the webapp itself.

Do not change the docker files or other files outside of the `webapp` folder, 
unless otherwise specified in this README (ie, the `poc` folder). 

### Part1:

The part1 flask app has the following files.

```
tree part1-xss/service/src/webapp/
part1-xss/service/src/webapp/
├── __init__.py
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       ├── game.js
│       └── jquery.min.js
├── templates
│   ├── end.html
│   └── index.html
└── views.py
```

* The `__init__.py` file initializes the web app. You can reference it to understand
the application but you shouldn't need to modify anything here. 

* The `views.py` file defines the behavior for various "routes." Routes
are essentially just the URI for a given request.

* The templates files are referenced in `views.py` and are used to generate
dynamic HTML content. These templates are jinja2 templates. Flask will
evaluate the templates on the server-side and then send the output
to the client. 

* By convention, anything in the `static` directory is directly accessible 
at the root of the application web server under the `/static/` path. 

### Part2:

```
tree part2-sqli/service/src/webapp/
part2-sqli/service/src/webapp/
├── db.py
├── __init__.py
├── schema.sql
├── setup.sql
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       └── jquery.min.js
├── templates
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── profile.html
│   └── register.html
└── views.py
```

In addition to the files mentioned in Part1:

* `db.py` provides helper functions to interface with a SQLite3 database. This database
does not have a server; instead it is a single binary file stored on disk. 
* `schema.sql` defines the database scheme. It is referenced in `__init__.py` to build
the database when the app first launches. 
* `setup.sql` is used by `__init__.py` to populate the database after it is initialized. 


### Part3:

```
tree part3-cmd/service/src/webapp/
part3-cmd/service/src/webapp/
├── __init__.py
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       ├── jquery.min.js
│       └── status.js
├── templates
│   ├── index.html
│   └── layout.html
└── views.py
```

See the Part1 file descriptions for an overview of the flask files seen in part3.

## Dependencies

This homework depends on containerization technology to 
standardize and isolate the execution environment. We use docker to 
achieve this (although other containers do exist).
You must install install docker in your VM in order
to run the web servers locally.

To update your GCP Ubuntu VM with the proper dependencies, 
run the following commands (taken from: https://docs.docker.com/engine/install/ubuntu/)

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Then run:
```
sudo groupadd docker
sudo usermod -aG docker YOUR_UNI_HERE
```

If you are willing and able to install docker on your own
computer, it should work without requiring the GCP VM. However,
this approach is not supported by the TAs for troubleshooting.

## Running each web server in docker
For each part of the homework, change into the 
directory for that part and run, `docker compose up`.

For example, in part1, this would be:

```
cd part1-xss
docker compose up
```

This will host the web server on port 8000. 

To close docker, enter "Ctrl + C" to send the "SIGINT" signal
to docker and close the container. 

When docker is running, you can 
access the web server on the IP address of your VM at port `8000`.
That is, `http://MYIP:8000/`.

Alternatively, 
you can tunnel port `8000` over SSH with the following flag:

`ssh UNI@IP -L8000:127.0.0.1:8000`

Then, you can access the web server from your own web browser
by navigating to:

`http://127.0.0.1:8000/`.

Note: you can also use python3 and pip3 to run flask directly.
This is an option if you are familiar with flask, but
if you run into issues we will tell you to use docker. 

To use this option without docker, in the folder directly
above `webapp`, run this:

```
pip3 install -r requirements.txt
python3 -m flask --app webapp run
```
In this case, you will access the server on port 5000 instead of 8000

If you make changes to the python files, you will
need to restart docker to see the changes. If you
make changes to the template HTML files, you can refresh
the web browser to see the changes. 

## Updating your Google Cloud Firewall to allow port 8000

Google Cloud has a firewall configured
that will block port 8000. To fix this this
so you can access your VM, do the following:

1. Type "Firewall" in the search to go to the Firewall settings

2. Click "Create Firewall Rule" at the top of the page. 

3. In the name section, enter, "port-8000"

4. Leave the network on default and the priority at 1000

5. In the "Direction of traffic" select "Ingress"

6. In "action on match" select "allow." Set "Targets" to
"All instances in the network." Set the source filter to 
IPV4 ranges, and enter the Source IPv4 ranges to be: 
`0.0.0.0/0`.

7. In "Protocols and ports", check "TCP" and enter `8000`

8. click "Create"


## Recommended Resources

Everything:

* Flask Documentation: most of the flask part is handled for you, but you may need
to read to understand the basics of flask routing. https://flask.palletsprojects.com/en/2.2.x/quickstart/


* Jinja Templates: These are used by flask to render HTML dynamically. https://palletsprojects.com/p/jinja/


* Javascript: you will want a reference to look up unknown functions and 
and to interact with javascript. If you want a javascript runtime to 
test code dynamically, press F12 on any website to open
the developer console and switch to the console tab. You can also use the
developer console to monitor and edit web requests in the "Network" tab.
Firefox and Chrome also offer a "Copy as CURL" option to export a request
for modification in curl. https://www.w3schools.com/js/

* Javascript JQuery POST request: https://api.jquery.com/jquery.post/

### Part1: XSS

* Base64 Encoding in Python3: https://docs.python.org/3/library/base64.html
* Base64 Encoding in javascript: https://developer.mozilla.org/en-US/docs/Glossary/Base64
* Cyber Chef: useful for modifying data and encodings quickly. https://gchq.github.io/CyberChef/
* Jinja Template Sanitization: https://jinja.palletsprojects.com/en/3.1.x/templates/#working-with-automatic-escaping -- Just what does the "safe" filter do? Is it used correctly?
* When should you sanitize inputs? Before or after decoding?
* https://www.w3schools.com/html/html_entities.asp may be useful if you decide to write your own sanitization code.

### Part2: SQL Injection

* SQLite3 documentation (the SQL variant we are using). Especially UNIONs: https://www.sqlitetutorial.net/sqlite-union/
* Header Manipulation in curl (if you prefer to use it in writing your POC): https://everything.curl.dev/http/requests/user-agent
* Python3 requests library (if you prefer it for writing your POC): https://requests.readthedocs.io/en/latest/
* Prepared Statements in SQL in flask: https://www.sqlitetutorial.net/sqlite-python/insert/, https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
* Proof of Concept resource: Python3 bcrypt https://pypi.org/project/bcrypt/
* Proof of Concept resource: sqlite3 subqueries. https://www.sqlitetutorial.net/sqlite-subquery/

### Part3: Command Injection

* Bash Subshells: (Not necessary for your POC, but can be used in some techniques) https://www.linuxtopia.org/online_books/advanced_bash_scripting_guide/subshells.html


* Safe subprocesses in Python3: https://docs.python.org/3/library/subprocess.html#subprocess.run


### GitHub Actions Auto-Grading

When you push your code, GitHub Actions
will ship a copy of your code to an auto-grader.

This auto-grader will run tests against your code
and notify you if one of the homework parts has 
a vulnerability. Note that it will not tell you
which parts of your code were vulnerable to some
injection attack, just that
an attack succeeded against your code. 
This is intended to help you know
if you have successfully patched your code. 

While reasonable attempts are made to protect the 
autograder server, attacks against this server are forbidden 
and are considered an academic integrity violation.

You can run this same test locally by running:

`make test`

After about 15 seconds, you will see an output.
If your code is vulnerable, you'll see:

```
{
  "part1": "injection succeeded",
  "part2": "injection succeeded",
  "part3": "injection succeeded"
}
```

When you have successfully secured the code, you will see:

```
{
  "part1": "No injections succeeded.",
  "part2": "No injections succeeded.",
  "part3": "No injections succeeded."
}
```
