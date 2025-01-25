## Part1 Vulnerability Proof of Concept 
 
### Instructions

There is a vulnerable instance of the part1 problem
hosted at the following URL:

https://localhost:8000/
 
Update the file `proof-of-concept.txt` with a URL 
to a reflected XSS attack in which a 
[javascript alert](https://www.w3schools.com/jsref/met_win_alert.asp) 
is displayed when the link is visited and the page
loads under a fully-patched Chromium-based web browser. 

###Identified Vulnerabilities
Cross-Site Scripting (XSS)
File Name: views.py:
Lines: 12-14
result = request.args.get("outcome", "")
board = request.args.get("board", "")
What the vulnerability is: User inputs retrieved from `request.args.get` are passed directly to the template without sanitization. In the template, the `| safe` filter is used, which prevents escaping of special characters, enabling XSS attacks.
What this vulnerabiity causes: Malicious scripts can be injected into the `outcome` and `board` query parameters, compromising the integrity and security of the application.
Why they are vulnerable:
12. result = request.args.get("outcome", ""). It is vulnerable since the request.args.get() method recieves data directly from the query paramters of the URL. Since the outcome is directly passed to the template rendering without sanitization, this can lead to a chance of an XSS attack if th attacker crafts a URL with a malicious javascript payload. The result takes the base64 encoded input without any sort of validtion.
13. board = request.args.get("board", ""). It is vulnerable since the board parameter is also directlyt taken from the query string without any input validation or some sort of sanitization.Therefore, this can lead to an XSS attack where the attacker can embed malicious scripts onto the URL. It is also vulnerable for the same reasons as seen in line 12.
14. return render_template('end.html', result=result, board=board).It is vulnerable since the result and board values are directly passed to the end.html. If the template renders these values without escaping then it leads to a chance where a hacker can inject malicious javascript onto the website.
File Name:end.html
Lines: 13 and 18 
ticTacToe.stringToGameboard(atob("{{ board | safe }}"))
("#game_result").html(atob("{{ result | safe }}"))
What the vulnerability is: It uses the safe filter which bypasses Jinja2's HTML escaping
Why it is a vulnerability:
13. ticTacToe.stringToGameboard(atob("{{ board | safe }}"));. This is vulnerable since the |safe filter disables Jinja2's automatic escaping mechanism. If board has data that is malicious then it will be directly included in the website without protection.It doesn't escape HTML content
18. $("#game_result").html(atob("{{ result | safe }}")) This is vulnerable since jquery's .html() method gives the opportunity that allows the insertion of raw HTML. If result has malicious Base64-encoded html or javascrip, decoding it and inserting it into the DOM will execute it. It also doesn't escape HTML content

File Name: game.js
Lines: 3, 40, 41, 268, 269, 295, 296
Why it is a vulnerability:
3. var SPACE = "&nbsp;";. This is vulnerable since there is a possibility that it utilizes HTML entity which can be seen or interpreteed as innerHTML. This can lead to the attacker having the opportunity to do a HTML injection attack.
40. col.innerHTML = this.model[row_index][col_index];. This is vulnerable since it directly assigns innerHTML that can iontroduce XSS vulnerabilities if the this.model data is manipulated to include malicious scripts.
41. if(col.innerHTML == SPACE && this.active) {. This is vulnerable because it compares innerHTML against SPACE which relies on HTML rendering and therefore fragile. It can fail if there are unexpected characters, whitespace differences, or formatting issues. 
268. stringToGameboard(gameString). This is vulnerable since this function splits the input gameString without any sort of validation which can lead to issues if the string is malformed or has unexpected characters.
269. var elements = gameString.split(",");. This is vulnerable since the line assumes that the gameString function is always a valid string which contains exactly 9 cells seperated by commas. However, if the gameString is malformed or has unexpected values, it can lead to errors or can also lead to behavior that is incorrect such as having undefined cells in the game board.
295. redirectToEnd(outcome). This is vulnerable since it utilizes a function called btoa() to encode the outcome and board strings. While btoa() is good enough for basic encoding, it doesn't have any sort of validation or sanitizes the input. This can lead to a malicious or broken URL if the data contains unexpected characters.
296. var board = this.gameboardToString();. This is vulnerable because the line creates a string that represents the game boaard but it doesn't validate the output. If the board model this.model iis malformed or has incorrect characters, it can lead to the resulting string being invalid or can lead to some broken behavior when it is sent to the server or rendered on the results screen.

